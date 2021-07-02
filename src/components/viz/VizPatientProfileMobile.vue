<template>
  <div class="profile-mobile mb-8">      
    <img src="https://picsum.photos/500/600/?random=1">
    <v-container class="py-12">
      <v-row justify="center" align="center">  
        <v-col cols="12">
          <div class="pa-4">
            <h4 class="text--body-1 font-weight-bold mb-2">{{ patientName }}</h4>
            <h4 class="text--body-1 font-weight-bold mb-6">{{ patientLocation }}</h4>

            <p class="text--body-2 font-weight-medium mb-4">{{ descPara1 }}</p>
          </div>     
        </v-col>   
      </v-row>
    </v-container>    
  </div>
</template>

<script>
export default {
  name: 'VizPatientProfileMobile',
  props: {
    patientName: {
      type: String,
      default: '',
    },
    patientLocation: {
      type: String,
      default: '',
    },  
    imgId: {
      type: String,
      default: '',
    },       
    descPara1: {
      type: String,
      default: '',
    },     
    descPara2: {
      type: String,
      default: '',
    },     
    descPara3: {
      type: String,
      default: '',
    },              
  },
}
</script>

<style lang="scss" scoped>
.profile-mobile {
  background-color: #F1ECE1;

  img {
    display: block;
    @media #{map-get($display-breakpoints, 'sm-and-down')} {
      width: 100%;
    }    
  }
}
</style>