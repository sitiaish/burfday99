<template>
  <section class="section_wrapper py-12">
    <v-container class="inner">
      <h3 class="text--h2 mb-16 scroll-prompt text-center">Titles of (mostly) Amy's Sex Tapes</h3>

      <v-row align="center" justify="center" no-gutters class="py-6">
        <v-col cols="12" xl="10">
          <p class="text--body-1 mb-4">
            <em>Title of your sex tape</em>. As Boyle said it, "Oh, that's just something we say back at the Nine-Nine." Another running gag is the highly inappropriate titling of people's sex tapes, mostly done by Jake to Amy throughout the seasons. 
          </p>

          <iframe class="my-8 youtube-iframe" src="https://www.youtube.com/embed/idQR0oARcIY" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>         
        </v-col>
      </v-row>
    </v-container>

    <VizSexTape />

  </section>
</template>

<script>
import VizSexTape from '@/components/viz/VizSexTape'

export default {
  name: 'Section2SexTapes',
  components: {
    VizSexTape,
  },
  data() {
    return {
    };
  },
}
</script>

<style lang="scss" scoped>
.section_wrapper {
  background-color: white;
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
  content: '👅';
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


.marquee {
    width: 100%;
    height: 150px;
    overflow: hidden;
}

.marquee-content {
    display: flex;
    list-style: none;
    animation: scrolling 10s linear infinite;
}

.marquee-item {
    height: 150px;
    width: 200px;
    flex-shrink: 0;
    margin: 0 50px;
}

.marquee-image {
    height: 100%;
    width: 100%;
}

@keyframes scrolling {
    0% { transform: translateX(0); }
    100% { transform: translatex(-100%); }
}

.youtube-iframe {
  display: block;
  margin: 0 auto;
  width: 560px;
  height: 315px;
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    width: 100%;
  }      
}
</style>