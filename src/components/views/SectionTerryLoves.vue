<template>
  <section class="section_wrapper">
    <VizBangladeshScrollySide/>
  </section>
</template>

<script>
// import Map from '@/components/viz/Map'
import VizBangladeshScrollySide from '@/components/viz/VizBangladeshScrollySide'

export default {
  name: 'Section',
  components: {
    VizBangladeshScrollySide,
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
  background-color: #F4F1EB;
  //height: calc(100vh - 64px);
}

</style>