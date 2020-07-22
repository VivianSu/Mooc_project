<template>
  <div id="app">
    <div id="left">
      <div class="panel-top">
        <el-select v-model="course" filterable placeholder="请选择"
                   @change="courseChange">
          <el-option
            v-for="item in options"
            :key="item.value"
            :label="item.label"
            :value="item.value"
            width="100%">
          </el-option>
        </el-select>
        <hr>
        <course-info :course="courseData.getCourse(parseInt(this.$route.params.courseId))"></course-info>
      </div>
      <div class="panel-bottom">
        <course-detail :course="courseData.getCourse(parseInt(this.$route.params.courseId))"></course-detail>
      </div>
    </div>
    <div id="right">
      <div id="top-nav">
        <nav>
          <div @click="$router.push({ name: 'city_map' })"
               class="nav-item">
            <a
              :class="{'is-active': $route.name === 'city_map'}">用户分布
            </a>
          </div>
          <div @click="$router.push({ name: 'college_map' })"
               class="nav-item">
            <a
              :class="{'is-active': $route.name === 'college_map'}">高校用户分布
            </a>
          </div>
          <div @click="$router.push({ name: 'wordcloud' })"
               class="nav-item">
            <a
              :class="{'is-active': $route.name === 'wordcloud'}">讨论区关键词
            </a>
          </div>
        </nav>
      </div>
      <div id="main">
        <router-view></router-view>
      </div>
    </div>
  </div>
</template>

<script>
  import './china'
  /* eslint-disable */
  import CourseInfo from './components/course/CourseInfo.vue'
  import CourseDetail from './components/course/CourseDetail.vue'
  import courseData from './data/course_data'

  console.log(courseData.getCourses())

  export default {
    name: 'app',
    data () {
      return {
        options: courseData.getCourses(),
        course: 0,
        courseData: courseData
      }
    },
    watch: {
      '$route.params.courseId' (value) {
        console.log(value)
        this.course = parseInt(value || 0)
      }
    },
    methods: {
      courseChange (id) {
        this.$router.push({name: this.$route.name, params: {courseId: id}})
      }
    },
    components: {CourseInfo, CourseDetail}
  }
</script>

<style>
  html, body {
    background: #1B1B1B;
    padding: 0;
    margin: 0;
  }

  #app {
    display: flex;
  }

  #left .panel-top {
    background: white;
    /*display: flex;*/
    justify-items: center;
    text-align: center;
    width: 100%;
    height: 40vh;
    font-size: 1rem;
  }

  #left .panel-bottom {
    background: #078ACE;
    height: 60vh;
    color: white;
    font-size: .8rem;
  }

  #left {
    display: block;
    flex-grow: 0;
    flex-shrink: 0;
    flex-basis: 300px;
    background: white;
    height: 100vh;
    position: relative;
  }

  #right {
    display: block;
    flex-grow: 0;
    flex-shrink: 0;
    height: 100vh;
    width: calc(100vw - 300px);
    position: relative;
  }

  #top-nav {
    height: 60px;
    width: 100%;
    background: #181818;
  }

  #main {
    height: calc(100vh - 60px);
    /*width: 80vw;*/
  }

  hr {
    opacity: .4;
  }

  nav a {
    display: block;
    height: 60px;
    line-height: 60px;
    color: #a0a0a0;
    text-decoration: none;
    font-size: small;
    border-top: 2px solid transparent;
    margin: 0 10px;
    transition: all .3s;
  }

  nav .nav-item {
    display: inline-block;
    height: 60px;
    padding: 0 10px;
    text-align: center;
    transition: all .3s;
    cursor: pointer;
  }

  nav .nav-item:hover {
    background: #363636;
  }

  nav a.is-active {
    color: #078ACE;
    border-color: #078ACE;
  }

  nav {
    padding: 0 50px;
  }

  .el-select {
    /*width: 90%;*/
    margin: 20px 0 10px 0;
  }
</style>
