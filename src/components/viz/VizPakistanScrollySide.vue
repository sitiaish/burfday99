<template>
  <v-container outer class="container--fluid scrolly-side">
    <v-row justify="space-between" align="start">  
      <v-col cols="12" md="4" class="scrolly__content">

        <div class="step first" data-step="1">
          <div class="text-block">
            <p class="text--body-1 font-weight-bold">Screened</p>
            <p class="text--body-3">
              In Pakistan, where the number of people infected with HCV is second only to the world’s highest - Egypt - Machar is just a small part of the country’s struggle with the plague of hepatitis C. 
            </p>           
          </div>
        </div>

        <div class="step first" data-step="2">
          <div class="text-block">
            <p class="text--body-1 font-weight-bold">Enrolled</p>
            <p class="text--body-3">
              At the Médecins Sans Frontières (MSF) clinic, which opened in Machar Colony in early 2015, patients come from high risk occupational groups that use sharp equipment or are exposed to bodily fluids. These include barbers, dentists, health practitioners, fishermen, beauticians, hijamas (cupping practitioners), truck drivers, traditional birth attendants, shrimp factory labourers and child scavengers. 
            </p>       
          </div>
        </div>


        <div class="step first" data-step="2">
          <div class="text-block">
            <p class="text--body-3">
              Age segregation legend (by colour): Most of those who get diagnosed at MSF’s clinic are adults around the 40-year age group. This is because HCV takes many years to damage the liver and exhibit symptoms. 
            </p>       
          </div>
        </div>        

        <div class="step first" data-step="3">
          <div class="text-block">
            <p class="text--body-1 font-weight-bold">Put on treatment</p>
            <p class="text--body-3">
              Contaminated blood transfusions and the reuse of dirty syringes and medical instruments are the leading causes of Pakistan’s high infection rate. Where resources are limited, health workers sometimes reuse needles on multiple patients during procedures. In very deprived areas such as Machar, poor infrastructure and the lack of hygiene and proper healthcare services have allowed HCV to take root, making an already vulnerable community more at risk of falling to deadly disease.  
            </p>           
          </div>
        </div>

        <div class="step first" data-step="4">
          <div class="text-block">
            <p class="text--body-1 font-weight-bold">Completed Treatment</p>
            <p class="text--body-3">
              HCV treatment is often centralised in hospitals, rather than at local health centres. This often puts a strain on a HCV-infected person, as treatment involves multiple medical check-ups. Many patients cannot afford to take time off work and compromise their daily wages to make the long journey to the hospital. MSF provides diagnosis, treatment, health education and patient support services for HCV under one roof for anyone seeking medical help for the first time. This lessens the burden of the many who struggle to get diagnosed and treated due to the high costs of accessing treatment. 
            </p>            
          </div>
        </div>                                       
      </v-col>

      <v-col cols="12" md="2" class="casestudy-scrolly scrolly__sticky">
        <div>
          <p class="text--body-2 pakistan-step-1 pakistan-tab">Screened</p>
        </div>

        <div>
          <p class="text--body-2 pakistan-step-2 pakistan-tab">Enrolled</p>
        </div>

        <div>
          <p class="text--body-2 pakistan-step-3 pakistan-tab">Put on treatment</p>
        </div>

        <div>
          <p class="text--body-2 pakistan-step-4 pakistan-tab">Completed treament</p>
        </div>                              
      </v-col>        

      <v-col cols="12" md="6" class="scrolly__sticky">
        <div class="pakistan-case-numbers-scrolly">                             
          <span v-for="(n, i) in data.screened" :key="i + '-total'" class="dot-pakistan-scrolly"/> 

          <span v-for="(n, i) in data.enrolledYouth" :key="i + '-total'" class="dot-pakistan-scrolly"/> 
          <span v-for="(n, i) in data.enrollledAdult" :key="i + '-total'" class="dot-pakistan-scrolly"/> 
          <span v-for="(n, i) in data.enrollledMiddleAge" :key="i + '-total'" class="dot-pakistan-scrolly"/> 
          <span v-for="(n, i) in data.enrollledOld" :key="i + '-total'" class="dot-pakistan-scrolly"/> 

          

        </div>
      </v-col> 
    </v-row>
  </v-container> 
</template>

<script>
import * as d3 from 'd3';
import scrollama from 'scrollama';

export default {
  name: 'VizPakistanScrolly',
  components: {},
  data() {
    return {
      publicPath: process.env.BASE_URL,
      data: {
        screened: 626, 
        enrolledYouth: 5,
        enrollledAdult: 71,
        enrollledMiddleAge: 56,
        enrollledOld: 8,
        onTreatment: 97,
        finTreatment: 70,
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
      d3.selectAll('p.pakistan-tab').classed('active-selection', false)
      d3.select(`p.pakistan-step-${step}`).classed('active-selection', true);

      // change the dots
      switch (step) {
        case '1':
          this.selectedPakistanCases = 'span.dot-pakistan-scrolly'
          break;     
        case '2':
          this.selectedPakistanCases = 'span.diagnosed-scrolly-1, span.onTreatment-scrolly-1, span.finTreatment-scrolly-1, span.cured-scrolly-1'
          break;
        case '3':
          this.selectedPakistanCases = 'span.onTreatment-scrolly-1, span.finTreatment-scrolly-1, span.cured-scrolly-1'
          break;
        case '4':
          this.selectedPakistanCases = 'span.cured-scrolly-1'
          break;     
      }
      d3.selectAll('span.dot-pakistan-scrolly').style('background-color', '#C4C4C4');      
      d3.selectAll(`${this.selectedPakistanCases}`).style('background-color', '#425D70');
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

.dot-pakistan-scrolly {
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
  // top: 50%;
  // transform: translate(0, -50%);
  top: calc(64px + 64px);
  z-index: 1;
  height: calc(100vh - 64px - 64px);
}

</style>