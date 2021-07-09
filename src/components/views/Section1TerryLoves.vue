<template>
  <section class="section_wrapper py-12">
    <v-container class="inner py-12">
      <h3 class="text--h2 mb-16 scroll-prompt text-center">Everything that Terry has ever loved/hated</h3>

      <v-row align="center" justify="center" no-gutters class="py-6">
        <v-col cols="12" md="9" xl="10">
          <p class="text--body-1 mb-4">
            Yeah, yeah, yeah. Everyone knows Terry loves yogurt. But here's other stuff that Terry loves - and hates - as well in case you forget!
          </p>

          <iframe width="560" height="315" class="my-8" src="https://www.youtube.com/embed/11JlyeigI30" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>          
        </v-col>
      </v-row>
    </v-container>
                
    <v-container> 
      <v-row align="start" justify="center" no-gutters>
        <v-col cols="3" offset="2">
          <h3 class="text--h2 text--header mb-12 text-right mr-4">TERRY LOVES</h3>
        </v-col>
        <v-col cols="6">
          <p class="text--h2 text-left">
          <span id="loves">love</span>
          </p>
        </v-col>
      </v-row>           
      <v-row align="start" justify="space-between" no-gutters class="py-6">
        <v-col cols="12" md="6">
          <div v-for="(n, i) in items" :key="i" class="mr-8 pb-12 terry-emoji" @click="handleInteractivity(n, $event)">
            {{ n.emoji }}
          </div> 
        </v-col>

        <v-col cols="12" md="6">
          <div class="terry-card text-left">
            <p class="text--body-2">Click on the emoji to see what Terry had loved/hated on B99!</p>          
              <div class="details pa-4">
                <h3 class="text--h2 text--header mb-12">{{ selectedItem.emotion === 'loves' ?  '❤️' : '💔' }} {{ selectedItem.thing }}</h3>
                <p class="mb-3 text--body-1">
                  <span class="text-subtitle">Episode: </span>{{ selectedItem.episode }}
                </p>

                <p class="mb-3 text--body-1">
                  <em>{{ selectedItem.prevLine }}<br></em> 
                  {{ selectedItem.line }}<br>
                  <em>{{ selectedItem.nextLine }}</em>
                </p>

                <p class="label text--body-1 text-right mb-0"> {{ selectedItem.emoji }} </p>  
              </div>                  
          </div>
        </v-col>        
      </v-row>      
      <!-- <div class="love-wrapper pa-4">
        <div class="text-center">
          <v-row align="start" justify="center" style="height: 120px;" no-gutters>
            <v-col cols="4">
              <h3 class="text--header mb-12">TERRY ❤️</h3>
            </v-col>
            <v-col cols="6">
              <p class="text--h2 text--header">
              <span id="loves">love</span>
              </p>
            </v-col>
          </v-row>
        </div>  

        <div v-for="(n, i) in items" :key="i" class="mr-8 pb-12 terry-emoji">
          {{ n.emoji }}
        </div>
      </div>         -->
    </v-container>
  </section>
</template>

<script>
import * as d3 from 'd3';

export default {
  name: 'Section1TerryLoves',
  data() {
    return {
      uniqueItems: [], 
      items: [],
      selectedItem: {
        nextLine: '',
        prevLine: '',
        episode: '',
        line: '',
        emoji: '',
        emotion: '',
        thing: ''
      }
    };
  },
  async mounted() {
    const data = await d3.csv('/data/terry-lav.csv');
    this.parseData(data);
    this.iterateWords();

    this.$nextTick(() => {
      d3.select('div.terry-emoji').classed('selectedEmoji', true);
    })
  },
  methods: {
    parseData(data) {
      this.items = data;

      let terryLoves = data.filter(item => item.emotion === "loves");
      terryLoves = terryLoves.map(d => d.thing)

      this.uniqueLoves = [];
      terryLoves.forEach(d => {
        if (!this.uniqueLoves.includes(d)) {
          this.uniqueLoves.push(d);
        }
      });    

      this.selectedItem = this.items[0];
    },
    iterateWords() {
      setInterval(() => {
        const items = this.uniqueLoves;
        let title = document.getElementById('loves')
        for (let i=0; i < items.length; i++) {
          if (title.innerHTML == items[i]) {
            if (i == items.length - 1) {
              title.innerHTML = items[0]
            } else {
              title.innerHTML = items[i+1]
            }
            break
          }
        }
      }, 750)      
    },
    handleInteractivity(n, $event) {
      d3.selectAll('div.terry-emoji').classed('selectedEmoji', false);
      const emoji = $event.target; 
      d3.select(emoji).classed('selectedEmoji', true);
      this.selectedItem = n;
    }
  }
}
</script>

<style lang="scss" scoped>
.section_wrapper {
  background-color: #FFFFFF;
  //height: calc(100vh - 64px);
}

div .v-input {
  width: 300px;
  display: inline-block;
  margin-left: 10px;
}

div .v-input >>> .v-input__slot{
  background-color: #ffd4c2;
  border-radius: 100px;
}

::v-deep .v-input__slot {
  box-shadow: none !important;
  margin-bottom: 0;
}

::v-deep .v-select__selection {
  font-size: 20px;
}


#loves {
  font-weight: 500;
  border-bottom: 4px solid black;
  text-decoration: none;
  word-break: break-word;
}

.terry-emoji {
  display: inline-block;
  font-size: 1.5rem;
  cursor: pointer;
}

.selectedEmoji {
  position: relative;
}

.selectedEmoji:after {
  content: '';
  position: absolute;
  top: calc(100% - 48px);
  left: 50%;
  width: 120%;
  border-bottom: 4px solid #2e2e2e;
  transform: translate(-50%);
}

.scroll-prompt {
  position: relative;
}

.scroll-prompt:after {
  content: '❤️';
  position: absolute;
  top: calc(100% + 8px);
  bottom: -48px;
  left: 50%;
  border-top: 4px solid #2e2e2e;
  transform: translate(-50%);
}

.terry-card {
  width: 85%;
  display: block; 
  margin: 0 auto;

  .details {
    border-left: 2px solid #2e2e2e;
    position: relative;  

    .label {
      display: inline-block;
      position: absolute;
      bottom: 0px;
      right: 16px;
    }    
  }
}

.text-subtitle {
  font-size: 18px;
  font-weight: 400;
  line-height: 28px;
  font-family: 'Anton', sans-serif;
  // color: #2e2e2e;  
  letter-spacing: 2px;
  text-transform: uppercase;  
}
</style>