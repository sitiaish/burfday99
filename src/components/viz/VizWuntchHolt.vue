<template>
  <div class="py-12 viz-wuntch-holt">
    <v-container class="py-lg-12">
      <v-row align="center" justify="center">
        <p class="text--h2 font-tertiary text-center mb-4">
          A quick look at insults across the seasons
        </p>

        <p class="text--body-1 text-center">
          Hover over the skulls to see the back and forth between Wuntch and Holt!<br/>
          (/editor's note: I think SK had a little bit of fun with the extra doodles) 
        </p>        
        
      </v-row>
    </v-container>

    <v-container outer>
      <svg id='wuntch-holt'/>
    </v-container>
    
    <v-container>
      <v-row align="start" align-md="center" justify="center">
        <v-col cols="3">
          <img :src="holtImage" style="width: 100%; margin: auto; display: block;"/>
        </v-col>
        <v-col cols="6" v-if="line">
          <h3 class="text--h4" style="text-align: center;">"{{ line }}"</h3>
        </v-col>
        <v-col cols="3">
          <img :src="wuntchImage" style="width: 100%; margin: auto; display: block;"/>
        </v-col>
      </v-row>
      <v-row v-if="foundIn" align="center" justify="center">
        <h3 style="background: #fff534;">{{ foundIn }}</h3>
      </v-row>
      <v-row class="data-row" no-gutters align="center" justify="center" v-for="(data, id) in selectedConvo" :key="id">
        <v-col cols="12" md="8">
          <div class="pa-3 mt-8">
            <p 
              v-for="(n, i) in data[1]"
              :key="i"
              :class="['mb-0, line', n.who === 'Wuntch' || n.who === 'Holt' ? n.who : 'other', n.type === '' ? '' : 'insult', n.line === line ? 'selected-insult' : '']"> 
                {{ n.line }}
            </p>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </div>
</template>

<script>
import * as d3 from 'd3';

export default {
  data() {
    return {
      data: [],
      insultTypes: ['fantasy', 'work', 'physical', 'animal', 'others'],
      line: '',
      selectedConvoId: -1,
      holtImage: '',
      wuntchImage: '',
      foundIn: ''
    };
  },   
  mounted() {
    this.loadData()
  },
  computed: {
    selectedConvo() {
      // Group and filter data by conversation ID
      return d3.filter(d3.groups(this.data, d => d.id), d => d[0] === this.selectedConvoId)
    },
    groupedData() {
      // Group and filter data by insult type and who said it
      return d3.groups(d3.filter(this.data, d => d.type != '' && (d.who === 'Holt' || d.who === 'Wuntch')), d => d.type, d => d.who)
    }
  },
  methods: {
    async loadData() {
      this.data = await d3.csv('/data/wuntch-holt-new.csv')
      this.$nextTick(() => {
        this.updateChart()
        const svg = d3.select('svg#wuntch-holt')
        svg.call(this.responsivefy)
      })
    },
    cleanSlate() {
      // Start from clean slate whenever we update the chart
      d3.select('svg#wuntch-holt')
        .selectAll('g.insult-types')
        .data([]).exit().remove()
    },
    updateChart() {
      this.cleanSlate()
      const svg = d3.select('svg#wuntch-holt');

      // Add 1 <g> per insult type
      let insultTypes = svg.selectAll('g.insult-types')
        .data(this.groupedData).enter()
        .append('g')
        .attr('class', 'insult-types')
        .attr('transform', d => `translate(700 ${(this.insultTypes.indexOf(d[0]) * 50 + 15)})`)

      // Add labels
      insultTypes.append('rect')
        .attr('x', -60)
        .attr('y', -5)
        .attr('height', 30)
        .attr('width', 120)
        .attr('fill', '#fff534')
      insultTypes.append('text')
        .text(d => d[0])
        .attr('text-anchor', 'middle')
        .attr('y', 20)
        .attr('class', 'insult-label')
        .style('font-family', 'Anton')
        .style('font-weight', 'bold')

      // For each insult type, add 1 <g> per person (Wuntch/Holt)
      let insultWhos = insultTypes.selectAll('g')
        .data(d => d[1]).enter()
        .append('g')
      
      // For each person, add 1 <rect> per insult
      insultWhos.selectAll('rect')
        .data(d => d[1]).enter()
        .append('rect')
        .attr('who', d => d.who)
        .attr('x', (d, i) => (d.who === 'Wuntch' ? 1 : -1) * 30 * (i + 2.7) - 15)
        .attr('y', -5)
        .attr('height', 30)
        .attr('width', 30)
        .attr('fill', d => d.who === 'Holt' ? '#1e3799' : '#eb2f06')
        .on("mouseover", this.handleMouseOver)
        .on('mouseout', this.handleMouseOut)
      insultWhos.selectAll('image')
        .data(d => d[1]).enter()
        .append('image')
        .attr('who', d => d.who)
        .attr('x', (d, i) => (d.who === 'Wuntch' ? 1 : -1) * 30 * (i + 2.7) - 15)
        .attr('y', -5)
        .attr('height', 30)
        .attr('width', 30)
        .attr('href', d => d.who === 'Holt' ? '/holt_dp.png' : '/wuntch_dp.png')
        .style('pointer-events', 'none') // Pass through pointer, so we just use underlying rect's mouseover
    },
    updateChartVertical() {
      this.cleanSlate()
      const svg = d3.select('svg#wuntch-holt')
                    // .attr('height', 800)
                    // .attr('width', 210)
      
      // Add 1 <g> per insult type
      let insultTypes = svg.selectAll('g.insult-types')
        .data(this.groupedData).enter()
        .append('g') // Append 1 <g> per insult type
        .attr('class', 'insult-types')
        .attr('transform', d => `translate(${(this.insultTypes.indexOf(d[0]) * 40 + 70)} 600)`)
      // Add labels
      insultTypes.append('rect')
        .attr('x', 0)
        .attr('y', -42 + 74)
        .attr('height', 84)
        .attr('width', 30)
        .attr('fill', '#fff534')
      insultTypes.append('text')
        .text(d => d[0])
        .attr('transform', 'rotate(270)')
        .attr('text-anchor', 'end')
        .attr('class', 'insult-label')
        .attr('x', -40)
        .attr('y', 25)
        .style('font-family', 'Anton')
        .style('font-weight', 'bold');
      
      // For each insult type, add 1 <g> per person (Wuntch/Holt)
      let insultWhos = insultTypes.selectAll('g')
        .data(d => d[1]).enter()
        .append('g')
      
      insultWhos.selectAll('rect')
        .data(d => d[1]).enter()
        .append('rect')
        .attr('who', d => d.who)
        .attr('x', 0)
        .attr('y', (d, i) => -i * 30)
        .attr('height', 30)
        .attr('width', 30)
        .attr('fill', d => d.who === 'Holt'? '#1e3799' : '#eb2f06')
        .on("mouseover", this.handleMouseOver)
        .on('mouseout', this.handleMouseOut)

      insultWhos.selectAll('image')
        .data(d => d[1]).enter()
        .append('image')
        .attr('who', d => d.who)
        .attr('x', 0)
        .attr('y', (d, i) => -i * 30)
        .attr('height', 30)
        .attr('width', 30)
        .attr('href', d => d.who === 'Holt' ? '/holt_dp.png' : '/wuntch_dp.png')
        .style('pointer-events', 'none') // Pass through pointer, so we just use underlying rect's mouseover
    },
    handleMouseOver(target, d) {
      this.selectedConvoId = d.id
      this.line = d.line
      if (d.who != 'Wuntch') {
        this.holtImage = 'holt_dp.png'
        this.wuntchImage = `wuntch_dp_${d.type}.png`
      } else {
        this.wuntchImage = 'wuntch_dp.png'
        this.holtImage = `holt_dp_${d.type}.png`
      }
      this.foundIn = `Found in S${d.season}E${d.episode}...`
      d3.select(target.target)
        .style('cursor', 'pointer')
        .attr('stroke', '#fff534')
        .attr('fill', '#fff534')
    },
    handleMouseOut(target) {
      d3.select(target.target)
        .attr('stroke', 'none')
        .attr('fill', d => d.who === 'Holt'? '#1e3799' : '#eb2f06')
    },
    responsivefy(svg) {
      this.resize(svg)
      d3.select(window).on('resize.test', () => {
        this.resize(svg);
      });
    },
    resize(svg) {
      const container = d3.select(svg.node().parentNode);
      let w = parseInt(container.style('width'), 10)
      let aspect = null
      if (w < 600) {
        w -= 50
        aspect = 3/8
      } else {
        aspect = 4
      }
      const h = Math.round(w / aspect)
      svg.attr('width', w);
      svg.attr('height', h);
      if (w < 600) {
        svg.attr('viewBox', `0 0 ${300} ${800}`)
          .attr('preserveAspectRatio', 'xMinYMid')
        this.updateChartVertical()
      } else {
        svg.attr('viewBox', `0 0 ${1200} ${300}`)
          .attr('preserveAspectRatio', 'xMinYMid')
        this.updateChart()
      }
    },
  },
};
</script>

<style lang="scss" scoped>
.viz-wuntch-holt {
  background: #ffffff;
}

.Wuntch {
  background: repeating-linear-gradient(
    45deg,
    rgba(0, 0, 0, 0.4),
    rgba(0, 0, 0, 0.4) 10px,
    rgba(0, 0, 0, 0.5) 10px,
    rgba(0, 0, 0, 0.5) 20px), #eb2f06;
}

.Wuntch:before {
  content: url(/wuntch_tiny.png);
  vertical-align: text-top; 
}

.Holt {
  background: repeating-linear-gradient(
    45deg,
    rgba(0, 0, 0, 0.4),
    rgba(0, 0, 0, 0.4) 10px,
    rgba(0, 0, 0, 0.5) 10px,
    rgba(0, 0, 0, 0.5) 20px), #1e3799;
}

.Holt:before {
  content: url(/holt_tiny.png);
  vertical-align: text-top; 
}

.other {
  background: repeating-linear-gradient(
    45deg,
    rgba(0, 0, 0, 0.4),
    rgba(0, 0, 0, 0.4) 10px,
    rgba(0, 0, 0, 0.5) 10px,
    rgba(0, 0, 0, 0.5) 20px), #57606f;
}

.data-row {
  background-color: rgba(255, 255, 255, 0.7);
  margin: 2px;
}

.data-row:hover {
  background-color: rgba(0, 0, 0, 0.1);
  cursor: pointer;
}

.line {
  padding: 0px 4px;
  margin-right: 8px;  
  display: inline;
  border-radius: 25px;
  font-size: 18px;
  color: grey;
  user-select: none;
  cursor: pointer;  
  overflow-wrap: break-word;
}

.line:hover {
  color: white;
}

.insult {
  background-image: unset !important;
  color: white;
}

.selected-insult {
  border: 3px solid yellow;
}

text {
  cursor: pointer;
}

.text--h4 {
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    font-size: 18px !important;
  }
} 
</style>

<style lang="scss">
text.insult-label {
  font-size: 32px;
  @media #{map-get($display-breakpoints, 'xl-only')} {
    font-size: 34px;
  }
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    font-size: 30px;
  }  
}
</style>