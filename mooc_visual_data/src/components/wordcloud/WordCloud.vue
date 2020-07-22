<template>
  <div class="wrapper" v-show="wordsCloud">
    <div class="slider" :style="{transform: 'translateX(' + sliderOffset +')'}">
      <div>
        <el-slider
          v-if="words && words.length >= 2"
          v-model="step"
          :step="1"
          :min="1"
          :max="totalStep"
          :format-tooltip="formatTooltip"
          :style="{width: sliderItemWidth * (totalStep - 1) + 'px'}"
          show-stops>
        </el-slider>
      </div>
      <div class="dates">
        <div class="date"
             v-for="i in totalStep"
             :style="{width: sliderItemWidth + 'px'}"
             @click="step = i - 1"><span>{{ words[i - 1].time }}</span></div>
      </div>
    </div>

    <div id="vis"></div>

    <div class="filter">
      <div class="el-input el-input--mini el-input-group el-input-group--prepend">
        <div tabindex="0" class="el-input-group__prepend">关键词排除</div>
        <input v-model.lazy="wordsFilter"
               autocomplete="off"
               size="mini"
               type="text"
               class="el-input__inner"><!---->
        <!----><!---->
      </div>
    </div>

    <div class="detail" v-if="wordsCloud.length > 1">
      <h5>Top 20</h5>
      <el-tag type="info" v-for="i in Math.min(wordsCloud.length - 1, 20)">
        {{ wordsCloud[i][0] }} : {{ wordsCloud[i][1] }}
      </el-tag>
    </div>
  </div>
</template>
<style>
  .wrapper {
    overflow: hidden;
  }

  .slider {
    padding: 0 50px;
    color: #484848;
    font-family: 'Lucida Console', Monaco, monospace;;
    white-space: nowrap;
    transition: all .3s;
    /*position: relative;*/
  }

  .slider .dates {
    margin-top: -15px;
    margin-left: -30px;
    /*padding-top: 10px;*/
  }

  .slider .date {
    text-align: center;
    display: inline-block;
    font-size: smaller;
    cursor: pointer;
    height: 50px;
    padding-top: 20px;
  }

  .filter {
    text-align: center;
  }

  .filter .el-input .el-input__inner,
  .filter .el-input-group__prepend {
    width: 70vw;
    background: transparent;
    border: 1px solid #4a4b4e;
  }

  .slider span {
    display: block;
    text-decoration: none;
    font-style: normal;
    transform: rotateZ(-30deg);
    /*margin: -10px 0 0 -20px;*/
  }

  .slider span:first-child {
    /*margin-left: -30px;*/
  }

  #vis {
    text-align: center;
    height: 500px;
    width: calc(100% - 100px);
    margin: 50px;
  }

  .el-slider__runway {
    background-color: #484848;
  }

  .el-slider__bar {

  }

  .detail {
    color: #494949;
    padding: 0 20px;
    text-align: center;
  }
