<template>
  <div>
    <div id="map-data"></div>
  </div>
</template>
<style>
  #map-data {
    width: 80vw;
    height: calc(100vh - 80px);
    overflow: hidden;
  }
</style>
<script>
  /* eslint-disable */
  import cityData from './city_coord'
  import courseData from '../../data/course_data'

  export default { 
    mounted () {
      this.init()
    },
    watch: {
      '$route.params.courseId' () {
        this.init()
      }
    },
    methods: {
      init () {
        let geoCoordMap = cityData
        let data = courseData.getCourse(this.$route.params.courseId).cityUser

        const myChart = window.echarts.init(document.getElementById('map-data'))

        let convertData = function (data) {
          let res = []
          for (let i = 0; i < data.length; i++) {
            let geoCoord = geoCoordMap[data[i].name]
            if (geoCoord) {
              res.push({
                name: data[i].name,
                value: geoCoord.concat(data[i].value)
              })
            }
          }
          return res
        }

        let convertedData = [
          convertData(data),
          convertData(data.sort(function (a, b) {
            return b.value - a.value
          }).slice(0, 6))
        ]

        const option = {
          backgroundColor: '#1B1B1B',
          animation: true,
          animationDuration: 1000,
          animationEasing: 'cubicInOut',
          animationDurationUpdate: 1000,
          animationEasingUpdate: 'cubicInOut',
          title: [
            {
              text: '全国用户分布',
              left: 'center',
              textStyle: {
                color: '#fff'
              }
            },
            {
              id: 'statistic',
              right: 120,
              top: 40,
              width: 100,
              textStyle: {
                color: '#fff',
                fontSize: 16
              }
            }
          ],
          toolbox: {
            iconStyle: {
              normal: {
                borderColor: '#fff'
              },
              emphasis: {
                borderColor: '#b1e4ff'
              }
            }
          },
          brush: {
            outOfBrush: {
              color: 'white'
            },
            brushStyle: {
              borderWidth: 2,
              color: 'rgba(0,0,0,0.2)',
              borderColor: 'rgba(0,0,0,0.5)',
            },
            seriesIndex: [0, 1],
            throttleType: 'debounce',
            throttleDelay: 300,
            geoIndex: 0
          },
          geo: {
            map: 'china',
            left: '10',
            right: '35%',
            center: [116.1172733, 35.9385466],
            zoom: 1.5,
            label: {
              emphasis: {
                show: false
              }
            },
            roam: true,
            itemStyle: {
              normal: {
                areaColor: '#444444',
                borderColor: '#1b1b1b'
              },
              emphasis: {
                areaColor: '#2a333d'
              }
            }
          },
          tooltip: {
            trigger: 'item'
          },
          grid: {
            right: 40,
            top: 100,
            bottom: 40,
            width: '30%'
          },
          xAxis: {
            type: 'value',
            scale: true,
            position: 'top',
            boundaryGap: false,
            splitLine: {show: false},
            axisLine: {show: false},
            axisTick: {show: false},
            axisLabel: {margin: 2, textStyle: {color: '#aaa'}},
          },
          yAxis: {
            type: 'category',
            name: 'TOP 20',
            nameGap: 16,
            axisLine: {show: false, lineStyle: {color: '#ddd'}},
            axisTick: {show: false, lineStyle: {color: '#ddd'}},
            axisLabel: {interval: 0, textStyle: {color: '#ddd'}},
            data: []
          },
          series: [
            {
              name: '人数',
              type: 'scatter',
              coordinateSystem: 'geo',
              data: convertedData[0],
              symbolSize: function (val) {
//              console.log(val[2])
                return Math.max(Math.sqrt(val[2]), 4)
              },
              label: {
                normal: {
                  formatter: '{b}',
                  position: 'right',
                  show: false
                },
                emphasis: {
                  show: true
                }
              },
              itemStyle: {
                normal: {
                  color: '#008AD0'
                }
              }
            },
            {
              name: 'Top 5',
              type: 'effectScatter',
              coordinateSystem: 'geo',
              data: convertedData[1],
              symbolSize: function (val) {
                return Math.max(Math.sqrt(val[2]), 4)
              },
              showEffectOn: 'emphasis',
              rippleEffect: {
                brushType: 'stroke'
              },
              hoverAnimation: true,
              label: {
                normal: {
                  formatter: '{b}',
                  position: 'right',
                  show: true
                }
              },
              itemStyle: {
                normal: {
                  color: '#008AD0',
                  shadowBlur: 10,
                  shadowColor: '#333'
                }
              },
              zlevel: 1
            },
            {
              id: 'bar',
              zlevel: 2,
              type: 'bar',
              symbol: 'none',
              itemStyle: {
                normal: {
                  color: '#008AD0'
                }
              },
              data: []
            }
          ]
        }

        myChart.on('brushselected', renderBrushed)
        myChart.setOption(option)

        setTimeout(function () {
          myChart.dispatchAction({
            type: 'brush'
          })
        }, 0)

        function renderBrushed (params) {
          let mainSeries = params.batch[0].selected[0]

          let selectedItems = []
          let categoryData = []
          let barData = []
          let maxBar = 30
          let sum = 0

          if (mainSeries.dataIndex.length) {
            for (let i = 0; i < mainSeries.dataIndex.length; i++) {
              let rawIndex = mainSeries.dataIndex[i]
              let dataItem = convertedData[0][rawIndex]
              sum += dataItem.value[2]
              selectedItems.push(dataItem)
            }
          } else {
            for (let i = 0; i < convertedData[0].length; i++) {
              let dataItem = convertedData[0][i]
              sum += dataItem.value[2]
              selectedItems.push(dataItem)
            }
          }

          selectedItems = _.sortBy(selectedItems, [(item) => {
            return -1 * item.value[2] || 0
          }])

          for (let i = Math.min(selectedItems.length, maxBar) - 1; i >= 0; i--) {
            categoryData.push(selectedItems[i].name)
            barData.push(selectedItems[i].value[2])
          }

          this.setOption({
            yAxis: {
              data: categoryData
            },
            xAxis: {
              axisLabel: {show: !!sum}
            },
            title: {
              id: 'statistic',
              text: sum ? '总计: ' + sum : ''
            },
            series: {
              id: 'bar',
              data: barData
            }
          })
        }
      }
    }
  }
</script>
