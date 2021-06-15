<template>
  <div>
    <SectionLandingHepC />
    <Section1DiseasesBar />
    <Section2HepC />
    <Section3PakistanCS />
    <Section4BangladeshCS />
    <Section5PatientProfile />
    <Section6PatientProfile />
    <Section7SolutionModel />
    <SectionReferencesHepC />
  </div>
</template>

<script>
import SectionLandingHepC from '@/components/views/SectionHepCLanding'
import Section1DiseasesBar from '@/components/views/Section1DiseasesBar';
import Section2HepC from '@/components/views/Section2HepCBar';
import Section3PakistanCS from '@/components/views/Section3PakistanCS'
import Section4BangladeshCS from '@/components/views/Section4BangladeshCS';
import Section5PatientProfile from '@/components/views/Section5PatientProfile';
import Section6PatientProfile from '@/components/views/Section6PatientProfile'
import Section7SolutionModel from '@/components/views/Section7SolutionModel';
import SectionReferencesHepC from '@/components/views/SectionHepCReferences';

export default {
  name: 'Main',
  components: {
    SectionLandingHepC,
    Section1DiseasesBar,
    Section2HepC,
    Section3PakistanCS,
    Section4BangladeshCS,
    Section5PatientProfile,
    Section6PatientProfile,
    Section7SolutionModel,
    SectionReferencesHepC,
  },
  data: () => ({}),
}
</script>