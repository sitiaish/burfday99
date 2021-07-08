<template>
  <section class="section_wrapper">    
    <v-container class="container--inner">
      <v-row justify="center" align="end" class="fill-height">  
        <v-col cols="12" md="8" class="text-center">
          <h1 id='title'><em>BROOKLYN<br/>NINE-NINE</em></h1> 
        </v-col>
      </v-row>
    </v-container>
  </section>
</template>

<script>
// import Map from '@/components/viz/Map'
import variables from '../../styles/_typography.scss';

export default {
  name: 'Section',
  components: {},
  data() {
    return {
      publicPath: process.env.BASE_URL,
      variables
    };
  },
  methods: {},
}
</script>

<style lang="scss" scoped>
.section_wrapper {
  background-color: #fff534;
  height: 100vh;
}
#title {
  font-family: 'Anton', sans-serif;
  font-size: 100px;
  font-style: 'italic';
}

</style>