<template>
  <div class="profile-type-1 d-flex align-center">
    <div class="profile-image">
      <img src="https://picsum.photos/500/600/?random=1">
    </div>        
    <div class="pa-4">
      <h4 class="text--body-1 font-weight-bold mb-2">{{ patientName }}</h4>
      <h4 class="text--body-1 font-weight-bold mb-6">{{ patientLocation }}</h4>

      <p class="text--body-2 font-weight-medium mb-4">{{ descPara1 }}</p>

      <p class="text--body-2 font-weight-medium mb-4">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Ipsam in reiciendis repellendus odit repudiandae praesentium quos amet nulla, provident eum placeat? Eius voluptatem vel numquam provident eveniet a, amet quam.
      </p>  
    </div>  
  </div>   
</template>

<script>
export default {
  name: 'VizPatientProfile1',
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
.profile-type-1 {
  background-color: #F1ECE1;
  position: relative;
  width: calc(100% - 48px);
  left: 48px;
  margin-bottom: 96px;

  .profile-image {
    position: relative;
    top: -48px;
    left: -48px;
    img {
      display: block;
      @media #{map-get($display-breakpoints, 'sm-and-down')} {
        width: 100%;
      }    
    }
  }  
}
</style>