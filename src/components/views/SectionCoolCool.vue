<template>
  <section class="section_wrapper">
    <VizCoolCoolScrollyOverlay/>
    <VizCoolCoolGraph/>
  </section>
</template>

<script>
// import Map from '@/components/viz/Map'
import VizCoolCoolScrollyOverlay from '@/components/viz/VizCoolCoolScrollyOverlay'
import VizCoolCoolGraph from '@/components/viz/VizCoolCoolGraph'

export default {
  name: 'Section',
  mounted() {},
  components: {
    VizCoolCoolScrollyOverlay,
    VizCoolCoolGraph,
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
}

</style>