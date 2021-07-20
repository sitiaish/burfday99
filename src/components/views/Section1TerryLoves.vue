<template>
  <section class="section_wrapper py-12">
    <v-container class="py-12">
      <v-row align="center" justify="center">
        <v-col cols="8" md="4">
          <div
            data-aos="slide-right"
            data-aos-ease = "ease"
            data-aos-duration="1000"
            data-aos-delay="100">
            <img v-if="count % 2 === 1" src="@/assets/terry-yogurt.png" width="100%" />
            <img v-if="count % 2 === 0" src="@/assets/terry-yogurt-2.png" width="100%" />            
          </div>
        </v-col>
        <v-col cols="12" md="8">
          <div>
            <h3 class="text--header mb-2 mr-4 text-center text-lg-left">TERRY LOVES</h3>
          </div>
          <div class="iterate-wrapper">
            <p class="text--h1 text-center text-lg-left">
            <span id="loves">love</span>
          </p>
          </div>
        </v-col>             
      </v-row>
    </v-container>

    <v-container class="inner py-12">
      <v-row justify="center">
        <v-col cols="12" md="12">
          <h3 class="text--h2 mb-16 scroll-prompt text-center">
            Everything that Terry has ever loved/hated
          </h3>

          <div class="pt-12">
            <p class="text--body-1">            
              The running gag with Terry is that he refers to himself in the third person -- "You made Terry get real with himself and his genitals. [S0202 - Chocolate Milk]". And that he loves yogurt. I wanted to see what else Terry loves besides yogurt. We went ahead to find instances in B99 with "Terry love". We expanded this to include "Terry like". 
            </p>

            <p class="text--body-1">            
              If love wasn't enough, we found stuff that Terry Jeffords hated. Special mention to bugs because Terry, despite his bulky frame and all those 👅 muscles, is just a mere mortal like us. Hand me that Baygon!
            </p>
          </div>
        </v-col>        
      </v-row>
    </v-container>    
                
    <v-container>     
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
                <h3 class="text--h2 text--header mb-12">{{ ['loves', 'likes', 'loved'].some(d => selectedItem.emotion === d) ?  '❤️' : '💔' }} {{ selectedItem.thing }}</h3>
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
    </v-container>

    <v-container class="inner py-12">
      <v-row justify="center">
        <v-col cols="12" md="12">
          <div class="pt-12">
            <p class="text--body-1">            
              Of course, searching by string like we did couldn't possibly cover all the things Terry loves and hate. I caught that when <em>"Terry loves yogurt"</em> strings only came up three times across the B99 files. And we know, <em>for a fact</em> that Terry loves his yogurt. So what gives? 
            </p>

            <p class="text--body-1">            
              I guess it's more of how important yogurt is to Terrence that makes us remmember Terry loves yogurt and maybe less so of the number of times the line is spoken. Like even Captain Holt knows Terry loves his yogurt when the gag first started in S01E02 - The Tagger. 
            </p>
          </div>
        </v-col>        
      </v-row>
    </v-container>    

    <div class="tall-container" id="tall">
      <div class="sticky" id="refd">
        <div class="horizontal-container" id="horizontal" :style="{transform: `translateX(${translate}px)`}">
          <div class="card-container">
            <div class="sample-card pa-6 pa-xl-8">
              <img src="@/assets/yogurt-1.png" width="100%" />
              <div class="my-8">
                <p class="text--h3 font-tertiary">
                  S01E02 - The Tagger
                </p>
                <p class="text--body-2">
                  First mention of "Terry loves yogurt" when a police report was fished from Terry's trash with stains of yogurt.
                </p>
              </div>            
            </div>
            <div class="sample-card pa-6 pa-xl-8">
              <div class="mb-8">
                <p class="text--h3 font-tertiary">
                  S01E014 - The Ebony Falcon
                </p>
                <p class="text--body-2">
                  A personal favourite! Terry describes himself as <em> the ebony falcon</em>: monogamous and too tired for sex, so his only indulgence is fresh fruit yogurt parfaits. Jake echoes with "Terry loves yogurt".
                </p>
              </div>                
              <img src="@/assets/yogurt-2.png" width="100%" />                        
            </div>
            <div class="sample-card pa-6 pa-xl-8">
              <img src="@/assets/yogurt-password.png" width="100%" />
              <div class="my-8">
                <p class="text--h3 font-tertiary">
                  S02E13 - Payback
                </p>
                <p class="text--body-2">
                  The team tries to hack into Terry's email, only to be stumped by password. Surprise, surprise -- the password, as guessed by Boyle, is "yogurt".
                </p>
              </div>                             
            </div>
            <div class="sample-card pa-6 pa-xl-8">
              <div class="mb-8">
                <p class="text--h3 font-tertiary">
                  S03E02 - The Funeral
                </p>
                <p class="text--body-2">
                  Did you hear? Terry's favourite mango yogurt got discontinued! I love how he ranks this together with Sharon's bedrest and his kids thinking their preschool teacher a "stupidface". Yep they all stink Terry.
                </p>
              </div>                    
              <img src="@/assets/mango-yogurt.png" width="100%" />             
            </div>     
            <div class="sample-card pa-6 pa-xl-8">
              <img src="@/assets/yogurt-fridge.png" width="100%" />
              <div class="my-8">
                <p class="text--h3 font-tertiary">
                  S04E02 - Coral Palms Pt.2
                </p>
                <p class="text--body-2">
                  "Enjoy your blood yogurt" Terry caves under the chill-dude Captain Stentley and got a personal yogurt fridge at his desk. Which he eventually returns to save Jake and Holt at Coral Palms.
                </p>
              </div>                    
            </div>                                                         
          </div>
        </div>
      </div>
    </div>    

   
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
      },
      translate: 0,
      count: 0,
    };
  },
  async mounted() {
    const data = await d3.csv('/data/terry-lav.csv');
    this.parseData(data);
    this.iterateWords();

    this.$nextTick(() => {
      d3.select('div.terry-emoji').classed('selectedEmoji', true);
    });

    this.calcDynamicHeight();
    this.addScrollOffset();    
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
          this.count = i;
          if (title.innerHTML == items[i]) {
            if (i == items.length - 1) {
              title.innerHTML = items[0]
            } else {
              title.innerHTML = items[i+1]
            }
            break
          }
        }
      }, 600)      
    },
    handleInteractivity(n, $event) {
      d3.selectAll('div.terry-emoji').classed('selectedEmoji', false);
      const emoji = $event.target; 
      d3.select(emoji).classed('selectedEmoji', true);
      this.selectedItem = n;
    },
    calcDynamicHeight() {
      const vw = window.innerWidth;
      const vh = window.innerHeight;   
      const objectWidth = document.getElementById('horizontal').scrollWidth
      document.getElementById("tall").style.height = objectWidth - vw + vh  + 'px';
    },
    addScrollOffset() {
      window.addEventListener("scroll", () => {
        const offsetTop = document.getElementById("refd").offsetTop;
        const offsetParent = document.getElementById("tall").offsetTop; 
        this.translate = (offsetParent - offsetTop);
      });      
    }    
  }
}
</script>

<style lang="scss" scoped>
.section_wrapper {
  background-color: #FFFFFF;
  //height: calc(100vh - 64px);
}

#loves {
  font-weight: 500;
  border-bottom: 4px solid black;
  text-decoration: none;
  word-break: break-word;
  background-color: #fff534 !important;
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
  letter-spacing: 2px;
  text-transform: uppercase;  
}

.sticky {
  position: sticky;
  top: 40px;
  height: calc(100vh - 80px);
  width: 100%;
  overflow-x: hidden;
}

.horizontal-container {
  position: absolute;
  height: 100%;
  will-change: transform;
}

.card-container {
  position: relative;
  height: 100%;
  margin: 0 0 0 60px;
  display: flex;
  flex-flow: row nowrap;
  justify-content: flex-start;
  align-items: center;
  background-color: #002f88;
}

.sample-card {
  position: relative;
  height: 80%;
  width: 500px;
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    width: 300px;
    height: 70%;    
  }  
  background-color: yellow;
  margin-right: 75px;
  flex-shrink: 0;
}

.sample-card:first-child {
  margin-left: 75px;
}

.iterate-wrapper {
  height: 150px;
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    height: 180px;
  }  
}
</style>