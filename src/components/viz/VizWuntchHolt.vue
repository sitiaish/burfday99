<template>
  <div class="pa-12">
    <v-row class="data-row" no-gutters align="center" justify="center" v-for="(data, id) in groupedData" :key="id">
      <!-- use a v-for to populate the divs  -->
      <v-col cols="1">
        <h2>S{{data[1][0].season}}E{{data[1][0].episode}}</h2>
      </v-col>
      <v-col cols="8">
        <div class="pa-3">
          <p 
            v-for="(n, i) in data[1]"
            :key="i"
            :class="['mb-0, line', n.who === 'Wuntch' || n.who === 'Holt' ? n.who : 'other', n.type]"> 
              {{n.line}}
          </p>
        </div>
      </v-col>
    </v-row>
  </div>
</template>

<script>
import * as d3 from 'd3';
import _kebabCase from 'lodash.kebabcase';

export default {
  data() {
    return {
      tooltip: {
        show: false,
        name: '',
        hex: '',
        move: {
          top: 0,
          left: 0,
        },
      },
      data: [
        {
          "who": "wuntch",
          "line": "Hello, Raymond.",
          "length": 2,
          "type": "no"
        },
        {
          "who": "holt",
          "line": "Captain Wuntch. Good to see you.",
          "length": 6,
          "type": "no"
        },
        {
          "who": "holt",
          "line": "But if you're here, who's guarding Hades?",
          "length": 7,
          "type": "insult"
        },
        {
          "who": "wuntch",
          "line": "It's deputy chief Wuntch now. ",
          "length": 5,
          "type": "no"
        },
        {
          "who": "wuntch",
          "line": "Unsurprisingly, I've been promoted above you. And now I'm here to evaluate you.",
          "length": 13,
          "type": "insult"
        }
      ]
    };
  },   
  mounted() {
    // to run format data on load
    this.loadData()
  },
  computed: {
    groupedData() {
      return d3.group(this.data, d => d.id)
    }
  },
  methods: {
    async loadData() {
      this.data = await d3.csv('/data/wuntch-holt.csv')
      this.$nextTick(() => {
        console.log('test')
        console.log(this.groupedData)
      })
    },
    formatData() {
      // load csv
      // group data by id
      // for each id to create a div in v-col cols="3"
      // in the div, append paragraphs based on the lines
      // style the lines based on who said it and if it is an insult
    },       
    handleTooltip() {
      this.rect
        .on('mouseenter.data', (event, d) => {
          this.tooltip.show = true;
          this.tooltip.name = d.title;
          this.tooltip.hex = d.hex;
        })
        .on('mouseenter.design', function showBox() {
          // highlight the circle
          d3.select(this).attr('stroke', '#2c3e50').raise();
          // move the tooltip to the correct position
          const selectedRect = d3
            .select(this)
            .node()
            .getBoundingClientRect();
          const tooltip = d3
            .select('.viz-tooltip')
            .node()
            .getBoundingClientRect();
          const chart = d3
            .select('#chartWuntchHolt')
            .node()
            .getBoundingClientRect();
          
          const posLeft =
            selectedRect.left > document.body.clientWidth / 2.25
              ? selectedRect.left - chart.left - tooltip.width - 5// right
              : selectedRect.right - chart.left + 5  // left

          const posTop = 
            selectedRect.top > document.body.clientHeight / 2.5
              ? selectedRect.bottom - chart.top - tooltip.height // bottom
              : selectedRect.top - chart.top // top
          
          d3.select('.viz-tooltip')
            .style('top', `${posTop}px`)
            .style('left', `${posLeft}px`);
        })
        .on('mouseleave.design', function hideBox() {
          // remove highlight from the circle
          d3.select(this).attr('stroke', d => d.hex === '#FFFFFF' ? '#ededed' : 'none');
        })
        .on('mouseleave.data', () => {
          // reset tooltip settings
          this.tooltip.show = false;
          this.tooltip.name = '';
          this.tooltip.hex = ''; 
        });
    },
    kebabCase(string) {
      return _kebabCase(string)
    },       
  },
};
</script>

<style lang="scss" scoped>
.Wuntch {
  background: repeating-linear-gradient(
    45deg,
    rgba(0, 0, 0, 0.4),
    rgba(0, 0, 0, 0.4) 10px,
    rgba(0, 0, 0, 0.5) 10px,
    rgba(0, 0, 0, 0.5) 20px), #eb2f06;
}

.Wuntch:before {
  content: url(/wuntch_tiny.png);
  vertical-align: text-top; 
}

.Holt {
  background: repeating-linear-gradient(
    45deg,
    rgba(0, 0, 0, 0.4),
    rgba(0, 0, 0, 0.4) 10px,
    rgba(0, 0, 0, 0.5) 10px,
    rgba(0, 0, 0, 0.5) 20px), #1e3799;
}

.Holt:before {
  content: url(/holt_tiny.png);
  vertical-align: text-top; 
}

.other {
  background: repeating-linear-gradient(
    45deg,
    rgba(0, 0, 0, 0.4),
    rgba(0, 0, 0, 0.4) 10px,
    rgba(0, 0, 0, 0.5) 10px,
    rgba(0, 0, 0, 0.5) 20px), #57606f;
}

.data-row {
  background-color: rgba(0, 0, 0, 0.1);
  margin: 2px;
}

.data-row:hover {
  background-color: rgba(255, 255, 255, 0.7);
  cursor: pointer;
}

.line {
  padding: 0px 4px;
  //margin: 5px;
  margin-right: 8px;  
  display: inline;
  border-radius: 25px;
  font-size: 18px;
  //color: transparent;
  color: grey;
  user-select: none;
  cursor: pointer;  
  overflow-wrap: break-word;
}

.line:hover {
  color: white;
}

.insult {
  background-image: unset !important;
  color: white;
}
</style>
