<template>
  <section class="section_wrapper">    
    <v-container class="container--inner">
      <v-row justify="center" align="bottom" class="fill-height">  
        <v-col cols="12" md="8" class="text-center">
          <h1 class="text--h1 font-weight-regular">Title</h1>       
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
// import Map from '@/components/viz/Map''

export default {
  name: 'Section',
  coponents: {},
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
  background-color: #F4F1EB;
  height: calc(100vh - 64px)
}

</style>