  <template>
    <v-container inner class="container--inner">
      <v-row justify="center" align="center">  
        <v-col cols="12" md="12">
          <div>
          <p class="text--body-1 text-center mb-0">
            Click around to explore the data
          </p>
          <p class="text--caption text-center mb-6">
            Each circle represents 10 cases.
          </p>
          <p class="text--caption text-center mb-6">
            Each circle represents 25 cases. [mobile]
          </p>          
          </div>         
      
          <div class="casestudy-numbers-bangladesh mb-md-6 mb-0 text-md-center" >
            <v-btn :ripple="false" :elevation='0' class="mr-4 mb-4 active-selection screened" @click="selectData('screened')">Screened</v-btn>
            <v-btn :ripple="false" :elevation='0' class="mr-4 mb-4 diagnosed" @click="selectData('diagnosed')">Diagnosed</v-btn>
            <v-btn :ripple="false" :elevation='0' class="mr-4 mb-4 onTreatment" @click="selectData('onTreatment')">Put on treatment</v-btn>
            <v-btn :ripple="false" :elevation='0' class="mr-4 mb-4 completedTreatment" @click="selectData('completedTreatment')">Completed treatment</v-btn>            
            <v-btn :ripple="false" :elevation='0' class="cured mb-4" @click="selectData('cured')">Cured</v-btn>
          </div>
        </v-col>

        <v-col cols="12" md="10">        
          <div class="bangladesh-case-numbers-viz" v-if="!$vuetify.breakpoint.mobile">                            
            <span v-for="(n, i) in data.cured" :key="i + '-cured-viz'" class="dot-pviz cured mr-2" /> 
            <span v-for="(n, i) in data.finTreatment" :key="i + '-finTreatment-viz'" class="dot-pviz finTreatment" /> 
            <span v-for="(n, i) in data.onTreatment" :key="i + '-onTreatment-viz'" class="dot-pviz onTreatment" /> 
            <span v-for="(n, i) in data.diagnosed" :key="i + '-diagnosed-viz'" class="dot-pviz diagnosed"/> 
            <span v-for="(n, i) in data.undiagnosed" :key="i + '-undiagnosed-viz'" class="dot-pviz undiagnosed"/> 
          </div>

          <div class="bangladesh-case-numbers-viz" v-if="$vuetify.breakpoint.mobile">                            
            <span v-for="(n, i) in dataMobile.cured" :key="i + '-cured-viz'" class="dot-pviz cured mr-2" /> 
            <span v-for="(n, i) in dataMobile.finTreatment" :key="i + '-finTreatment-viz'" class="dot-pviz finTreatment" /> 
            <span v-for="(n, i) in dataMobile.onTreatment" :key="i + '-onTreatment-viz'" class="dot-pviz onTreatment" /> 
            <span v-for="(n, i) in dataMobile.diagnosed" :key="i + '-diagnosed-viz'" class="dot-pviz diagnosed"/> 
            <span v-for="(n, i) in dataMobile.undiagnosed" :key="i + '-undiagnosed-viz'" class="dot-pviz undiagnosed"/> 
          </div>          
        </v-col>
      </v-row>
    </v-container>      
</template>

<script>
import * as d3 from 'd3';
export default {
  name: 'VizBangladeshNumbers',
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
        selected: '',
      },
      dataMobile: {
        screened: 252, 
        undiagnosed: 104,
        diagnosed: 64,
        onTreatment: 48,
        finTreatment: 29,
        cured: 9,
        selected: '',
      }      
    };
  },
  methods: {
    selectData(data) {
      const bangladeshButtons = d3.select('.casestudy-numbers-bangladesh');
      bangladeshButtons.selectAll('.v-btn')
        .classed('active-selection', false);

      bangladeshButtons.select(`.v-btn.${data}`)
        .classed('active-selection', true);

      switch (data) {
        case 'diagnosed':
          this.selected = 'span.diagnosed, span.onTreatment, span.finTreatment, span.cured'
          break;

        case 'onTreatment':
          this.selected = 'span.onTreatment, span.finTreatment, span.cured'
          break;
          
        case 'completedTreatment':
          this.selected = 'span.finTreatment, span.cured'
          break;

        case 'cured':
          this.selected = 'span.cured'
          break;     

        case 'screened':
          this.selected = 'span.dot-pviz'
          break;                   
      }

      d3.selectAll('.bangladesh-case-numbers-viz span.dot-pviz').style('background-color', '#C4C4C4');      
      d3.selectAll(`.bangladesh-case-numbers-viz ${this.selected}`).style('background-color', '#425D70');
    }
  },
}
</script>

<style lang="scss" scoped>
.casestudy-numbers-bangladesh {
  .v-btn.theme--light {
    padding: 4px 20px;
    border-radius: unset;
    border: 1px solid #2E2E2E;
    background-color: transparent;
  }

  .v-btn.theme--light.active-selection {
    background-color: #425D70;
    color: #FAFAFA;
  }
}


.dot-pviz {
  height: 12px;
  width: 12px;
  border-radius: 50%;
  display: inline-block;
  background-color: #425D70;
  margin-right: 8px;
}
</style>