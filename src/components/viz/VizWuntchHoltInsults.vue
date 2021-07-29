<template>
  <div class="scrolly-overlay-insults">
    <v-row justify="space-between" align="start"  class="scrolly__sticky" no-gutters>  
      <v-col cols="6">
        <v-row justify="center" no-gutters>
          <v-col cols="12" lg="6">
            <img src="@/assets/holt.png" width="80%" />
            <div class=" text-left mt-6 px-6">
              <div v-show="step >= 1">
                <img v-for="(n, i) in 4" :key="i + 'holt5-1'" src="@/assets/holt5.png" class="count-stick"/>
              </div>
              <div v-show="step >= 3">
                <img v-for="(n, i) in 3" :key="i + 'holt1-3'" src="@/assets/holt1.png" class="count-stick"/>
                <img v-for="(n, i) in 1" :key="i + 'holt5-3'" src="@/assets/holt5.png" class="count-stick"/>
              </div> 
              <div v-show="step >= 4">
                <img v-for="(n, i) in 3" :key="i + 'holt5-4'" src="@/assets/holt5.png" class="count-stick"/>
              </div> 
              <div v-show="step === 5">
                <img v-for="(n, i) in 2" :key="i + 'holt1-5'" src="@/assets/holt1.png" class="count-stick"/>
                <img v-for="(n, i) in 2" :key="i + 'holt5-5'" src="@/assets/holt5.png" class="count-stick"/>

              </div>                                                   
            </div>              
          </v-col>         
        </v-row>
      </v-col>

      <v-col cols="6">
        <v-row justify="center" no-gutters>            
          <v-col cols="12" lg="6">
            <img src="@/assets/wuntch.png" width="80%" style="display: block; margin-left: auto;" />
            <div class="text-right mt-6 px-6">
              <div v-show="step >= 1">
                <img v-for="(n, i) in 3" :key="i + 'wuntch1'" src="@/assets/wuntch1.png" class="count-stick"/>
              </div>
              <div v-show="step >= 2">
                <img v-for="(n, i) in 1" :key="i + 'wuntch5'" src="@/assets/wuntch5.png" class="count-stick"/>
                <img v-for="(n, i) in 1" :key="i + 'wuntch1'" src="@/assets/wuntch1.png" class="count-stick"/>
              </div>      
              <div v-show="step >= 3">
                <img v-for="(n, i) in 1" :key="i + 'wuntch5'" src="@/assets/wuntch5.png" class="count-stick"/>
                <img v-for="(n, i) in 1" :key="i + 'wuntch1'" src="@/assets/wuntch1.png" class="count-stick"/>
              </div> 
              <div v-show="step >= 4">
                <img v-for="(n, i) in 4" :key="i + 'wuntch1'" src="@/assets/wuntch1.png" class="count-stick"/>
              </div> 
              <div v-show="step === 5">
                <img v-for="(n, i) in 3" :key="i + 'wuntch1'" src="@/assets/wuntch1.png" class="count-stick"/>
              </div>                                                   
            </div>            
          </v-col>
        </v-row>      
      </v-col>

      <v-col v-if="step === 1" cols="11" lg="6" class="wuntch-holt-insults-intro hidden-sm-and-down">
        <iframe class="youtube-iframe my-8" src="https://www.youtube.com/embed/tqf5slEsdh0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>    
      </v-col>
    </v-row>

    <div>
      <v-container class="inner scrolly__content">
          <div class="step" data-step="1">
            <div class="text-block">
              <!-- <img src="03x08_side_edit.png" width="50%" /> -->

              <p class="text--h2 font-tertiary text-center">
                Fantasy references
              </p>

              <p class="text--body-2">
                Holt gets points in our book for the creative references to fantasy characters like the wicked Witch (from Oz), the Cheuksin and Bloody Mary. The most common of these are references to the devil. 
              </p>

              <p class="text--body-2">
                "As God says when Madeline Wuntch tries to sneak past into the gates of Heaven, "It ain't happening, honey" - S07E07 - Ding Dong. 
              </p>              
            </div>
          </div>

          <div class="step" data-step="2">
            <div class="text-block">
              <!-- <img src="03x08_side_edit.png" width="50%" /> -->

              <p class="text--h2 font-tertiary text-center">
                Work-Roast
              </p>

              <p class="text--body-2">
                Wuntch definitely wins this one. Not only does she <em>verbally</em> roast Holt's career, she made Holt wear Paulie the Pigeon mascot when she "promoted" him to a desk job as the head of NYPD Public Relations (S02E22 - The Chopper). Later in the season, she even demoted Holt for a year when she became acting commissioner in S06E18 - Suicide Squad. 
              </p>
            </div>
          </div>

          <div class="step" data-step="3">
            <div class="text-block">
              <!-- <img src="05x20_side_edit.png" width="50%" /> -->

              <p class="text--h2 font-tertiary text-center">
                Describing appearances
              </p>

              <p class="text--body-2">
                We'd say they are both pretty tied for these ones. The most common taunt on physical traits would be about each other's age. With that, comes wrinkly skin "like a raisin" and dying of old age.              
              </p>
            </div>
          </div>

          <div class="step" data-step="4">
            <div class="text-block">
              <!-- <img src="03x08_side_edit.png" width="50%" /> -->

              <p class="text--h2 font-tertiary text-center">
                Animals
              </p>

              <p class="text--body-2">
                HOLT GETS CREATIVE WITH THIS ONE AGAIN. <br> Insect? Yes, we have mold beetles. <br>Mammals? There's Madeline's rat hands. <br>Fish? <em>"Don't count your gross fish babies before they've hatched, Madeline."</em> <br>Reptile? Crocodile. 
              </p>

              <p class="text--body-2">
                Hotel? Trivago.
              </p>              
            </div>
          </div>

          <div class="step" data-step="5">
            <div class="text-block">
              <!-- <img src="03x08_side_edit.png" width="50%" /> -->

              <p class="text--h2 font-tertiary text-center">
                All the others
              </p>

              <p class="text--body-2">
                These are others that don't make it to any of the categories but are still in the dataset. Some are like the punch lines that Holt painstakingly took the entire night to come up with -- <em>"It's Wuntch-time"</em> or <em>"Wuntch meat"</em>. 
              </p>

              <p class="text--body-2">
                Or when Holt fired back <em>"Describing your breakfast"</em> to Wuntch's <em>"Sticks and stones, Raymond"</em>.
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
      count: [
        { id: '1', type: 'fantasy', holt1: 0, holt5: 4, wuntch1: 3, wuntch5: 0 },
        { id: '2', type: 'work', holt1: 0, holt5: 0, wuntch: 1, wuntch5: 1 },
        { id: '3', type: 'physical', holt1: 3, holt5: 1, wuntch: 1, wuntch5: 1 },
        { id: '4', type: 'animal', holt1: 0, holt5: 3, wuntch: 4, wuntch5: 0 },
        { id: '5', type: 'others', holt1: 2, holt5: 2, wuntch: 3, wuntch5: 0 },
      ], 
      step: 0,
    };
  },
  mounted() {
    // this.initViz();
    this.initScrollama();    
  },  
  methods: {
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
        offset: 0.7,
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
  min-width: 235px;
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    width: 80%;
    padding: 12px;
  }       

  img {
    display: block;
    margin: 0 auto;
  }
}

.scrolly__content {
  position: relative;
  padding: 0 1rem;
  width: 100%;
  z-index: 1;
}

.step {
  margin: 0 auto 2rem auto;
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
  top: -25%;
  left: 50%;
  transform: translate(-50%, -50%);
  
  iframe {
    display: block;
    margin: 0 auto;
  }
}

.highlight-holt {
  background-color: #FFF600;
  color: #2e2e2e
}

.highlight-wuntch {
  background-color: #4336A7;
  color: white;
}

.youtube-iframe {
  width: 535px;
  height: 315px;
  display: block;
  margin: 0 auto;  
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    width: 100%;
  }      
}

.count-stick {
  height: 50px;
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    height: 35px;
  }      
}
</style>