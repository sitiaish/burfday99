<template>
  <section class="section_wrapper">
    <VizCoolCoolScrollyOverlay v-if="!$vuetify.breakpoint.mobile" />
    <VizCoolCoolScrollyMobile v-if="$vuetify.breakpoint.mobile" />
    <VizCoolCoolGraph/>
  </section>
</template>

<script>
import VizCoolCoolScrollyMobile from '@/components/viz/VizCoolCoolScrollyMobile'
import VizCoolCoolScrollyOverlay from '@/components/viz/VizCoolCoolScrollyOverlay'
import VizCoolCoolGraph from '@/components/viz/VizCoolCoolGraph'

export default {
  name: 'Section',
  mounted() {},
  components: {
    VizCoolCoolScrollyMobile,    
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