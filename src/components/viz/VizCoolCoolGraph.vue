<template>
<v-container>
  <div class="my-5">
    <p class="text--h4 font-tertiary text-center">And a quick look at all the cools in every season!</p>
    <p class="text--body-1 text-center">Hover over the bars to see the count and episode.</p>
  </div>
  <div id="cool-chart-container" class="my-4 text-center">
    <svg id="cool-chart"/>
    <h3 style='height: 125px; text-align: top;'>{{ caption }}</h3>
  </div>
</v-container>
  
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
      colWidth: 6,
      innerWidth: 1000,
      vizSettings: {
        scale: {},
        axis: {},
      }
    };
  },
  computed: {
    innerHeight() {
      if (this.$vuetify.breakpoint.smAndDown) {
        return 600;
      }
      return 250;
    },
    chartMargin() {
      return { top: 20, right: 10, bottom: 30, left: 10 };
    },
    chartSettings() {
      return {
        width: this.innerWidth + this.chartMargin.left + this.chartMargin.right,
        height: this.innerHeight + this.chartMargin.top + this.chartMargin.bottom,
      };
    },
    maxCools() {
      return Math.max(...this.data.map(d => d.count))
    }
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
      const svg = d3.select('#cool-chart');
      svg
        .attr('width', this.chartSettings.width)
        .attr('height', this.chartSettings.height)
        .call(this.responsivefy);

      // Generate axes
      this.vizSettings.scale.x = d3
        .scaleLinear()
        .domain([-0.5, this.data.length - 0.5])
        .range([0, this.innerWidth]);
      this.vizSettings.scale.y = d3
        .scaleLinear()
        .domain([0, this.maxCools + 5])
        .range([this.innerHeight, 0]);

      // Draw axes groups
      svg
        .append('g')
        .attr('class', 'XAxis')
        .attr('transform', `translate(${this.chartMargin.left}, ${this.innerHeight + this.chartMargin.top})`);

      // Create gradients
      let grads = svg
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
        .attr('stop-color', 'black')
        .attr('stop-opacity', '0')
      grads.append('stop')
        .attr('offset', '30%')
        .attr('stop-color', 'black')
      grads.append('stop')
        .attr('offset', '100%')
        .attr('stop-color', 'black')

      // Create bars
      this.bars = svg
        .selectAll('rect.cool-bar')
        .data(this.data).enter()
        .append('rect')
        .attr('class', 'cool-bar')
        .attr('width', this.colWidth)
        //.attr('height', d => d.count >= 0 ? d.count * 10 : 300)
        //.attr('y', d => d.count >= 0 ? 400 - d.count * 10 : 400 - 300)
        //.attr('x', (d, i) => i * (this.colWidth + 1))
        .attr('x', (d, i) => this.vizSettings.scale.x(i))
        // .attr('y', this.vizSettings.scale.y(0))
        .attr('y', d => {
          if (d.count >= 0) {
            return this.vizSettings.scale.y(d.count)
          } else {
            return this.vizSettings.scale.y(this.maxCools + 5)
          }
        })
        .attr('height', d => {
          if (d.count >= 0) {
            return this.vizSettings.scale.y(this.maxCools + 5 - d.count)
          } else {
            return this.vizSettings.scale.y(0)
          }
        })
        .attr('fill', this.getFill)

        this.hoverBars = svg
          .selectAll('rect.hover-bar')
          .data(this.data).enter()
          .append('rect')
          .attr('class', 'hover-bar')
          .attr('width', this.colWidth)
          .attr('height', this.vizSettings.scale.y(0))
          .attr('y', this.vizSettings.scale.y(this.maxCools + 5))
          .attr('x', (d, i) => this.vizSettings.scale.x(i))
          .attr('fill', 'transparent')
          .on('mousemove', this.handleMouseMove)
          .on('mouseout', this.handleMouseOut)

        svg
          .selectAll('rect.season')
          .data(d3.range(7)).enter()
          .append('rect')
          .attr('class', 'season')
          // .attr('width', d => this.getNumEpisodes(d+1) * (this.colWidth + 1) - 2)
          .attr('width', d => this.vizSettings.scale.x(this.getNumEpisodes(d+1)) - 5)
          .attr('height', 5)
          .attr('x', d => this.vizSettings.scale.x(d3.range(d).map(e => this.getNumEpisodes(e+1)).reduce((a, b) => a + b, 0)))
          // .attr('x', d => d3.range(d).map(e => this.getNumEpisodes(e+1)).reduce((a, b) => a + b, 0) * (this.colWidth + 1))
          .attr('y', this.vizSettings.scale.y(0))
        svg
          .selectAll('text.season')
          .data(d3.range(7)).enter()
          .append('text')
          .attr('class', 'season')
          .attr('x', d => this.vizSettings.scale.x(d3.range(d).map(e => this.getNumEpisodes(e+1)).reduce((a, b) => a + b, 0)))
          .attr('y', this.vizSettings.scale.y(0) + 25)
          .text(d => 'Season ' + (d + 1))
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