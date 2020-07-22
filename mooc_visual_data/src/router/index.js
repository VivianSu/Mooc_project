import Vue from 'vue'
import Router from 'vue-router'
import CityMap from '@/components/citymap/CityMap.vue'
import WordCloud from '@/components/wordcloud/WordCloud.vue'
import CollegeMap from '@/components/collegemap/CollegeMap.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      redirect: '/0/city_map'
    },
    {
      path: '/:courseId/city_map',
      name: 'city_map',
      component: CityMap
    },
    {
      path: '/:courseId/college_map',
      name: 'college_map',
      component: CollegeMap
    },

    {
      path: '/:courseId/wordcloud',
      name: 'wordcloud',
      component: WordCloud
    }
  ]
})
