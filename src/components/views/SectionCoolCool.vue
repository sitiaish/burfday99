<template>
  <section class="section_wrapper">
    <VizCoolCoolScrollyOverlay/>
  </section>
</template>

<script>
// import Map from '@/components/viz/Map'
import VizCoolCoolScrollyOverlay from '@/components/viz/VizCoolCoolScrollyOverlay'

export default {
  name: 'Section',
  mounted() {},
  components: {
    VizCoolCoolScrollyOverlay,
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
  background-color: #fff534;
  //height: calc(100vh - 64px);
}

</style>