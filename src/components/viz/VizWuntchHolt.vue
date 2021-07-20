<template>
  <div class="pa-12">
    <v-select 
        style="width: 130px;"
        item-text="name"
        item-value="value"
        v-model="insultType"      
        :items="insultTypes"
        @input="updateChart()" />
    <v-container>
      <h3>Insults Given</h3>
      <svg id='wuntch-holt' style="border: 1px solid black;"/>
    </v-container>
    <v-container style="height: 250px; overflow: scroll;">
      <v-row class="data-row" no-gutters align="center" justify="center" v-for="(data, id) in groupedData" :key="id">
        <!-- use a v-for to populate the divs  -->
        <v-col cols="1">
          <h2>S{{data[1][0].season}}E{{data[1][0].episode}}</h2>
        </v-col>
        <v-col cols="8">
          <div class="pa-3">
            <p 
              v-for="(n, i) in data[1]"
              :key="i"
              :class="['mb-0, line', n.who === 'Wuntch' || n.who === 'Holt' ? n.who : 'other', n.type === '' ? '' : 'insult']"> 
                {{n.line}}
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
    };
  },   
  mounted() {
    // to run format data on load
    this.loadData()
  },
  computed: {
    groupedData() {
      return d3.filter(d3.groups(this.data, d => d.id), d => d[1].some(e => e.type === this.insultType || this.insultType === 'all'))
    }
  },
  methods: {
    async loadData() {
      this.data = await d3.csv('/data/wuntch-holt-new.csv')
      this.$nextTick(() => {
        this.updateChart()
      })
    },
    updateChart() {
      const svg = d3.select('svg#wuntch-holt')
                    .attr('height', 350)
                    .attr('width', 1200)

      const data = d3.groups(d3.filter(this.data, d => d.type === this.insultType || this.insultType === 'all'), d => d.who)

      let bars = svg.selectAll('rect.insult-bars')
        .data(data)
      bars.exit().remove()
      bars.enter()
        .append('rect')
        .attr('class', 'insult-bars')
        .merge(bars)
        .attr('x', 10)
        .attr('y', (d, i) => i * 30)
        .attr('fill', d => {
          switch(d[0]) {
            case 'Holt':
              return 'blue'
            case 'Wuntch':
              return 'red'
            default:
              return 'grey'
          }
        })
        .attr('width', d => d[1].length * 5)
        .attr('height', 20)
    }
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
  background-color: rgba(0, 0, 0, 0.1);
  margin: 2px;
}

.data-row:hover {
  background-color: rgba(255, 255, 255, 0.7);
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
</style>
