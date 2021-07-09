<template>
  <div>
    <SectionLanding />
    <Section1TerryLoves />
    <SectionCoolCool />
    <SectionReferences />
  </div>
</template>

<script>
import SectionLanding from '@/components/views/SectionLanding'
import Section1TerryLoves from '@/components/views/Section1TerryLoves'
import SectionCoolCool from '@/components/views/SectionCoolCool'
import SectionReferences from '@/components/views/SectionReferences';

export default {
  name: 'Main',
  components: {
    SectionLanding,
    Section1TerryLoves,
    SectionCoolCool,
    SectionReferences,
  },
  data: () => ({}),
}
</script>