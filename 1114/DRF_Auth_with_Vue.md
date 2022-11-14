# DRF Auth with Vue

### vue server 요청 정상 작동 여부 확인

![](assets/DRF_Auth_with_Vue.md/2022-11-14-16-20-52.png)

✔ 401 status code  
✔ 인증되지 않은 사용자이므로 조회 요청이 불가능!  

## SignUp Request

### SignUp Page

1. `views/SignUpView.vue`

```vue
// views/SignUpView.vue

<template>
  <div>
    <h1>Sign Up Page</h1>
    <form @submit.prevent="signUp">
      <label for="username">username : </label>
      <input type="text" id="username" v-model="username"><br>

      <label for="password1"> password : </label>
      <input type="password" id="password1" v-model="password1"><br>

      <label for="password2"> password confirmation : </label>
      <input type="password" id="password2" v-model="password2">
      
      <input type="submit" value="SignUp">
    </form>
  </div>
</template>

<script>
export default {
  name: 'SignUpView',
  data() {
    return{
      username: null,
      password1: null,
      password2: null,
    }
  },
  methods: {
  }
}
</script>
```

✔ Server에서 정의한 field명 확인
1. username
2. password1
3. password2

2. `router/index.js`

```javascript
// router/index.js

import SignUpView from '@/views/SignUpView'

Vue.use(VueRouter)

const routes = [
  ...
  {
    path: '/signup',
    name: 'SignUpView',
    component: SignUpView
  },
  ...
]
```

3. `src/App.vue`

```vue
// src/App.vue

<template>
  <div id="app">
    <nav>
      <router-link :to="{ name: 'ArticleView' }">Articles</router-link> | 
      <router-link :to="{ name: 'SignUpView' }">SignUpPage</router-link> | 
    </nav>
    <router-view/>
  </div>
</template>
```

4. 결과 확인

![](assets/DRF_Auth_with_Vue.md/2022-11-14-16-25-55.png)

### SignUp Request

✔ 회원가입을 완료 시 응답 받을 정보 Token을 store에서 관리할 수 있도록 actions를 활용하여 요처 후, state에 저장할 로직 작성
- 회원가입이나 로그인 후 얻을 수 있는 Toekn을 server의 구성방식에 따라 매 요청마다 요구할 수 있으므로, 다양한 컴포넌트에 쉽게 접근할 수 있도록 중앙 상태 저장소인 vuex에서 관리

1. `vies/SignUpView.vue`

```vue
// views/SignUpView.vue

<script>
export default {
  ...
  methods: {
    signUp() {
      const username = this.username
      const password1 = this.password1
      const password2 = this.password2

      const payload = {
        username: username,
        password1: password1,
        password2: password2,
      }

      this.$store.dispatch('signUp', payload)
    }
  }
}
</script>
```

✔ 사용자 입력 값을 하나의 객체 payload에 담아 전달  

2. `store/index.js`

```javascript
// store/index.js

actions: {
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
```

✔ payload가 가진 값 각각 할당  
✔ AJAX 요청으로 응답 받은 데이터는 다수의 컴포넌트에서 사용  
✔ state에 저장

3. `store/index.js`

```javascript
// store/index.js

export default new Vuex.Store({
  state: {
    articles: [],
    toekn: null,
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
  ...
})
```

✔ token을 저장할 위치 확인  
✔ mutations을 통해 state 변화  

4. 요청 결과 확인

![](assets/DRF_Auth_with_Vue.md/2022-11-14-16-43-47.png)

## 토큰 관리

✔ 게시물 전체 조회와 달리, 인증 요청의 응답으로 받은 Token을 매번 요청하기 힘들다.  
✔ localStorage에 Token 저장을 위해 `vuex-persistedstate` 활용

1. 설치

```shell
$ npm install vuex-persistedstate
```

2. `store/index.js`

```javascript
// store/index.js

import createPersistedState from 'vuex-persistedstate'


export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  ...
})
```

3. 결과 확인

![](assets/DRF_Auth_with_Vue.md/2022-11-14-16-49-06.png)

### [참고] User 인증 정보를 localStorage에 저장해도 되는가?

✔ 보안의 관점에서 안전한 방법은 아니다.  
✔ 따라서 vuex-persistedstate는 아래 2가지 방법을 제공한다.  
1. 쿠키 사용하여 관리
2. 로컬 저장소를 난독화 하여 관리

## Login Page

