<template>
  <section class="section_wrapper py-12">
    <div class="text-block" style="text-align: center; background: #fff534;">
      <h2 class="mb-4">And a quick look at all the cools in every season!</h2>
      <p class="text--body-1">
        Hover over the bars to see the count and episode.
      </p>
      <div>              
        <svg id="cool-chart"/>
      </div>
    <h3 style='height: 25px;'>{{ caption }}</h3>
    </div>
  </section>
</template>

<script>
import * as d3 from 'd3';

export default {
  name: 'VizCoolCoolGraph',
  components: {},
  data() {
    return {
      publicPath: process.env.BASE_URL,
      // colors: [
      //   '#273c75',
      //   '#c23616',
      //   '#44bd32',
      //   '#fa8231',
      //   '#8854d0',
      //   '#0fb9b1',
      //   '#718093'
      // ],
      colors: [
        'black',
        'black',
        'black',
        'black',
        'black',
        'black',
        'black'
      ],
      caption: '',
      colWidth: 8,
      width: 1200,
    };
  },
  mounted() {
    this.loadData()
    this.width = this.$el.clientWidth;
  },
  methods: {
    async loadData() {
      this.data = await d3.csv('/data/cool_counts.csv')
      this.$nextTick(() => {
        this.drawChart()
      })
    },
    drawChart() {
      d3.select('svg#cool-chart').attr('transform', 'translate(50, 0)')
      let grads = d3.select('svg#cool-chart')
        .append('defs')
        .selectAll('linearGradient')
        .data(d3.range(7)).enter()
        .append('linearGradient')
        .attr('id', d => 'Gradient' + d)
        .attr('x1', '0')
        .attr('x2', '0')
        .attr('y1', '0')
        .attr('y2', '1')
      grads.append('stop')
        .attr('offset', '0%')
        .attr('stop-color', d => this.colors[d])
        .attr('stop-opacity', '0')
      grads.append('stop')
        .attr('offset', '30%')
        .attr('stop-color', d => this.colors[d])
      grads.append('stop')
        .attr('offset', '100%')
        .attr('stop-color', d => this.colors[d])
      
      this.bars = d3.select('svg#cool-chart')
        .attr('width', this.width)
        .attr('height', 500)
        .selectAll('rect.cool-bar')
        .data(this.data).enter()
        .append('rect')
        .attr('class', 'cool-bar')
        .attr('width', this.colWidth)
        .attr('height', d => d.count >= 0 ? d.count * 10 : 300)
        .attr('y', d => d.count >= 0 ? 400 - d.count * 10 : 400 - 300)
        .attr('x', (d, i) => i * (this.colWidth + 1))
        .attr('fill', this.getFill)

      this.hoverBars = d3.select('svg#cool-chart')
        .selectAll('rect.hover-bar')
        .data(this.data).enter()
        .append('rect')
        .attr('class', 'hover-bar')
        .attr('width', this.colWidth)
        .attr('height', 500)
        .attr('y', -100)
        .attr('x', (d, i) => i * (this.colWidth + 1))
        .attr('fill', 'transparent')
        .on('mousemove', this.handleMouseMove)
        .on('mouseout', this.handleMouseOut)

      d3.select('svg#cool-chart')
        .selectAll('rect.season')
        .data(d3.range(7)).enter()
        .append('rect')
        .attr('class', 'season')
        .attr('width', d => this.getNumEpisodes(d+1) * (this.colWidth + 1) - 2)
        .attr('height', 5)
        .attr('x', d => d3.range(d).map(e => this.getNumEpisodes(e+1)).reduce((a, b) => a + b, 0) * (this.colWidth + 1))
        .attr('y', 400 + 1)
      d3.select('svg#cool-chart')
        .selectAll('text.season')
        .data(d3.range(7)).enter()
        .append('text')
        .attr('class', 'season')
        .attr('x', d => d3.range(d).map(e => this.getNumEpisodes(e+1)).reduce((a, b) => a + b, 0) * (this.colWidth + 1) + 1)
        .attr('y', 400 + 25)
        .text(d => 'Season ' + (d + 1))
      d3.select('svg#cool-chart')
        .call(this.responsivefy)
    },
    getNumEpisodes(season) {
      return this.data.filter(d => parseInt(d.episode.substr(1, 3)) == season).length
    },
    getFill(d) {
      if (d.count >= 0) {
        return this.colors[parseInt(d.episode.substr(1, 3)) - 1]
      } else {
        return 'url(#Gradient' + (parseInt(d.episode.substr(1, 3)) - 1) + ')'
      }
    },
    handleMouseMove(target, d) {
      let i = this.hoverBars.nodes().indexOf(target.target)
      d3.select(this.bars.nodes()[i])
        .attr('fill', '#fff534')
        .attr('stroke', '#000000')
      if (d.count > 1) {
        this.caption = `${d.episode} has ${d.count} "cool"s.`
      } else if (d.count == 1) {
        this.caption = `${d.episode} has ${d.count} "cool".`
      } else if (d.count == 0) {
        this.caption = `${d.episode} has ${d.count} "cool"s. Booooo.`
      } else {
        this.caption = `${d.episode} has too many "cool"s to count. 😎`
      }
    },
    handleMouseOut(target, d) {
      let i = this.hoverBars.nodes().indexOf(target.target)
      d3.select(this.bars.nodes()[i])
        .attr('fill', d.count >= 0 ? '#000000' : 'url(#Gradient' + (parseInt(d.episode.substr(1, 3)) - 1) + ')')
        .attr('stroke', '')
      this.caption = ''
    },    
    responsivefy(svg) {
      const width = parseInt(svg.style('width'), 10);
      const height = parseInt(svg.style('height'), 10);
      const aspect = width / height;

      svg
        .attr('viewBox', `0 0 ${width} ${height}`)
        .attr('preserveAspectRatio', 'xMinYMid')
        .call(this.resize, aspect);

      d3.select(window).on('resize.test', () => {
        this.resize(svg, aspect);
      });
    },
    resize(svg, aspect) {
      const container = d3.select(svg.node().parentNode);
      const w = Math.min(parseInt(container.style('width'), 10), 1000);

      svg.attr('width', w);
      svg.attr('height', Math.round(w / aspect));
    },
  },
}
</script>

<style lang="scss" scoped>
svg#cool-chart {
  //border: 1px solid red;
  margin-left: auto;
  margin-right: auto;
  display: block;
}
.text-block {
  background-color: white;
  color: #2E2E2E;
  padding: 24px;
}
</style>