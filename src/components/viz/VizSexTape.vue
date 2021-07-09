<template>
<v-container inner>
  <div class="my-5">
    <p class="text--body-1 text-center">What's the title of 
      <v-select 
        item-text="name"
        item-value="value"
        v-model="defaultWhose"      
        :items="whose"
        @input="colorByWhose($event)" /> 
    sex's tape?</p>  
    <p class="my-3"><strong>Show by </strong>
      <v-chip
        v-for="(item) in filterlist"
        :key="item.id"
        class="ml-1 px-3 flat"
        @click="drawBars(item.id)">
        <abbr :title="item.description">{{ item.id }}</abbr>
      </v-chip>
    </p>
    <!-- Viz Starts here -->
    <div id="chart" class="my-4">
      <svg id="colorsSVG"/>
      <v-card
        v-show="tooltip.show"
        class="viz-tooltip"
        :style="{ top: `${tooltip.move.top}px`, left: `${tooltip.move.left}px` }"
      >
        <v-card-subtitle class="caption">
          <p class="mb-0 pb-0">{{ tooltip.name }}</p>
          <p class="mb-0 pb-0"><strong>Hex code:</strong> {{ tooltip.hex }}</p>
        </v-card-subtitle>
      </v-card>       
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
      innerWidth: 600,
      innerHeight: 180,
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
        .selectAll('rect.sex-tape')
        .data(d => d.value)
        .enter()
        .append('rect')
        .attr('class', 'sex-tape')        
        .attr('x', d => this.vizSettings.scale.x(+d.season))
        .attr('y', (d, i) => this.vizSettings.scale.y(d.startY) - i * 10)
        .attr('width', this.innerWidth / 10)
        .attr('transform', `translate(${(this.innerWidth / 6 - this.innerWidth / 9) / 2}, 0)`)
        .attr('height',  (d) => this.vizSettings.scale.y(d.startY) - this.vizSettings.scale.y(d.endY));
      
      this.colorByWhose('all');
      this.handleTooltip();      
    },
    colorByWhose(selected) {
      const selectedPerson = this.kebabCase(selected);
      const people = {
        Amy: 'red', 
        Jake: 'yellow',
        Holt: 'green',
        Boyle: 'purple'
      }
      d3.selectAll('rect.sex-tape')
        .attr('fill', d => people[d.whoseSexTape]);
      
      d3.selectAll('rect.sex-tape')
        .attr('opacity', d => {
          if (selectedPerson === 'all') {
            return 1
          } else {
            return this.kebabCase(d.whoseSexTape) === selectedPerson ? 1 : 0.1
          }
        });
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
#chart {
  position: relative;
  border-top: 1px dashed grey;
}

.viz-tooltip {
  width: 200px;
  // @media only screen and (max-width: 600px) {
  //   width: 160px;
  // }
  position: absolute;
  background-color: #fff;
  color: rgba(0,0,0,.7);
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