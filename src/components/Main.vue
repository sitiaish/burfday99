<template>
  <div>
    <SectionLanding />
    <SectionTerryLoves />
    <SectionCoolCool />
    <SectionReferencesHepC />
  </div>
</template>

<script>
import SectionLanding from '@/components/views/SectionLanding'
import SectionTerryLoves from '@/components/views/SectionTerryLoves'
import SectionCoolCool from '@/components/views/SectionCoolCool'
import SectionReferencesHepC from '@/components/views/SectionHepCReferences';

export default {
  name: 'Main',
  components: {
    SectionLanding,
    SectionTerryLoves,
    SectionCoolCool,
    SectionReferencesHepC,
  },
  data: () => ({}),
}
</script>