</style>
<script>
  import cloud from 'd3-cloud'
  import courseData from '../../data/course_data'

  const d3 = window.d3

  export default {
    data () {
      return {
        sliderItemWidth: 75,
        step: 1,
        totalStep: 1,
        words: [],
        wordsFilter: '为,一个,都,啊,吗,就,这个,后,应该,能,知道,和,在,不,是,一下,这样,中,呢,们,有,不是,以下,而已,=,+,-',
        wordcloud: null
      }
    },
    watch: {
      '$route.params.courseId' () {
        this.step = 1
        this.totalStep = courseData.getCourse(this.$route.params.courseId).words.length
        this.words = courseData.getCourse(this.$route.params.courseId).words || {time: '', words: []}
      }
    },
    mounted () {
      this.totalStep = courseData.getCourse(this.$route.params.courseId).words.length
      this.words = courseData.getCourse(this.$route.params.courseId).words || {time: '', words: []}
      let vis = document.getElementById('vis')
      let width = vis.offsetWidth // vis.width
      let height = vis.offsetHeight // vis.height

      let svg = d3.select('#vis')
        .append('svg')
        .attr('width', width)
        .attr('height', height)

      let background = svg.append('g')
      vis = svg.append('g').attr('transform', 'translate(' + [width >> 1, height >> 1] + ')')

      this.wordcloud = cloud()
        .timeInterval(10)
        .size([width, height])
        .text(function (t) {
          return t.key
        })
        .font('Impact')
        .fontSize(function (d) {
          return d.size
        })
        .rotate(function () {
          return 0
        })
        .padding(5)
        .random(function () {
          return 0.5
        })
        .on('end', draw)

      function draw (words, e) {
        let n = vis.selectAll('text').data(words, function (t) {
          return t.text
        })

        let scale = e ? Math.min(width / Math.abs(e[1].x - width / 2), width / Math.abs(e[0].x - width / 2), height / Math.abs(e[1].y - height / 2), height / Math.abs(e[0].y - height / 2)) / 2 : 1

        n.transition()
          .duration(1e3)
          .attr('transform', function (t) {
            return 'translate(' + [t.x, t.y] + ')rotate(' + t.rotate + ')'
          })
          .style('font-size', function (t) {
            return t.size + 'px'
          })

        n.enter()
          .append('text')
          .attr('text-anchor', 'middle')
          .attr('transform', function (t) {
            return 'translate(' + [t.x, t.y] + ')rotate(' + t.rotate + ')'
          })
          .style('font-size', '1px')
          .transition()
          .duration(1e3)
          .style('font-size', function (t) {
            return t.size + 'px'
          })

        n.style('font-family', function (t) {
          return t.font
        })
          .style('fill', function (t) {
            if (t.frequency > 100) return '#ff4964'
            if (t.frequency > 5) return '#0F97E1'
            if (t.frequency < 3) return '#555555'
            return '#c2c2c2'
          })
          .text(function (t) {
            return t.text
          })

        let a = background.append('g')
          .attr('transform', vis.attr('transform'))

        let r = a.node()
        n.exit()
          .each(function () {
            r.appendChild(this)
          })

        a.transition()
          .duration(1e3)
          .style('opacity', 1e-6)
          .remove()
        vis.transition()
          .delay(1e3)
          .duration(750)
          .attr('transform', 'translate(' + [width >> 1, height >> 1] + ')scale(' + scale + ')')
      }
    },
    computed: {
      wordsCloud () {
        this.words = courseData.getCourse(this.$route.params.courseId).words || {time: '', words: []}
        let words = (this.words && this.words[this.step - 1]) || {time: '', words: []}

        const cloudWords = []
        for (let i = 0; (i < words.words.length) && (cloudWords.length < 100); i++) {
          if (this.filter[words.words[i][0]]) {
            continue
          }
          cloudWords.push(words.words[i])
        }

        this.wordcloud && this.wordcloud.stop().words(cloudWords.map(function (t) {
          return {
            key: t[0],
            text: t[0],
            size: t[1] / 2 + 15,
            frequency: t[1]
          }
        })).start()
        return cloudWords
      },
      sliderOffset () {
        const totalWidth = this.getWindowSize().width - 300 - 100
        const prePage = totalWidth / this.sliderItemWidth / 2
        const offset = ~~((this.step - 1) / prePage)
        return '-' + (offset * (totalWidth) / 2 - (offset > 0 ? this.sliderItemWidth : 0)) + 'px'
      },
      filter () {
        const ret = {}
        const arr = this.wordsFilter.split(',')
        arr.length && arr.forEach((word) => {
          ret[word] = true
        })
        return ret
      }
    },
    methods: {
      formatTooltip (val) {
        return val + ' 月'
      },
      getWindowSize () {
        let w = window
        let d = document
        let e = d.documentElement
        let g = d.getElementsByTagName('body')[0]
        let x = w.innerWidth || e.clientWidth || g.clientWidth
        let y = w.innerHeight || e.clientHeight || g.clientHeight
        return {height: y, width: x}
      }
    }
  }
</script>
