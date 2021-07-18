<template>
  <div>
    <div class="boost">
      <p class="text-h1">hello still can scroll here</p>
    </div>       <div class="boost">
      <p class="text-h1">hello still can scroll here</p>
    </div>       <div class="boost">
      <p class="text-h1">hello still can scroll here</p>
    </div>       <div class="boost">
      <p class="text-h1">hello still can scroll here</p>
    </div>       

    <div class="tall-container" id="tall">
      <div class="sticky" id="refd">
        <div class="horizontal-container" id="horizontal" :style="{transform: `translateX(${translate}px)`}">
          <div class="card-container">
            <div class="sample-card">
              hello
            </div>
            <div class="sample-card">
              this
            </div>
            <div class="sample-card">
              is
            </div>
            <div class="sample-card">
              the
            </div>                                    
            <div class="sample-card"/>
            <div class="sample-card" />                
          </div>
        </div>
      </div>
    </div>
    <div class="boost">
      <p class="text-h1">hello still can scroll here</p>
    </div>    
  </div>
</template>

<script>
export default {
  head() {
    return {
      title: 'Career',
      meta: [
        {
          hid: 'description',
          name: 'description',
          content:
            'We are always on the look out for passionate individuals to join our team. If you believe that there is something unique you can bring to our cause, please drop us an e-mail with your resume and cover letter',
        },
      ],
    };
  },
  data() {
    return {
      translate: 0,
    }
  },
  mounted() {
    this.calcDynamicHeight();
    this.addScrollOffset();
  },
  methods: {
    calcDynamicHeight() {
      const vw = window.innerWidth;
      const vh = window.innerHeight;   
      const objectWidth = document.getElementById('horizontal').scrollWidth
      document.getElementById("tall").style.height = objectWidth - vw + vh  + 'px';
    },
    addScrollOffset() {
      window.addEventListener("scroll", () => {
        const offsetTop = document.getElementById("refd").offsetTop;
        const offsetParent = document.getElementById("tall").offsetTop; 
        this.translate = (offsetParent - offsetTop);
      });      
    }
  }

};
</script>

<style scoped>
.boost {
  background-color: palegreen;
  height: 50vh;
  text-align: center;
}

.tall-container {
  border: 5px solid orange;
}

.sticky {
  position: sticky;
  top: 64px;
  height: calc(100vh - 80px);
  width: 100%;
  overflow-x: hidden;
  background-color: pink;
}

.horizontal-container {
  position: absolute;
  height: 100%;
  will-change: transform;
  border: 2px solid purple;
}

.card-container {
  position: relative;
  height: 100%;
  margin: 0 0 0 150px;
  display: flex;
  flex-flow: row nowrap;
  justify-content: flex-start;
  align-items: center;
  border: 10px solid black;
  background-color: grey;
}

.sample-card {
  position: relative;
  height: 400px;
  width: 500px;
  background-color: yellow;
  margin-right: 75px;
  flex-shrink: 0;
}
</style>