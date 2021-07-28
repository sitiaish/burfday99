<template>
  <v-container class="cool-scrolly-overlay">
    <v-row justify="space-between" align="start">  
      <v-col cols="12" class="cool-casestudy-scrolly cool-scrolly__sticky" >
        <!-- <svg id='coolcool-viz'></svg> -->
        <p class="text--header" v-for="(s, i) in coolSegments" :key="i" :class="['cool', `cool-${s}`]" style="display: inline-block;">cool</p>
        <div id='cool-intro' class="text-block" >
          <h3 class="text--h2 mb-16 scroll-prompt text-center">The times they said cool cool</h3>
          <iframe style="margin-left: auto; margin-right: auto; display: block;" width="560" height="315" class="my-8" src="https://www.youtube.com/embed/zDcbpFimUc8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
          <p class="text--body-2">
            Is it a real compliment? A coping mechanism? Something to fill the silence? Whatever it is, the cool-chain has become part of what we love about the Nine-Nine. No doubt, no doubt.
          </p>
        </div>
      </v-col>
      <v-col class="cool-scrolly__content">

        <div class="cool-step first" data-step="1">
          <img src="02x03_side_edit.png" width="50%" style="margin-left: -10%;" />
          <div class="text-block">
            <p class="text--body-1 font-weight-bold">2 Cools: S02E03 - The Jimmy Jab Games</p>
            <p class="text--body-2">
              Well, well, well. Turns out the first ever "Cool, cool." was said by Boyle during his attempt to retrieve the tape in the department video camera from Hitchcock. This was more of a slow serious "cool, cool" meant to mask Boyle's frantic attempt to conceal evidence of Boyle and Gina's sexcapade.
            </p>
            <img class="cool-img" src="02x03_coolcool.png" />
          </div>
        </div>

        <div class="cool-step" data-step="2">
          <img src="03x08_side_edit.png" width="50%" style="margin-left: -10%;" />
          <div class="text-block">
            <p class="text--body-1 font-weight-bold">3 Cools: S03E08 - Ava</p>
            <p class="text--body-2">
              Jake rattles off three "cool"s in sweet succession as he calmly handles Sharon's childbirth and proceeds to summon her vaginal Gandalf aka doula, which is a thing that he definitely know what it is.
            </p>
            <img class="cool-img" src="03x08_coolcoolcool.png" />             
          </div>
        </div>

        <div class="cool-step" data-step="3">
          <img src="05x20_side_edit.png" width="50%" />
          <div class="text-block">
            <p class="text--body-1 font-weight-bold">3 Cools (worried ver.): S05E20 - Show Me Going</p>
            <p class="text--body-2">
              In response to the name of Det. Brett Booth, Jake nonchalently utters, "Cool, cool, cool." But best-bud-Boyle notices that (UH-OH!) that was Jake's worried "cool, cool, cool."
            </p>
            <img class="cool-img" src="05x20_coolcoolcool.png" />
          </div>
        </div>

        <div class="cool-step" data-step="4">
          <img src="02x10_side_edit.png" width="40%" style="margin-right: -30%;" />
          <div class="text-block">
            <p class="text--body-1 font-weight-bold">7 Cools: S02E10 - The Pontiac Bandit Returns</p>
            <p class="text--body-2">
              Some might call this the first official cool-cool-cool, as Jake goes undercover with Rosa and a string of seven "cool"s camouflages his nervousness in the presence of Tito Ruiz.
            </p>
            <img class="cool-img" src="02x10_coolcool.png" />
          </div>
        </div>

        <div class="cool-step" data-step="5">
          <img src="06x12_side2_edit.png" width="50%" style="margin-right: -10%;" />
          <div class="text-block">
            <p class="text--body-1 font-weight-bold">10 Cools: S06E12 - Casecation</p>
            <p class="text--body-2"><em>"I don't know that I totally know that I for sure want to have kids, so..."</em></p>
            <p class="text--body-2">
              Oh lord, we sank right into the deep end of the cool-pool here! What follows is an intense debate over this major life decision between Amy (taking the affirmative) and Jake (taking the negative), judged by none other than Captain Raymond Holt (debate moderator license D810Y41JJ6).
            </p>
            <p class="text--body-2">
              Still, they did end up making the world's hottest baby by the end of season 7 (S07E13 - Lights Out) - aka McClane "Mac" Peralta-Santiago.
            </p>
            <img class="cool-img" src="07x13_baby.png" />
          </div>
        </div>

        <div class="cool-step last" data-step="6">
          <img src="02x11_jake_edit.png" height="100%" style="margin-top: -10%; margin-right: -15%;" />
          <div class="text-block" style="margin-bottom: 300px;">
            <p class="text--body-1 font-weight-bold">Many Many Cools</p>
            <p class="text--body-2">
              Yeah well we're definitely not counting these, but uncountable cool-chains include:
            </p>
            <p class="text--body-1 font-weight-bold">S02E11 - Stakeout</p>
            <p class="text--body-2">
              Peralta and Boyle both fire off some cool-chains over their no-no lists.
            </p>
            <p class="text--body-1 font-weight-bold">S03E12 - 9 Days</p>
            <p class="text--body-2">
              Captain Holt and Peralta finding extreme testicular discomfort very very cool.
            </p>
            <p class="text--body-1 font-weight-bold">S04E22 - Crime &amp; Punishment</p>
            <p class="text--body-2">
              Season 4 ends with lots of "cool"s as Jake gets sentenced to jailtime!
            </p>
            <p class="text--body-1 font-weight-bold">S06E10 - Gintars</p>
            <p class="text--body-2">
              Boyle machine-guns "cool"s and faints upon meet Nikolaj's birth father.
            </p>
          </div>
          <img src="02x11_charles_edit.png" height="100%" style="margin-top: -10%; margin-left: -20%;" />
        </div>
      </v-col>     
    </v-row>
  </v-container> 
