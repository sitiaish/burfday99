<template>
<article>
  <section class="section-intro py-12">
    <div class="section-intro-landing py-12">
      <v-container class="container--inner fill-height">
        <v-row justify="center" align="center">  
          <v-col cols="12" md="8" class="text-center">
            <p class="text--h2 font-tertiary--poorfamily">i am sad that</p>
            <h1 id='title'><em>BROOKLYN<br/>NINE-NINE</em></h1> 
            <p class="text--h2 font-tertiary--poorfamily">is ending at season 8</p>
          </v-col>
        </v-row>
      </v-container>
    </div>

    <div>
    <v-container inner>
      <v-row justify="center" align="end" class="fill-height">  
        <v-col cols="12" md="10">
          <p class="text--body-1">
            ...so we made this together. Hi I'm Aishah, and I am guilty of rewatching Brooklyn 99 episodes during my lunch breaks. This dataviz project is a birthday collab project with greentfrapp. 
          </p>

          <p class="text--body-1">
            SK scrapped B99 dialog from <a href="https://transcripts.foreverdreaming.org/viewforum.php?f=429">here</a>. And we tried to do something per character based on the dialog data that we have. Also the lines were not tagged to the character that spoke it, so we were limited that way. Pretty cool cool cool cool birthday gift!  
          </p> 
        </v-col>
      </v-row>
    </v-container>        
    </div>
  </section>

  <section class="section-marquee py-8">
    <div class="menu">
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
  </section>   
</article>
</template>

<script>
export default {
  name: 'SectionLanding',
}
</script>

<style lang="scss" scoped>
.section-intro {
  background: radial-gradient(47.59% 100.11% at 50% 47.6%, #ffffff 0%, #3e77bb 100%);
}

.section-intro-landing {
  height: 100vh;
}

.section-marquee {
  background: #FFF534;
}

#title {
  font-family: 'Anton', sans-serif;
  font-size: 100px;
  font-style: 'italic';
}

.font-tertiary--poorfamily {
  font-family: 'Poor Story', cursive !important;  
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