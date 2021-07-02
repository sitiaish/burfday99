<template>
  <section class="section_wrapper py-12">    
    <v-container inner class="container py-12">
      <v-row justify="center" align="center">  
        <v-col cols="12" md="12">
          <h3 class="text--h4 mb-8 text-center">
            It goes back to unequal access to healthcare 
          </h3>
          <p class="text--body-2">
            While MSF’s work with the most vulnerable communities in Asia has shown that a shorter and affordable model of treatment for hepatitis C is possible and scalable, many treatment regimens around the world remain out of reach for people who need to pay for medication out-of-pocket, or make arduous journeys just to get to a hospital. Without improved access to HCV diagnosis and treatment, it will be an uphill battle to end the suffering of those living with hepatitis C and stem its spread.
          </p>                 
          <p class="text--body-2">
            In the long run, a decentralised model of treatment will serve to bring a cure for hepatitis C closer to people in rural and remote areas across the region. Local clinics within a short distance of people’s homes that are able to test and treat HCV will make a huge difference to saving lives, as will greater health financing and proper training of healthcare workers who are regularly exposed to blood. 
          </p>
          <p class="text--body-2 mb-12">
            At the root of the hepatitis C epidemic lies the deep disparity between countries and people who can afford to cure the disease, and those who have no choice but to continue suffering in silence. The scourge of hepatitis C can only come to an end if the world is committed to lift its burden from those who are most deprived. 
          </p>

          <h3 class="text--body-1 mb-2 font-weight-bold text-center">
            What can you do to prevent the transmission of hepatitis C?
          </h3>          

          <p class="text--body-2 text-center">
            Click on the cards to find out more
          </p>
        </v-col>
      </v-row>

      <v-row justify="space-between" align="start">  
        <v-col v-for="(n, i) in prevention" :key="i" cols="6" md="4" class="text-center mb-6 mb-md-12">
          <div class="image-wrapper" @click="openDialog(n.name, n.id)">
            <img :src="`https://picsum.photos/270/330?random=${i}`" class="mb-5" width="100%">
            <div class="image-label pa-2">{{ n.name }}</div>
          </div>
        </v-col>

        <v-dialog
          v-model="dialog"
          max-width="600"
          overlay-opacity="0.7">
            <div class="dialog-text pt-10 pb-8 px-8">
              <v-icon @click.native="dialog = false">mdi-close</v-icon>
              <div>
                <p class="text--body-1 font-weight-medium pa-2 mb-0 dialog-title text-center">{{ selectedPrevention.title }}</p>
              </div>
              
              <img :src="`https://picsum.photos/150/150?random=${selectedPrevention.img}`" class="px-2 my-5">

              <p class="text--body-2">
                Lorem ipsum dolor sit amet, consectetur ad enim adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
              </p>

              <p class="text--body-2">
                Ut enim ad minim veniam, quis nostrud dolore exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
              </p>
            </div>    
        </v-dialog> 
      </v-row>
    </v-container>
  </section>
</template>

<script>
export default {
  name: 'Section8Prevention',
  components: {},
  data() {
    return {
      publicPath: process.env.BASE_URL,
      prevention: [
        {id: 1, name: 'Get your blood screened', desc: ''},
        {id: 2, name: 'Never share needles, razors and toothbrushes'},
        {id: 3, name: 'Prevent transmitting HCV to your child'},
        {id: 4, name: 'Use only sterilized tattoo, acupuncture and piercing instruments'},
        {id: 5, name: 'Use condoms correctly and consistently'},
        {id: 6, name: 'Choose oral medications instead of injections'},                              
      ],
      dialog: false,    
      selectedPrevention: {
        title: 'Prevention something',
        img: '',
      }
    };
  },
  methods: {
    openDialog(title, img) {
      this.selectedPrevention.title = title;
      this.selectedPrevention.img = img;
      this.dialog = true;
    }
  },
}
</script>

<style lang="scss" scoped>
.section_wrapper {
  background-color: #F4F1EB;
}

img {
  margin: 0 auto;
  display: block;
}

// dialog 
.v-dialog__content {
  ::v-deep.v-dialog {
    border-radius: 0 !important;
  }
}

.dialog-text {
  background-color: #FAFAFA;      
  color: #2E2E2E;
  position: relative;

  .v-icon {
    position: absolute;
    top: 12px;
    right: 16px;
  }

  .v-icon:hover {
    cursor: pointer;
  }
  
  div {
    display: flex;
    justify-content: center;
    align-items: center;    
  }

  p.dialog-title {
    border: 1px solid #2E2E2E;
    display: inline-block;
    background: #F4F1EB;
  }

  img.category-icon {
    vertical-align: middle;
  }      
}
$dialog-border-radius: 0;

.image-wrapper {
  cursor: pointer;
  
  .image-label {
    border: 1px solid #2E2E2E;
    width: 90%;
    display: block;
    margin: 0 auto;
  }
}
</style>