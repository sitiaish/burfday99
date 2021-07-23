<template>
  <div class="pa-12" style="background: white;">
    <v-container>
      <v-row align="center" justify="center">
        <p class="text--h2 font-tertiary text-center">
          A quick look at insults across the seasons
        </p>
        <svg id='wuntch-holt'/>
      </v-row>
    </v-container>
    <!-- <v-select 
        style="width: 130px;"
        item-text="name"
        item-value="value"
        v-model="insultType"      
        :items="insultTypes"
        @input="updateChart()" />
    <v-container>
      <h3>Insults Given</h3>
      <svg id='wuntch-holt2' style="border: 1px solid black;"/>
    </v-container> -->
    <v-container>
      <v-row align="center" justify="center">
        <v-col cols="3">
          <img :src="holtImage" style="width: 100%; margin: auto; display: block;"/>
        </v-col>
        <v-col cols="6" v-if="line">
          <h3 style="text-align: center;">"{{ line }}"</h3>
        </v-col>
        <v-col cols="3">
          <img :src="wuntchImage" style="width: 100%; margin: auto; display: block;"/>
        </v-col>
      </v-row>
      <v-row v-if="foundIn" align="center" justify="center">
        <h3 style="background: #fff534;">{{ foundIn }}</h3>
      </v-row>
      <v-row class="data-row" no-gutters align="center" justify="center" v-for="(data, id) in selectedConvo" :key="id">
        <!-- use a v-for to populate the divs  -->
        <!-- <v-col cols="1">
          <h2>S{{data[1][0].season}}E{{data[1][0].episode}}</h2>
        </v-col> -->
        <v-col cols="8">
          <div class="pa-3">
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
      insultType: 'all',
      insultTypes: [
        {name: "Fantasy", value: 'fantasy'},
        {name: "Animal", value: 'animal'},
        {name: "Physical", value: 'physical'},
        {name: "Others", value: 'others'},
        {name: "All", value: 'all'}
      ],
      line: '',
      selectedConvoId: -1,
      holtImage: '',
      wuntchImage: '',
      foundIn: ''
    };
  },   
  mounted() {
    // to run format data on load
    this.loadData()
  },
  computed: {
    groupedData() {
      return d3.filter(d3.groups(this.data, d => d.id), d => d[1].some(e => e.type === this.insultType || this.insultType === 'all'))
    },
    selectedConvo() {
      return d3.filter(d3.groups(this.data, d => d.id), d => d[0] === this.selectedConvoId)
    }
  },
  methods: {
    async loadData() {
      this.data = await d3.csv('/data/wuntch-holt-new.csv')
      this.$nextTick(() => {
        this.updateChart()
        // this.makeChartVertical()
        const svg = d3.select('svg#wuntch-holt')
        svg.call(this.responsivefy)
      })
    },
    updateChart() {
      console.log('horizontaling')
      const svg = d3.select('svg#wuntch-holt')
                    // .attr('height', 300)
                    // .attr('width', 1200)
      svg.selectAll('g.insult-types')
        .data([]).exit().remove()
      const data = d3.groups(d3.filter(this.data, d => d.type != '' && (d.who === 'Holt' || d.who === 'Wuntch')), d => d.type, d => d.who)
      
      let insultTypes = svg.selectAll('g.insult-types')
        .data(data).enter()
        .append('g')
        .attr('class', 'insult-types')
        .attr('transform', d => {
          const insultTypesY = {
            fantasy: 0,
            work: 1,
            physical: 2,
            animal: 3,
            others: 4,
          }
          return 'translate(600 ' + (insultTypesY[d[0]] * 40 + 15) + ')'
        })

      insultTypes.append('rect')
        .attr('x', -42)
        .attr('y', -5)
        .attr('height', 30)
        .attr('width', 84)
        .attr('fill', '#fff534')
      insultTypes.append('text')
        .text(d => d[0])
        .attr('text-anchor', 'middle')
        .attr('y', 15)
        // .style('font-family', 'Anton')
        .style('font-weight', 'bold')
        .style('font-size', 32)

      let insultWhos = insultTypes.selectAll('g')
        .data(d => d[1]).enter()
        .append('g')
      
      insultWhos.selectAll('rect')
        .data(d => d[1]).enter()
        .append('rect')
        .attr('who', d => d.who)
        .attr('x', (d, i) => d.who === 'Wuntch' ? 28 * (i + 2) - 14 : -28 * (i + 2) - 14)
        .attr('y', -5)
        .attr('height', 30)
        .attr('width', 28)
        .attr('fill', d => {
          switch (d.who) {
            case 'Holt': return '#1e3799'
            case 'Wuntch': return '#eb2f06'
            default: return 'grey'
          }
        })
        .on("mouseover", (target, d) => {
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
        })
        .on('mouseout', target => {
          d3.select(target.target)
            .attr('stroke', 'none')
            .attr('fill', d => d.who === 'Holt'? '#1e3799' : '#eb2f06')
        })

      insultWhos.selectAll('text')
        .data(d => d[1]).enter()
        .append('text')
        .attr('who', d => d.who)
        .attr('x', (d, i) => d.who === 'Wuntch' ? 28 * (i + 2) - 14 : -28 * (i + 2) - 14)
        .attr('y', 20)
        .text('💀')
        .attr('font-size', 28)
        .style('pointer-events', 'none')
    },
    updateChartVertical() {
      console.log('verticaling')
      const svg = d3.select('svg#wuntch-holt')
                    // .attr('height', 800)
                    // .attr('width', 210)
      const data = d3.groups(d3.filter(this.data, d => d.type != '' && (d.who === 'Holt' || d.who === 'Wuntch')), d => d.type, d => d.who)

      svg.selectAll('g.insult-types')
        .data([]).exit().remove()
      
      let insultTypes = svg.selectAll('g.insult-types')
        .data(data).enter()
        .append('g')
        .attr('class', 'insult-types')
        .attr('transform', d => {
          const insultTypesY = {
            fantasy: 0,
            work: 1,
            physical: 2,
            animal: 3,
            others: 4,
          }
          return 'translate(' + (insultTypesY[d[0]] * 40 + 70) + ' 600)'
        })

      insultTypes.append('rect')
        .attr('x', 0)
        .attr('y', -42 + 74)
        .attr('height', 84)
        .attr('width', 30)
        .attr('fill', '#fff534')
      insultTypes.append('text')
        .text(d => d[0])
        .attr('transform', 'rotate(270)')
        .attr('text-anchor', 'middle')
        .attr('y', 18)
        .attr('x', -74)
        // .style('font-family', 'Anton')
        .style('font-weight', 'bold')
        .style('font-size', 32)
        
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
        .attr('width', 28)
        .attr('fill', d => {
          switch (d.who) {
            case 'Holt': return '#1e3799'
            case 'Wuntch': return '#eb2f06'
            default: return 'grey'
          }
        })
        .on("mouseover", (target, d) => {
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
        })
        .on('mouseout', target => {
          d3.select(target.target)
            .attr('stroke', 'none')
            .attr('fill', d => d.who === 'Holt'? '#1e3799' : '#eb2f06')
        })

      insultWhos.selectAll('text')
        .data(d => d[1]).enter()
        .append('text')
        .attr('who', d => d.who)
        .attr('x', 0)
        .attr('y', (d, i) => -i * 30 + 26)
        .text('💀')
        .attr('font-size', 28)
        .style('pointer-events', 'none')
    },
    responsivefy(svg) {
      // const width = parseInt(svg.style('width'), 10);
      // const height = parseInt(svg.style('height'), 10);
      // const aspect = width / height;
      let aspect = null
      // if (width < 600) {
      //   aspect = 0.45
      // } else {
      //   aspect = 2.25
      // }
      // const height = Math.round(width / aspect)
      // console.log(width)
      // console.log(height)

      // svg.attr('viewBox', `0 0 ${width} ${height}`)
      //   .attr('preserveAspectRatio', 'xMinYMid')
      //   .call(this.resize, aspect);
      this.resize(svg, aspect)

      d3.select(window).on('resize.test', () => {
        this.resize(svg, aspect);
      });
    },
    resize(svg, aspect) {
      const container = d3.select(svg.node().parentNode);
      const w = parseInt(container.style('width'), 10)
      if (w < 600) {
        aspect = 0.5
      } else {
        aspect = 4
      }
      const h = Math.round(w / aspect)
      console.log(w)
      console.log(h)
      // const w = Math.min(parseInt(container.style('width'), 10), 1200);
      svg.attr('width', w);
      svg.attr('height', h);
        
      
      // const container = d3.select(svg.node().parentNode);
      // const w = Math.min(parseInt(container.style('width'), 10), 1200);

      // console.log(w)
      if (w < 600) {
        svg.attr('viewBox', `0 0 ${400} ${800}`)
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
  //margin: 5px;
  margin-right: 8px;  
  display: inline;
  border-radius: 25px;
  font-size: 18px;
  //color: transparent;
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
</style>
