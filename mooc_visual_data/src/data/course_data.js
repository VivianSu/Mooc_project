import Data1 from './0/city_user.js'
import Data2 from './0/college_user.js'
import Data3 from './0/words.js'
import Data4 from './1/city_user.js'
import Data5 from './1/college_user.js'
import Data6 from './1/words.js'
import Data7 from './2/city_user.js'
import Data8 from './2/school_user.js'
import Data9 from './2/word_time1.js'
import Data10 from './3/city_user.js'
import Data11 from './3/school_user.js'
import Data12 from './3/word_time1.js'
import Data13 from './4/city_user.js'
import Data14 from './4/school_user.js'
import Data15 from './4/word_time1.js'
import Data16 from './5/city_user.js'
import Data17 from './5/school_user.js'
import Data18 from './5/word_time1.js'
import Data19 from './6/city_user.js'
import Data20 from './6/school_user.js'
import Data21 from './6/word_time1.js'
import Data22 from './7/city_user.js'
import Data23 from './7/school_user.js'
import Data24 from './7/word_time1.js'
import Data25 from './8/city_user.js'
import Data26 from './8/school_user.js'
import Data27 from './8/word_time1.js'
import Data28 from './9/city_user.js'
import Data29 from './9/school_user.js'
import Data30 from './9/word_time1.js'
import Data31 from './10/city_user.js'
import Data32 from './10/school_user.js'
import Data33 from './10/word_time1.js'

const courses = []

courses.push({
  value: 0,
  label: '简明世界史',
  users: 81515,
  score: 4.5,
  collegeUsers: 5042,
  primaryCollege: '哈尔滨工业大学',
  primaryCity: '北京市',
  startAt: '2015-02',
  cityUser: Data1,
  collegeUser: Data2,
  words: Data3
})
courses.push({
  value: 1,
  label: 'Python语言程序设计',
  score: 4.3,
  users: 43422,
  collegeUsers: 5402,
  primaryCollege: '哈尔滨工业大学',
  primaryCity: '北京市',
  startAt: '2015-10',
  cityUser: Data4,
  collegeUser: Data5,
  words: Data6
})
courses.push({
  value: 2,
  label: '中国茶道',
  score: 4.7,
  users: 10482,
  collegeUsers: 785,
  primaryCollege: '济南大学',
  primaryCity: '北京市',
  startAt: '2017-09',
  cityUser: Data7,
  collegeUser: Data8,
  words: Data9
})
courses.push({
  value: 3,
  label: '人人爱设计',
  users: 5316,
  score: 4.5,
  collegeUsers: 399,
  primaryCollege: '山东大学',
  primaryCity: '北京市',
  startAt: '2017-09',
  cityUser: Data10,
  collegeUser: Data11,
  words: Data12
})
courses.push({
  value: 4,
  label: '化妆品赏析与应用',
  score: 4.7,
  users: 9166,
  collegeUsers: 829,
  primaryCollege: '四川大学',
  primaryCity: '北京市',
  startAt: '2017-09',
  cityUser: Data13,
  collegeUser: Data14,
  words: Data15
})
courses.push({
  value: 5,
  label: '唐诗经典',
  score: 4.8,
  users: 4969,
  collegeUsers: 507,
  primaryCollege: '西北工业大学',
  primaryCity: '北京市',
  startAt: '2017-09',
  cityUser: Data16,
  collegeUser: Data17,
  words: Data18
})
courses.push({
  value: 6,
  label: '国际交流英语',
  score: 4.7,
  users: 8283,
  collegeUsers: 1101,
  primaryCollege: '哈尔滨工业大学',
  primaryCity: '北京市',
  startAt: '2017-09',
  cityUser: Data19,
  collegeUser: Data20,
  words: Data21
})
courses.push({
  value: 7,
  label: '心理学与生活',
  score: 4.6,
  users: 11236,
  collegeUsers: 805,
  primaryCollege: '东南大学',
  primaryCity: '北京市',
  startAt: '2017-09',
  cityUser: Data22,
  collegeUser: Data23,
  words: Data24
})
courses.push({
  value: 8,
  label: '急救常识',
  score: 4.5,
  users: 4602,
  collegeUsers: 472,
  primaryCollege: '西南石油大学',
  primaryCity: '北京市',
  startAt: '2017-09',
  cityUser: Data25,
  collegeUser: Data26,
  words: Data27
})
courses.push({
  value: 9,
  label: '沟通心理学',
  score: 4.7,
  users: 13269,
  collegeUsers: 1116,
  primaryCollege: '哈尔滨工业大学',
  primaryCity: '北京市',
  startAt: '2017-09',
  cityUser: Data28,
  collegeUser: Data29,
  words: Data30
})
courses.push({
  value: 10,
  label: '现代礼仪',
  score: 4.5,
  users: 10902,
  collegeUsers: 899,
  primaryCollege: '哈尔滨工业大学',
  primaryCity: '北京市',
  startAt: '2017-09',
  cityUser: Data31,
  collegeUser: Data32,
  words: Data33
})

export default {
  getCourse (id) {
    return courses[id]
  },

  getCourses () {
    return courses
  }
}
