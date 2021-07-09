<template>
  <section class="section_wrapper py-12">    
    <v-container class="container--inner">
      <v-row justify="center" align="end" class="fill-height">  
        <v-col cols="12" md="8" class="text-center">
          <p id='title'><em>BROOKLYN<br/>NINE-NINE</em></p> 
        </v-col>
      </v-row>
    </v-container>

    <v-container inner>
      <v-row justify="center" align="end">  
        <v-col cols="12" md="6">
          <p class="text--body-2 font-tertiary text-center">
            FREMULON! NOT A DOKTER! SHH. 
          </p> 
        </v-col>
      </v-row>
    </v-container>    
  </section>
</template>

<script>
export default {
  name: 'SectionReferences',
}
</script>

<style lang="scss" scoped>
.section_wrapper {
  background-color: #fff534;
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
      color: white;
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