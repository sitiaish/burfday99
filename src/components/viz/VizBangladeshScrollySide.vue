<template>
  <v-container outer class="container--fluid scrolly-side">
    <v-row justify="space-between" align="start">  
      <v-col cols="12" md="4" class="scrolly__content">

        <div class="step first" data-step="1">
          <div class="text-block">         
          </div>
        </div>

        <div class="step first" data-step="2">
          <div class="text-block">           
          </div>
        </div>

        <div class="step first" data-step="3">
          <div class="text-block">          
          </div>
        </div>

        <div class="step first" data-step="4">
          <div class="text-block">      
          </div>
        </div>

        <div class="step first" data-step="5">
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

        <div>
          <p class="text--body-2 bangladesh-step-4 bangladesh-tab">Completed treatment</p>
        </div>

        <div>
          <p class="text--body-2 bangladesh-step-5 bangladesh-tab">Cured</p>
        </div>                                              
      </v-col>        

      <v-col cols="12" md="6" class="scrolly__sticky">        
        <div class="bangladesh-case-numbers-scrolly">                            
          <span v-for="(n, i) in data.cured" :key="i + '-cured'" class="dot-bangladesh-scrolly cured-scrolly-1" /> 
          <span v-for="(n, i) in data.finTreatment" :key="i + '-finTreatment'" class="dot-bangladesh-scrolly finTreatment-scrolly-1" /> 
          <span v-for="(n, i) in data.onTreatment" :key="i + '-onTreatment'" class="dot-bangladesh-scrolly onTreatment-scrolly-1" /> 
          <span v-for="(n, i) in data.diagnosed" :key="i + '-diagnosed'" class="dot-bangladesh-scrolly diagnosed-scrolly-1"/> 
          <span v-for="(n, i) in data.undiagnosed" :key="i + '-undiagnosed'" class="dot-bangladesh-scrolly undiagnosed-scrolly-1"/> 
        </div>
        <p class="text--body-3 my-4">Each circle represents 10 cases [desktop]</p>
      </v-col> 
    </v-row>
  </v-container> 
</template>

<script>
import * as d3 from 'd3';
import scrollama from 'scrollama';

export default {
  name: 'VizBangladeshScrollySide',
  components: {},
  data() {
    return {
      publicPath: process.env.BASE_URL,
      data: {
        screened: 630, 
        undiagnosed: 258,
        diagnosed: 159,
        onTreatment: 120,
        finTreatment: 72,
        cured: 21,
        selectedPakistanCases: '',
      }
    };
  },
  mounted() {
    this.initScrollama();    
  },  
  methods: {
    initScrollama() {
      // instantiate scrollama
      const scrollerDesktop = scrollama();

      const stepH = Math.floor(window.innerHeight * 1);
      d3.selectAll('.step').style("height", stepH + "px");    

      // setup scrollama
      scrollerDesktop.setup({
        container: '.scrolly-side',
        graphic: '.scrolly-side .scrolly__sticky',
        step: '.scrolly-side .scrolly__content .step', // required
        offset: 0.8,
        debug: false
      })
      .onStepEnter(this.handleStepEnter)
    },
    handleStepEnter({ element }) {
      const step = d3.select(element).attr('data-step');

      // change the tabs
      d3.selectAll('p.bangladesh-tab').classed('active-selection', false)
      d3.select(`p.bangladesh-step-${step}`).classed('active-selection', true);

      // change the dots
      switch (step) {
        case '1':
          this.selectedPakistanCases = 'span.dot-bangladesh-scrolly'
          break;     
        case '2':
          this.selectedPakistanCases = 'span.diagnosed-scrolly-1, span.onTreatment-scrolly-1, span.finTreatment-scrolly-1, span.cured-scrolly-1'
          break;
        case '3':
          this.selectedPakistanCases = 'span.onTreatment-scrolly-1, span.finTreatment-scrolly-1, span.cured-scrolly-1'
          break;
        case '4':
          this.selectedPakistanCases = 'span.finTreatment-scrolly-1, span.cured-scrolly-1'
          break;          
        case '5':
          this.selectedPakistanCases = 'span.cured-scrolly-1'
          break;     
      }
      d3.select('.bangladesh-case-numbers-scrolly').selectAll('span.dot-bangladesh-scrolly').style('background-color', '#C4C4C4');      
      d3.select('.bangladesh-case-numbers-scrolly').selectAll(`${this.selectedPakistanCases}`).style('background-color', '#425D70');
    },    
  },
}
</script>

<style lang="scss" scoped>
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