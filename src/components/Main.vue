<template>
  <div>
    <SectionLanding />
    <Section1TerryLoves />
    <SectionCoolCool />
    <Section2SexTapes />   
    <Section3WuntchHolt />
    <SectionReferences /> 
  </div>
</template>

<script>
import SectionLanding from '@/components/views/SectionLanding'
import Section1TerryLoves from '@/components/views/Section1TerryLoves'
import Section2SexTapes from '@/components/views/Section2SexTapes'
import Section3WuntchHolt from '@/components/views/Section3WuntchHolt'
import SectionCoolCool from '@/components/views/SectionCoolCool'
import SectionReferences from '@/components/views/SectionReferences';

export default {
  name: 'Main',
  components: {
    SectionLanding,
    Section1TerryLoves,
    Section2SexTapes,
    Section3WuntchHolt,
    SectionCoolCool,
    SectionReferences,
  },
  data: () => ({}),
}
</script>