</template>

<script>
import * as d3 from 'd3';
import scrollama from 'scrollama';

export default {
  name: 'VizCoolCoolScrollyOverlay',
  components: {},
  data() {
    return {
      publicPath: process.env.BASE_URL,
      coolSegments: [1, 1, 2, 4, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6]
    };
  },
  mounted() {
    this.initViz();
    this.initScrollama();    
  },  
  methods: {
    initViz() {
      d3.selectAll('p.cool')
          .style('transform', `translateX(100vw)`)
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
      const scrollerDesktop = scrollama();

      const stepH = Math.floor(window.innerHeight * 0.5);
      d3.selectAll('.cool-step').style("height", stepH + "px");
      // d3.selectAll('.step.first').style("height", null);

      // setup scrollama
      scrollerDesktop.setup({
        container: '.cool-scrolly-overlay',
        graphic: '.cool-scrolly-overlay .cool-scrolly__sticky',
        step: '.cool-scrolly-overlay .cool-scrolly__content .cool-step', // required
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
      let p
      if (response.index < 5) {
        p = Math.min(response.progress, 0.6)
        p /= 0.6
        d3.selectAll('p.cool-' + (response.index + 1))
          .style('transform', `translateX(${100 - 100 * p}vw)`)
      } else {
        p = Math.min(response.progress, 0.2)
        p /= 0.2
        d3.selectAll('p.cool-' + (response.index + 1))
          .style('transform', `translateX(${100 - 100 * p}vw)`)
      }
      if (response.index == 0) {
        d3.select('div#cool-intro')
          .style('opacity', 1 - p)
      }
      d3.selectAll('.cool-step')
        .style('opacity', 0)
      d3.select(response.element)
        .style('opacity', () => {
          if (response.progress >= 0.1 && response.index == 5) return 1
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

.cool-scrolly-overlay {
  max-width: 100%;
}

img.cool-img {
  width: 300px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}

.cool-scroll-prompt {
  position: relative;
}

.cool-scroll-prompt:after {
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
  padding: 36px;
  width: 50%;
  min-width: 250px;
  margin-left: auto;
  margin-right: auto;
}

.cool-casestudy-scrolly {
  z-index: 1000; 
}

.cool-scrolly__overlay {
  position: relative;
}

.cool-scrolly__content {
  position: relative;
  padding: 0 1rem;
  width: 100%;
}

.cool-step {
  margin: 0 auto 2rem auto;
  // border: 2px solid #104E8B;
  display: flex;
  justify-content: center;
  align-items: center;    
}

// .step:first-child {
//   //margin-top: calc(25vh);
// }

.cool-scrolly__sticky {
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