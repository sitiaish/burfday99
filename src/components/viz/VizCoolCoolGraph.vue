<template>
  <section class="section_wrapper py-12">
    <v-container class="inner py-12">
      <h3 class="text--h2 mb-16 scroll-prompt text-center">All the Cools ever!</h3>
      <v-row align="center" justify="center" no-gutters class="py-6">
        <v-col cols="12" md="9" xl="10">
          <p class="text--body-1 mb-4">
            A graph here to summarize all the cools
            </p>       
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
// import * as d3 from 'd3';

export default {
  name: 'VizCoolCoolGraph',
  components: {},
  data() {
    return {
      publicPath: process.env.BASE_URL,
    };
  },
  mounted() {
  },  
  methods: {
  },
}
</script>

<style lang="scss" scoped>
</style>