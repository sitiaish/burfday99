<template>
  <v-container outer class="container--fluid scrolly-side">
    <v-row justify="space-between" align="start">  
      <v-col cols="12" md="4" class="scrolly__content">

        <div class="step first" data-step="1">
          <div class="text-block">         
          </div>
        </div>                                              
      </v-col>

      <v-col cols="12" md="2" class="casestudy-scrolly scrolly__sticky">
        <div>
          <p class="text--body-2 bangladesh-step-1 bangladesh-tab">Screened</p>
        </div>

        <div>
          <p class="text--body-2 bangladesh-step-2 bangladesh-tab">Diagnosed</p>
        </div>

        <div>
          <p class="text--body-2 bangladesh-step-3 bangladesh-tab">Put on treatment</p>
        </div>                                            
      </v-col>        

      <v-col cols="12" md="6" class="scrolly__sticky">
        <svg id='coolcool-viz' />
        <p class="text--body-3 my-4">Each circle represents 10 cases [desktop]</p>
      </v-col> 
    </v-row>
  </v-container> 
</template>

<script>
import * as d3 from 'd3';
import scrollama from 'scrollama';

export default {
  name: 'VizCoolCoolScrollySide',
  mounted() {
    this.initScrollama()
    this.loadData()
  },
  components: {},
  data() {
    return {
      publicPath: process.env.BASE_URL,
    };
  },
  methods: {
    async loadData() {
      this.data = await d3.csv('/data/coolcool.csv')
      this.$nextTick(() => {
        this.drawChart()
      })
    },
    drawChart() {
      d3.select('svg#coolcool-viz')
        .attr('height', '800px')
        .attr('width', '500px')
        .selectAll('g.cool-line')
        .data(this.data).enter()
        .append('g')
        .attr('class', 'cool-line')
        .attr('transform', (d, i) => 'translate(0,' + i * 25 + ')')
        .append('g')
        .attr('class', d => 'line-' + d.nCool)
        // .attr('transform', d => d.nCool == 2 ? 'translate(1000,0)' : 'translate(100,0)')
        .selectAll('text')
        .data(d => d3.range(d.nCool)).enter()
        .append('text')
        .attr('class', (d, i) => i < 6 ? 'cool-' + i : 'cool-n')
        // .attr('x', (d, i) => i * 35 + 50)
        .attr('x', 1000)
        .attr('y', 50)
        .text('cool')
    },
    initScrollama() {
      // instantiate scrollama
      const scrollerDesktop = scrollama();

      // const stepH = Math.floor(window.innerHeight * 1);
      const stepH = 1000
      d3.selectAll('.step').style("height", stepH + "px");    

      // setup scrollama
      scrollerDesktop.setup({
        container: '.scrolly-side',
        graphic: '.scrolly-side .scrolly__sticky',
        step: '.scrolly-side .scrolly__content .step', // required
        offset: 0.8,
        progress: true,
        debug: false,
      })
      .onStepEnter(this.handleStepEnter)
      .onStepProgress(this.handleStepProgress)
    },
    handleStepEnter({ element }) {
      console.log(element)
    },
    handleStepProgress(response) {
      console.log(response.progress)
      this.moveLine(response.progress)
    },
    moveLine(progress) {
      for (let i=0;i<6;i++) {
        let p = Math.min(Math.max(progress, i * 0.1), i * 0.1 + 0.2)
        p -= i * 0.1
        p /= 0.2
        d3.selectAll('text.cool-' + i)
          .attr('x', 500 - p * 500 + i * 35)
      }
      let p = Math.min(Math.max(progress, 0.8), 0.9)
      p -= 0.8
      p /= 0.1
      console.log(p)
      d3.selectAll('text.cool-n')
        .attr('x', d => 500 - p * 500 + d * 35)
    }
  },
}
</script>

<style lang="scss" scoped>
#coolcool-viz {
  border: 1px solid black;
}
.text-block {
  background-color: white;
  color: #2E2E2E;
  padding: 36px;
}

.casestudy-scrolly {
  text-align: right;
  div {
    p {
      display: inline-block;
      padding: 4px 12px;
      border-radius: unset;
      border: 1px solid #2E2E2E;
      background-color: transparent;
    }

    p.active-selection {
      background-color: #425D70;
      color: #FAFAFA;
    }
  }  
}

.dot-bangladesh-scrolly {
  height: 12px;
  width: 12px;
  border-radius: 50%;
  display: inline-block;
  background-color: #425D70;
  margin-right: 8px;
}

.scrolly__side {
  position: relative;
}

.scrolly__content {
  position: relative;
  padding: 0 1rem;
  width: 100%;
}

.step {
  margin: 0 auto 2rem auto;
  // border: 2px solid #104E8B;
  display: flex;
  justify-content: center;
  align-items: center;    
}

.step:first-child {
  margin-top: calc(25vh);
}

.scrolly__sticky {
  justify-content: center;  
  align-items: center;
  position: sticky;
  top: calc(64px + 64px);
  z-index: 1;
  height: calc(100vh - 64px - 64px);
}

</style>