<template>
  <div class="scrolly-overlay-insults">
    <v-row justify="space-between" align="start"  class="scrolly__sticky">  
      <v-col cols="6">
        <v-row justify="space-between">
          <v-col cols="6">
            <img src="@/assets/holt.png" width="100%" />
          </v-col>

          <v-col cols="6">
            <div>
              <p class="text--h2">
                sticks and stones
              </p>              
            </div>
          </v-col>          
        </v-row>
      </v-col>

      <v-col cols="6">
        <v-row justify="space-between">
          <v-col cols="6">
            <div>
              <p class="text--h2">
                how creative are these insults? 
              </p>              
            </div>
          </v-col>             
          <v-col cols="6" offset="6">
            <img src="@/assets/wuntch.png" width="100%" />
          </v-col>
        </v-row>      
      </v-col>

      <v-col cols="6" class="wuntch-holt-insults-intro" >
        <p class="text--header text-center" style="opacity: 0.2">
          sticks and stones, <br>
          raymond
        </p>
        {{ step }}
      </v-col>
    </v-row>

<!-- style="border: 2px solid red;" -->
    <div >
      <v-container class="inner scrolly__content">
          <div class="step" data-step="1">
            <div class="text-block">
              <img src="03x08_side_edit.png" width="50%" />

              <p class="text--h2 font-tertiary text-center">
                Character references
              </p>

              <p class="text--body-2">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro impedit tempore molestiae sunt repellat voluptatem voluptatum eligendi sequi officiis, natus ducimus harum repudiandae, vitae possimus nihil eius omnis nesciunt odio?
              </p>
            </div>
          </div>

          <div class="step" data-step="2">
            <div class="text-block">
              <img src="03x08_side_edit.png" width="50%" />

              <p class="text--h2 font-tertiary text-center">
                Work-Roast
              </p>

              <p class="text--body-2">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro impedit tempore molestiae sunt repellat voluptatem voluptatum eligendi sequi officiis, natus ducimus harum repudiandae, vitae possimus nihil eius omnis nesciunt odio?
              </p>
            </div>
          </div>

          <div class="step" data-step="3">
            <div class="text-block">
              <img src="05x20_side_edit.png" width="50%" />

              <p class="text--h2 font-tertiary text-center">
                Describing appearances
              </p>

              <p class="text--body-2">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro impedit tempore molestiae sunt repellat voluptatem voluptatum eligendi sequi officiis, natus ducimus harum repudiandae, vitae possimus nihil eius omnis nesciunt odio?
              </p>
            </div>
          </div>

          <div class="step" data-step="4">
            <div class="text-block">
              <img src="03x08_side_edit.png" width="50%" />

              <p class="text--h2 font-tertiary text-center">
                Animals
              </p>

              <p class="text--body-2">
                Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro impedit tempore molestiae sunt repellat voluptatem voluptatum eligendi sequi officiis, natus ducimus harum repudiandae, vitae possimus nihil eius omnis nesciunt odio?
              </p>
            </div>
          </div>

          <div class="step" data-step="5">
            <div class="text-block">
              <img src="03x08_side_edit.png" width="50%" />

              <p class="text--h2 font-tertiary text-center">
                just go with it
              </p>

              <p class="text--body-2">
                These are others that don't make it to any of the categories but are still in the dataset. Some are like the punch lines that Holt painstakingly took the entire night to come up with -- <span class="font-tertiary text--body-3 highlight-holt">"It's Wuntch-time"</span> or <span class="font-tertiary text--body-3 highlight-holt">"Wuntch meat"</span>. 
              </p>

              <p class="text--body-2">
                Or when Holt fired back <span class="font-tertiary text--body-3 highlight-holt">"Describing your breakfast"</span> to Wuntch's <span class="font-tertiary text--body-3  highlight-wuntch">"Sticks and stones, Raymond"</span>.
              </p>              
            </div>
          </div>
      </v-container>
    </div>
  </div> 
</template>

<script>
import * as d3 from 'd3';
import scrollama from 'scrollama';

export default {
  name: 'VizWuntchHoltInsults',
  data() {
    return {
      coolSegments: [1, 1, 2, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6], 
      step: 0,
    };
  },
  mounted() {
    // this.initViz();
    this.initScrollama();    
  },  
  methods: {
    initViz() {
      d3.select('#coolcool-viz')
        .attr('height', 150)
        .attr('width', window.innerWidth)
        .selectAll('text')
        .data(d3.range(15)).enter()
        .append('text')
        .text('cool')
        .attr('class', d => 'cool cool-' + this.coolSegments[d])
        .attr('font-family', 'Anton')
        .attr('font-size', '64px')
        .attr('y', 100)
        .attr('x', 2000)
    },
    initScrollama() {
      // instantiate scrollama
      const scrollerDesktop1 = scrollama();

      const stepH = Math.floor(window.innerHeight * 0.8);
      d3.selectAll('.step').style("height", stepH + "px");

      // setup scrollama
      scrollerDesktop1.setup({
        container: '.scrolly-overlay-insults',
        graphic: '.scrolly-overlay-insults .scrolly__sticky',
        step: '.scrolly-overlay-insults .scrolly__content .step', // required
        offset: 0.2,
        debug: false,
      })
      .onStepEnter(this.handleStepEnter)
    },
    handleStepEnter({ element }) {
      const step = d3.select(element).attr('data-step');
      this.step = +step;
    },    
  },
}
</script>

<style lang="scss" scoped>

.scrolly-overlay {
  max-width: 100%;
}

img.cool-img {
  width: 300px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.scroll-prompt {
  position: relative;
}

.scroll-prompt:after {
  content: '😎';
  position: absolute;
  top: calc(100% + 8px);
  bottom: -48px;
  left: 50%;
  border-top: 4px solid #2e2e2e;
  transform: translate(-50%);
}

.text-block {
  background-color: white;
  color: #2E2E2E;
  padding: 24px;
  width: 80%;
  min-width: 250px;

  img {
    display: block;
    margin: 0 auto;
  }
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

.scrolly__sticky {
  justify-content: center;  
  align-items: center;
  position: sticky;
  top: calc(64px + 12px);
  z-index: 0;
  height: calc(100vh - 64px);
}

.wuntch-holt-insults-intro {
  position: relative;
  top: -50%;
  left: 50%;
  transform: translate(-50%, -50%);
  // border: 2px solid red;
}

.highlight-holt {
  background-color: #FFF600;
  color: #2e2e2e
}

.highlight-wuntch {
  background-color: #4336A7;
  color: white;
}
</style>