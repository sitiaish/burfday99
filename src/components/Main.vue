<template>
  <div>
    <SectionLandingHepC />
    <SectionReferencesHepC />
  </div>
</template>

<script>
import SectionLandingHepC from '@/components/views/SectionHepCLanding'
import SectionReferencesHepC from '@/components/views/SectionHepCReferences';

export default {
  name: 'Main',
  components: {
    SectionLandingHepC,
    SectionReferencesHepC,
  },
  data: () => ({}),
}
</script>