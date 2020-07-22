<template>
  <div style="margin-top:80px">
    <br>
    <div class="block">
      <h1 class="title">{{ (course.collegeUsers / course.users * 100).toFixed(1) }} %</h1>
      <h4 class="subtitle">高校 IP 占比</h4>
      <hr>
    </div>
    <div class="block">
      <h1 class="title">{{ course.primaryCollege }}</h1>
      <h4 class="subtitle">用户最多学校</h4>
      <hr>
    </div>
    <div class="block">
      <h1 class="title">{{ course.primaryCity }}</h1>
      <h4 class="subtitle">用户最多省市</h4>
      <hr>
    </div>
  </div>
</template>
<style scoped>
  .block {
    text-align: left;
    font-family: Helvetica Neue,Open Sans,Microsoft YaHei,\\5FAE\8F6F\96C5\9ED1,Hiragino Sans GB,SimSun,sans-serif;
    padding: 0 20px 0 20px;
    position: relative;
  }

  .block .title,
  .block .subtitle {
    font-size: 1em;
    padding: 8px 20px;
    display: inline-block;
    width: 80px;
    text-align: left;
    margin: 0;
  }

  .block .title {
    font-weight: bolder;
  }

  .block .subtitle {
    font-size: .8em;
    color: #48b6ee;
  }

  hr {
    border-color: white;
    opacity: .1;
  }
</style>
<script>
  //  import data from '../../data/area'

  export default {
    props: ['course'],
    mounted () {
//      const colleges = {}
//      data.map(city => {
//        colleges[city.name] = [city.longitude, city.latitude]
//      })
//      const anchor = document.createElement('a')
//      anchor.href = 'data:text/plain,' + JSON.stringify((colleges))
//      anchor.download = 'college.js'
//      anchor.click()
    }
  }
</script>