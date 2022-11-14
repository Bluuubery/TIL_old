import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import createPersistedState from 'vuex-persistedstate'

const API_URL = 'http://127.0.0.1:8000'

Vue.use(Vuex)



export default new Vuex.Store({
  plugins: [
    createPersistedState(), 
  ],
  state: {
    articles: [],
    token: null,
  },
  getters: {
  },
  mutations: {
    GET_ARTICLES(state, articles) {
      state.articles=articles
    },
    SIGN_UP(state, token){
      state.token = token
    }
  },
  actions: {
    getArticles(context) {
      axios({
        method: 'get',
        url: `${API_URL}/api/v1/articles/`
      })
        .then((res) => {
          // console.log(res, context)
          context.commit('GET_ARTICLES', res.data)
        })
        .catch((err) => {
          console.log(err)
        })
    },
    signUp(context, payload) {
      axios({
        method: 'post',
        url: `${API_URL}/accounts/signup/`,
        data: {
          // 축약형 표현
          // username,
          // password1,
          // password2,
          username: payload.username,
          password1: payload.password1,
          password2: payload.password2,
        }
      })
        .then((res) => {
          console.log(res)
          context.commit('SIGN_UP', res.data.key)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  modules: {
  }
})
