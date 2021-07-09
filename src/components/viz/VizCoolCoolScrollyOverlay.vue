<template>
  <v-container outer class="scrolly-overlay">
    <v-row justify="space-between" align="start">  
      <v-col cols="12" class="casestudy-scrolly scrolly__sticky" >
        <svg id='coolcool-viz'></svg>
        <div id='cool-intro' class="text-block" >
          <h3 class="text--h2 mb-16 scroll-prompt text-center">The times they said cool cool</h3>
          <iframe style="margin-left: auto; margin-right: auto; display: block;" width="560" height="315" class="my-8" src="https://www.youtube.com/embed/zDcbpFimUc8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          <p class="text--body-3">
            Is it a real compliment? A coping mechanism? Something to fill the silence? Whatever it is, the cool-chain has become part of what we love about the Nine-Nine.
          </p>
        </div>
      </v-col>
      <v-col class="scrolly__content">

        <div class="step first" data-step="1">
          <div class="text-block">
            <p class="text--body-1 font-weight-bold">The first ever "Cool, cool."</p>
            <p class="text--body-3">
              Well, well, well. Turns out the first ever "Cool, cool." was said by Boyle during his attempt to retrieve the tape in the department video camera from Hitchcock. This was more of a slow serious "cool, cool" meant to mask Boyle's frantic attempt to conceal evidence of Boyle and Gina's sexcapade.
            </p>
            <img class="cool-img" src="02x03_coolcool.png" />
          </div>
        </div>

        <div class="step" data-step="2">
          <div class="text-block">
            <p class="text--body-1 font-weight-bold">No hospital!</p>
            <p class="text--body-3">
              Jake rattles off three "cool"s in sweet succession as he calmly handles Sharon's childbirth and proceeds to summon her vaginal Gandalf aka doula, which is a thing that he definitely know what it is.
            </p>
            <img class="cool-img" src="03x08_coolcoolcool.png" />             
          </div>
        </div>

        <div class="step" data-step="3">
          <div class="text-block">
            <p class="text--body-1 font-weight-bold">Who's Brett Booth?</p>
            <p class="text--body-3">
              In response to the name of Det. Brett Booth, Jake nonchalently utters, "Cool, cool, cool." But best-bud-Boyle notices that (UH-OH!) that was Jake's worried "cool, cool, cool."
            </p>
            <img class="cool-img" src="05x20_coolcoolcool.png" />  
          </div>
        </div>

        <div class="step" data-step="4">
          <div class="text-block">
            <p class="text--body-1 font-weight-bold">Cured</p>
            <p class="text--body-3">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero perspiciatis consectetur ipsa fugit itaque minima ea repellat distinctio sint soluta nisi nihil illo, culpa minus quia maxime vitae! Doloremque, voluptate.
            </p>
            <p class="text--body-3">
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Libero perspiciatis consectetur ipsa fugit itaque minima ea repellat distinctio sint soluta nisi nihil illo, culpa minus quia maxime vitae! Doloremque, voluptate.
            </p>              
          </div>
        </div>                                       
      </v-col>     
    </v-row>
  </v-container> 
</template>

<script>
import * as d3 from 'd3';
import scrollama from 'scrollama';

export default {
  name: 'VizBangladeshScrollyOverlay',
  components: {},
  data() {
    return {
      publicPath: process.env.BASE_URL,
      coolSegments: [1, 1, 2, 4, 4, 4, 4, 4, 5, 6]
    };
  },
  mounted() {
    this.initViz();
    this.initScrollama();    
  },  
  methods: {
    initViz() {
      d3.select('#coolcool-viz')
        .attr('height', 150)
        .attr('width', window.innerWidth)
        .selectAll('text')
        .data(d3.range(10)).enter()
        .append('text')
        .text('cool')
        .attr('class', d => 'cool-' + this.coolSegments[d])
        .attr('font-family', 'Anton')
        .attr('font-size', '64px')
        .attr('y', 100)
        .attr('x', 2000)
    },
    initScrollama() {
      // instantiate scrollama
      const scrollerDesktop = scrollama();

      const stepH = Math.floor(window.innerHeight * 0.7);
      d3.selectAll('.step').style("height", stepH + "px");
      // d3.selectAll('.step.first').style("height", null)

      // setup scrollama
      scrollerDesktop.setup({
        container: '.scrolly-overlay',
        graphic: '.scrolly-overlay .scrolly__sticky',
        step: '.scrolly-overlay .scrolly__content .step', // required
        offset: 0.7,
        debug: false,
        progress: true
      })
      // .onStepEnter(this.handleStepEnter)
      .onStepProgress(this.handleStepProgress)
    },
    // handleStepEnter({ element }) {
    //   console.log(element)
    // },
    handleStepProgress(response) {
      let p = Math.min(response.progress, 0.6)
      p /= 0.6
      d3.selectAll('text.cool-' + (response.index + 1))
        .attr('x', d => 2000 - 2000 * p + d * 120)
      if (response.index == 0) {
        d3.select('div#cool-intro')
          .style('opacity', 1 - p)
      }
      d3.selectAll('.step')
        .style('opacity', 0)
      d3.select(response.element)
        .style('opacity', () => {
          if (response.progress >= 0.1 && response.progress <= 0.9) return 1
          else if (response.progress < 0.1) return response.progress * (1/0.1)
          else return (1 - response.progress) * (1/0.1)
        })
        .attr('progress', response.progress)
    }
  },
}
</script>

<style lang="scss" scoped>
svg#coolcool-viz {
  //border: 1px solid red;
}

img.cool-img {
  width: 300px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.text-block {
  background-color: white;
  color: #2E2E2E;
  padding: 36px;
}

.casestudy-scrolly {
  z-index: 1000; 
}

.dot-bangladesh-scrolly {
  height: 15px;
  width: 15px;
  border-radius: 50%;
  display: inline-block;
  background-color: #425D70;
  margin-right: 10px;
}

.scrolly__overlay {
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
  //margin-top: calc(25vh);
}

.scrolly__sticky {
  justify-content: center;  
  align-items: center;
  position: sticky;
  // top: 50%;
  // transform: translate(0, -50%);
  top: calc(64px + 12px);
  z-index: 0;
  height: calc(100vh - 64px);
}

</style>