<template>
<v-container>
  <div class="my-5">
    <p class="text--h4 font-tertiary text-center">What are the titles of 
      <v-select 
        style="width: 130px;"
        item-text="name"
        item-value="value"
        v-model="defaultWhose"      
        :items="whose"
        @input="colorByWhose($event)" /> 
      sex's tapes?</p>  

    <div v-if="this.$vuetify.breakpoint.smAndDown">   
      <v-card
        class="viz-tooltip pa-3 tooltip-container"
        flat
      >
        <img src="tape.png" width="100%" />
        <div class="centered">{{ tooltip.name }}</div>
      </v-card>
    </div>

    <!-- Viz Starts here -->
    <div id="chart" class="my-4">
      <svg id="colorsSVG"/>
      <div v-if="this.$vuetify.breakpoint.mdAndUp">   
        <v-card
          v-show="tooltip.show"
          class="viz-tooltip pa-3 tooltip-container"
          flat
          :style="{ top: `${tooltip.move.top}px`, left: `${tooltip.move.left}px` }"
        >
          <img src="tape.png" width= "100%" />
          <div class="centered">{{ tooltip.name }}</div>
        </v-card>
      </div>
    </div>
  </div>
</v-container>
</template>

<script>
import * as d3 from 'd3';
import _kebabCase from 'lodash.kebabcase';

