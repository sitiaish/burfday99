<template>
  <section class="section_wrapper">
    <v-container class="inner py-12">
      <h3 class="text--h2 mb-16 scroll-prompt text-center">The Wuntch-Holt Feud</h3>

      <v-row align="center" justify="center" no-gutters class="py-6">
        <v-col cols="12" xl="10">
          <p class="text--body-1 mb-4">
            I've always enjoyed the Wuntch-Holt petty arguments because it detracts Holt from his robotic, no nonsense-Captain personality. That, and also Holt's heterosexual acting -- "bitch please!". I wanted to see the winner between the back and forth between them in their dialogues by finding the roasts in their banter.
          </p>

          <p class="text--body-1 mb-4">
            Note: I know that it's subjective to classify which lines are roasts, but if I had more time and access to a machine learning sentiment analysis maybe it'll be slightly more scientific. But for now, here's a quick classification with reference to 
            <a href="https://brooklyn99.fandom.com/wiki/Holt-Wuntch_Relationship#:~:text=Wuntch%20is%20introduced%20as%20Holt's%20arch%20nemesis.&text=It%20is%20revealed%20in%20a,is%20angry%20for%20other%20reasons." target="_blank">
            this Wuntch-Holt wiki page
            </a>. 
          </p>

          <iframe width="560" height="315" class="my-8" src="https://www.youtube.com/embed/tqf5slEsdh0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>         
        </v-col>
      </v-row>
    </v-container>

    <div>
      <v-row class="holt-wuntch-title" justify="center">
        <v-col cols="6" class="holt-title" style="background-color: rgba(0, 0, 255, 0.2); color: white;">
          <p class="text--header text-right">Holt</p>
        </v-col>
        <v-col cols="6"  style="background-color: rgba(255, 0, 0, 0.2); color: white;">
          <p class="text--header  holt-hyphen">Wuntch</p>
        </v-col>        
      </v-row>
    </div>

    <VizWuntchHolt />

    <VizWuntchHoltInsults />
  </section>
</template>

<script>
import VizWuntchHolt from '@/components/viz/VizWuntchHolt'
import VizWuntchHoltInsults from '@/components/viz/VizWuntchHoltInsults'

export default {
  name: 'Section',
  components: {
    VizWuntchHolt,
    VizWuntchHoltInsults
  },
  data() {
    return {
      publicPath: process.env.BASE_URL,
    };
  },
  methods: {},
}
</script>

<style lang="scss" scoped>
.section_wrapper {
  background: #fff534;
}

.scroll-prompt {
  position: relative;
}

.scroll-prompt:after {
  content: '🤼';
  position: absolute;
  top: calc(100% + 8px);
  bottom: -48px;
  left: 50%;
  border-top: 4px solid #2e2e2e;
  transform: translate(-50%);
}

.text--header {
  margin-bottom: 0;
}

.holt-wuntch-title {
  background-image: url(/holt_wuntch.png);
  background-size: cover;
  background-position: center;
  background-attachment: fixed;
}

.holt-hyphen {
  position: relative;
}

.holt-hyphen:before {
  content: '-';
  position: absolute;
  top: 0;
  bottom: 0;
  left: -23px;
  color: white;
}
</style>