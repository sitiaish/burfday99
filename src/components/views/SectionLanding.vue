<template>
  <section class="section_wrapper py-12">    
    <v-container class="container--inner">
      <v-row justify="center" align="end" class="fill-height">  
        <v-col cols="12" md="8" class="text-center">
          <h1 id='title'><em>BROOKLYN<br/>NINE-NINE</em></h1> 
        </v-col>
      </v-row>
    </v-container>

    <div class="menu my-6">
      <div class="menu__item">
        <div class="marquee">
          <div class="marquee__inner">
            <span
              v-for="(n, i) in 10"
              :key="i"
              class="text--h4 font-tertiary"
              style="padding-left: 0; padding-right: 5px;"
            >
              <em>noice smort toit noice smort toit</em>
            </span>
          </div>
        </div>
      </div>
    </div>

    <v-container inner>
      <v-row justify="center" align="end" class="fill-height">  
        <v-col cols="12" md="6">
          <p class="text--body-2">
            Hi I'm Aishah, and I am guilty of rewatching Brooklyn 99 episodes during my lunch breaks. This dataviz project is a birthday collab project with greentfrapp. 
          </p>

          <p class="text--body-2">
            SK scrapped B99 dialog from here. And we try to something per character based on the dialog data that we have. Also the lines were not tagged to the character that spoke it, so we were limited that way. Pretty cool cool cool cool birthday gift!  
          </p> 
        </v-col>
      </v-row>
    </v-container>    
  </section>
</template>

<script>
export default {
  name: 'SectionLanding',
}
</script>

<style lang="scss" scoped>
.section_wrapper {
  background-color: #fff534;
  min-height: 100vh;
}

#title {
  font-family: 'Anton', sans-serif;
  font-size: 100px;
  font-style: 'italic';
}

.menu {
  counter-reset: menu;
  --marquee-width: 100vw;
  --offset: 20vw;
  --move-initial: calc(-25% + var(--offset));
  --move-final: calc(-50% + var(--offset));
  --move-initial-counter: calc(-50% + var(--offset));
  --move-final-counter: calc(-25% + var(--offset));
}

.marquee {
  top: 0;
  left: 0;
  width: var(--marquee-width);
  overflow: hidden;
}

.marquee__inner {
  width: fit-content;
  display: flex;
  position: relative;
  transform: translate3d(var(--move-initial), 0, 0);
  animation: marquee 7s linear infinite;
  animation-play-state: running;

  &:hover,
  &:active {
    span {
      color: #fff534;
      background-color: #000000;
    }
  }
}

.marquee__inner.counter {
  width: fit-content;
  display: flex;
  position: relative;
  transform: translate3d(var(--move-initial-counter), 0, 0);
  animation: marquee-counter 9s linear infinite;
  animation-play-state: running;
}

.marquee span {
  white-space: nowrap;
  padding: 0 20px;
}

@keyframes marquee {
  0% {
    transform: translate3d(var(--move-initial), 0, 0);
  }

  100% {
    transform: translate3d(var(--move-final), 0, 0);
  }
}

@keyframes marquee-counter {
  0% {
    transform: translate3d(var(--move-initial-counter), 0, 0);
  }

  100% {
    transform: translate3d(var(--move-final-counter), 0, 0);
  }
}

</style>