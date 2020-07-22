<template>
  <div>
    <br>
    <div class="block">
      <h1 class="title">{{ course.score }}</h1>
      <h4 class="subtitle">课程评分</h4>
      <hr>
    </div>
    <div class="block">
      <h1 class="title">{{ course.users }}</h1>
      <h4 class="subtitle">独立IP数</h4>
      <hr>
    </div>
    <div class="block">
      <h1 class="title">{{ course.collegeUsers }}</h1>
      <h4 class="subtitle">高校用户</h4>
      <hr>
    </div>
    <div class="block">
      <h1 class="title">{{ course.startAt }}</h1>
      <h4 class="subtitle">开课时间</h4>
      <hr>
    </div>
  </div>
</template>
<style scoped>
  .block {
    text-align: left;
    font-family: Helvetica Neue,Open Sans,Microsoft YaHei,\\5FAE\8F6F\96C5\9ED1,Hiragino Sans GB,SimSun,sans-serif;
    padding: 0 10px 0 10px;
  }

  .block .title,
  .block .subtitle {
    font-size: 1.5em;
    padding: 0 20px;
    display: block;
    text-align: left;
    margin: 0;
    color: #333;

  }

  .block .title {
    font-weight: bolder;
  }

  .block .subtitle {
    font-size: 1em;

  }
</style>
<script>
  export default {
    props: ['course'],
    mounted () {}
  }
</script>