export default {
  data() {
    return {
      innerWidth: 700,
      filterlist: [
        {id: 'pronoun [your]', description: 'Title of YOUR sex tap'},
        {id: 'every time Jake said it', description: 'and the times that he did not'},
      ],
      whose: [
        {name: "Amy's", value: 'amy' },
        {name: "Jake's", value: 'jake' },
        {name: "Boyle's", value: 'boyle' },
        {name: "Holt's", value: 'holt' },
        {name: "everyone's", value: "all"}
      ],
      vizSettings: {
        scale: {},
        axis: {},
      },
      tooltip: {
        show: false,
        name: '',
        hex: '',
        move: {
          top: 0,
          left: 0,
        },
      }, 
      defaultWhose: {name: "everyone's", value: "all"}
    };
  }, 
  computed: {
    innerHeight() {
      if (this.$vuetify.breakpoint.smAndDown) {
        return 600;
      }
      return 250;
    },
    gap() {
      if (this.$vuetify.breakpoint.smAndDown) {
        return 30;
      }
      return 18;
    },    
    chartMargin() {
      return { top: 20, right: 10, bottom: 30, left: 10 };
    },
    chartSettings() {
      return {
        width: this.innerWidth + this.chartMargin.left + this.chartMargin.right,
        height: this.innerHeight + this.chartMargin.top + this.chartMargin.bottom,
      };
    }, 
  },  
  async mounted() {
    this.drawBase();
    this.data = await d3.csv('/data/sex-tape.csv');
    this.$nextTick(() => {
      this.formatData();
      this.drawBars();
    })
  },
  methods: {
    formatData() {
      this.formatted = Array.from(d3.group(this.data, d => d.season), ([key, value]) => ({key, value}));
      this.formatted.forEach(season => {
        let startY = 0;
        season.value.forEach(d => {
          d.startY = startY;
          d.endY = 6 +d.startY;
          startY = d.endY;
        });
      });
    },     
    drawBase() {
      const colorsSVG = d3.select('#colorsSVG');
      // draw base
      colorsSVG
        .attr('width', this.chartSettings.width)
        .attr('height', this.chartSettings.height)
        .call(this.responsivefy);

      // axes
      this.vizSettings.scale.x = d3
        .scaleLinear()
        .domain([0.5, 7.5])
        .range([0, this.innerWidth]);
      this.vizSettings.scale.y = d3
        .scaleLinear()
        .domain([0, 120])
        .range([this.innerHeight, 0]);        

      colorsSVG
        .append('g')
        .attr('class', 'XAxis')
        .attr('transform', `translate(${this.chartMargin.left}, ${this.innerHeight + this.chartMargin.top})`)
        .call(d3
          .axisBottom(this.vizSettings.scale.x)
          .ticks(8)
          .tickSize(10)
          .tickSizeOuter(0)
          .tickFormat(d => 'Season ' + d)
        );

      colorsSVG
        .append('g')
        .attr('class', 'YAxis')
        .attr('transform', `translate(${this.chartMargin.left}, ${this.chartMargin.top})`)
        .call(d3
          .axisLeft(this.vizSettings.scale.y)
          .tickSize(0)
        )
        .call(g => g.selectAll('.tick')).attr('visibility','hidden');      
    },
    drawBars() {
      const data = this.formatted; 
      // clear all bars first 
      d3.selectAll('rect.sex-tape').remove();
      // draw bars
      const group = d3.select('#colorsSVG')
        .append('g')
        .attr('transform', `translate(-${this.innerWidth / 24 + this.chartMargin.left}, 0)`)
        .selectAll(`g.${data.key}`)
        .data(data)
        .enter()
        .append('g')
        .attr('class', d => d.key);
      this.rect = group
        .selectAll('text.sex-tape')
        .data(d => d.value)
        .enter()
        // .append('rect')
        .append('text')
        .text('📼')
        .attr('class', 'sex-tape')        
        .attr('x', d => this.vizSettings.scale.x(+d.season))
        .attr('y', (d, i) => this.vizSettings.scale.y(d.startY) - i * 30)
        .attr('transform', `translate(35, 0)`)
        .attr('height',  (d) => this.vizSettings.scale.y(d.startY) - this.vizSettings.scale.y(d.endY));
      
      this.colorByWhose('all');
      this.handleTooltip();      
    },
    colorByWhose(selected) {
      const selectedPerson = this.kebabCase(selected);
      d3.selectAll('text.sex-tape')
        .attr('opacity', 1);
      
      d3.selectAll('text.sex-tape')
        .attr('opacity', d => {
          if (selectedPerson === 'all') {
            return 1
          } else {
            return this.kebabCase(d.whoseSexTape) === selectedPerson ? 1 : 0.25
          }
        });
    },    
    handleTooltip() {
      this.rect
        .on('mouseenter.data', (event, d) => {
          this.tooltip.show = true;
          this.tooltip.name = d.title;
          this.tooltip.hex = d.hex;
          console.log(this.tooltip);
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

      if (this.$vuetify.breakpoint.mdAndUp) {
        this.rect
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
              .select('#chart')
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
            d3.select(this).style("cursor", "pointer");
          })      
      }
    },
    kebabCase(string) {
      return _kebabCase(string)
    },    
    responsivefy(svg) {
      const width = parseInt(svg.style('width'), 10);
      const height = parseInt(svg.style('height'), 10);
      const aspect = width / height;

      svg
        .attr('viewBox', `0 0 ${width} ${height}`)
        .attr('preserveAspectRatio', 'xMinYMid')
        .call(this.resize, aspect);

      d3.select(window).on('resize.test', () => {
        this.resize(svg, aspect);
      });
    },
    resize(svg, aspect) {
      const container = d3.select(svg.node().parentNode);
      const w = parseInt(container.style('width'), 10);

      svg.attr('width', w);
      svg.attr('height', Math.round(w / aspect));
    },    
  },
};
</script>

<style lang="scss" scoped>
.tooltip-container {
  position: relative;
  text-align: center;
  color: black;
}

.centered {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-family: 'Poor Story', cursive;
  font-weight: 700;
  background-color: #ffffff;
  box-shadow: 0 2px 1px #b3b3b3;
  padding: 0 8px;
}

#chart {
  position: relative;
  border-top: 1px dashed #b3b3b3;
}

.viz-tooltip {
  max-width: 300px;
  position: absolute;
  background-color: #fff534 !important;
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    position: unset;
    max-width: 250px;
    display: block;
    margin: 0 auto;
    position: relative;
  }  
}

.sex-tape {
  cursor: pointer;
}

div .v-input {
  width: 120px;
  display: inline-block;
  margin-left: 10px;
}

div .v-input >>> .v-input__slot{
  background-color: #ffd4c2;
  border-radius: 100px;
}

::v-deep .v-input__slot {
  box-shadow: none !important;
  margin-bottom: 0;
}

::v-deep .v-select__selection {
  font-size: 20px;
}
</style>

<style lang="scss">
text.sex-tape {
  font-size: 1.8rem;
  @media #{map-get($display-breakpoints, 'sm-and-down')} {
    font-size: 3rem;
  }
}
</style>