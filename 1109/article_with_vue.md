# Articles with Vue

## 사전 준비

```shell
$ vue create articles
$ cd articles
$ vue add vuex
$ vue add router
```

```vue
// App.vue

<template>
  <div id="app">
    <router-view/>
  </div>
</template>
```

## Index

1. state 정의

```javascript
// store/index.js

import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    article_id: 3,
    articles: [
      {
        id: 1,
        title: 'title1',
        content: 'content1',
        createdAt: new Date().getTime()
      },
      {
        id: 2,
        title: 'title2',
        content: 'content2',
        createdAt: new Date().getTime()
      },
    ]
  },
})
```

2. IndexView 컴포넌트 및 라우터 작성

```vue
// views/IndexView.vue

<template>
  <div>
    <h1>Articles</h1>
  </div>
</template>

<script>
export default {
  name: 'IndexView'
}
</script>

<style>

</style>
```

```javascript
// router/index.js

import IndexView from '../views/IndexView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'IndexView',
    component: IndexView
  },
]  
```

3. state 에서 불러온 articles 출력

```vue
// views/IndexView.vue

<template>
  <div>
    <h1>Articles</h1>
    {{ articles }}
  </div>
</template>

<script>
export default {
  name: 'IndexView',
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
}
</script>
```

![](assets/article_with_vue.md/2022-11-09-16-20-24.png)

4. ArticleItem 컴포넌트 작성

```vue
// components/ArticleItem.vue

<template>
  <div>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
}
</script>
```

5. IndexView 컴포넌트에서 ArticleItem 컴포넌트 등록 밑 props 데이터 전달
   
```vue
// views/IndexView.vue

<template>
  <div>
    <h1>Articles</h1>
    <ArticleItem 
      v-for="article in articles"
      :key="article.id"
      :article=article
    />
  </div>
</template>

<script>
import ArticleItem from '../components/ArticleItem.vue'

export default {
  name: 'IndexView',
  components: {
    ArticleItem
  },
  computed: {
    articles() {
      return this.$store.state.articles
    }
  },
}
</script>
```

6. props 데이터 선언 및 게시글 출력

```vue
// components/ArticleItem.vue

<template>
  <div>
    <p>글 번호: {{ article.id }}</p>
    <p>글 제목: {{ article.title }}</p>
    <hr>
  </div>
</template>

<script>
export default {
  name: 'ArticleItem',
  props: {
    article: Object
  }
}
</script>
```

7. 결과 확인
   ![](assets/article_with_vue.md/2022-11-09-16-26-48.png)

## Create

1. CreateView 컴포넌트 및 라우터 작성

```vue
// views/CreateView.vue

<template>
  <div>
    <h1>게시글 작성</h1>
  </div>
</template>

<script>
export default {
  name: "CreateView"
}
</script>
```

```javascript
// router/index.js

const routes = [
  ...
  {
    path: '/create',
    name: 'create',
    component: CreateView
  },
]
```

2. Form 생성 및 데이터 정의

```vue
<template>
  <div>
    <h1>게시글 작성</h1>
    <form>
      <label for="title">제목: </label>
      <input id="title" type="text" v-model="title"> 
      <br>
      <label for="content">내용: </label>
      <textarea
        id="content" cols="30" rows="10"
        v-model="content"
      ></textarea>
      <input type="submit">
    </form>
  </div>
</template>

<script>
export default {
  name: "CreateView",
  data() {
    return {
      title: null,
      content: null,
    }
  },
}
</script>
```

3. submit 이벤트 동작 취소하기

```vue
// views/CreateView.vue

<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
    ...
    </form>
  </div>
</template>
```

✔ `v-on: {event}.prevent` 활용하여 submit 이벤트 동작 취소  

4. actions에 여러 데이터를 넘길 때 하나의 object로 만들어서 전달

```vue
// views/CreateView.vue

<script>
export default {
  name: "CreateView",
  data() {
    return {
      title: null,
      content: null,
    }
  },
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const payload = {
        title, content
      }
      this.$store.dispatch('createArticle', payload)
    }
  }
}
</script>
```

5. actions에서 넘어온 데이터를 활용하여 article 생성 후 mutations 호출
  
```javascript
// store/index.js

actions: {
    createArticle(context, payload) {
      const article = {
        id: context.state.article_id,
        title: payload.title,
        content: payload.content,
        createdAt: new Date().getTime()
      }
      context.commit('CREATE_ARTICLE', article)
    }
  },
```

6. mutations에서는 전달된 article 객체를 사용해 게시글 작성

```javascript
  mutations: {
    CREATE_ARTICLE(state, article) {
      state.articles.push(article)
      state.article_id = state.article_id + 1
    }
  },
```

7. 뒤로가기 링크 추가

```vue
// views/CreateView.vue

<template>
  <div>
    <h1>게시글 작성</h1>
    ...
    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
  </div>
</template>
```

8. 게시글 생성 후 index 페이지로 이동하도록 하는 네비게이터 작성

```vue
// views/CreateView.vue

  methods: {
    createArticle() {
      ...
      this.$store.dispatch('createArticle', payload)
      this.$router.push({ name: 'index' })
    }
  }
```

9. IndexView 컴포넌트에 게시글 작성 페이지로 이동하는 링크 추가

```vue
// views/IndexView.vue

<template>
  <div>
    <h1>Articles</h1>
    <router-link :to="{name:'create'}">게시글 작성</router-link>
    <ArticleItem 
      v-for="article in articles"
      :key="article.id"
      :article=article
    />
  </div>
</template>
```

## Detail

1. DetailView 컴포넌트 및 라우터 작성

```vue
// views/DetailView.vue

<template>
  <div>
    <h1>Detail</h1>
  </div>
</template>

<script>
export default {
  name: "DetailView",
};
</script>
```

```javascript
// router/index.js
import DetailView from '../views/DetailView.vue'

...

const routes = [
  ...
  {
    path: '/:id',
    name: 'detail',
    component: DetailView
  },
]

```

2. article 정의 및 state에서 articles 가져오기

```vue
// views/DetailView.vue

<script>
export default {
  name: "DetailView",
  data() {
    return {
      article: null
      }
  },
  computed: {
    articles() {
      return this.$store.state.articles;
    },
  },
}
</script>
```

3. articles에서 동적인자를 통해 받은 id에 해당하는 article 가져오기

```vue
// views/DetailView.vue

<script>
  ...
  methods: {
    getArticleById() {
      const id = this.$route.params.id;
      for (const article of this.articles) {
        // url은 문자로 들어오므로 형변환해서 비교
        if (article.id === Number(id)) {
          this.article = article;
          break;
        }
      }
    },
  },
</script>
```
✔ 동적 인자를 통해 받은 id는 str이므로 형변환을 통해서 비교해준다.  

4. article 출력

```vue
// views/DetailView.vue

<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호: {{ article.id }}</p>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <p>작성시간: {{ article.createdAt }}</p>
  </div>
</template>
```

5. created lifecycle hook을 통해 인스턴스가 생성되었을 때 article을 가져오는 함수 호출

```vue
// views/DetailView.vue

<script>
...
  methods: {
    getArticleById() {
      const id = this.$route.params.id;
      for (const article of this.articles) {
        // url은 문자로 들어오므로 형변환해서 비교
        if (article.id === Number(id)) {
          this.article = article;
          break;
        }
      }
    },
  },
  created() {
    this.getArticleById(this.$route.params.id)
  },
</script>
```

#### [참고] Optional Chaining

![](assets/article_with_vue.md/2022-11-10-10-02-41.png)

✔ Optional Chaining(`?.`) 앞의 평가 대상이 undefined나 null 이면 에러가 발생하지 않고 undefined를 반환한다.

6. optional chaining(`?.`)을 통해 article 객체가 있을 때만 출력되도록 수정
   
```vue
// views/DetailView.vue

<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호: {{ article?.id }}</p>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <p>작성시간: {{ article.createdAt }}</p>
  </div>
</template>
```

7. 로컬 시간으로 변환해주는 computed 값 작성 및 출력

```vue
// views/DetailView.vue

<script>
export default {
  ...
  computed: {
    ...
    articleCreatedAt() {
      const article = this.article
      const createdAt = new Date(article?.createdAt).toLocaleString()
      return createdAt
    }
  },
}
```

```vue
// views/DetailView.vue

<template>
  <div>
    <h1>Detail</h1>
    <p>글 번호: {{ article?.id }}</p>
    <p>제목: {{ article.title }}</p>
    <p>내용: {{ article.content }}</p>
    <!-- <p>작성시간: {{ article.createdAt }}</p> -->
    <p>작성시간: {{ articleCreatedAt }}</p>
  </div>
</template>
```

8. DetailView 컴포넌트에 뒤로가기 링크 추가

```vue
// views/DetailView.vue

<template>
  <div>
  ...
    <router-link :to="{ name:index }">뒤로가기</router-link>
  </div>
</template>
```

9. 각 게시글을 클릭하면 detail 페이지로 이동하도록 ArticleItem에 이벤트 추가

```vue
// components/ArticleItem.vue

<template>
  <div @click="goDetail(article.id)">
    <p>글 번호: {{ article.id }}</p>
    <p>글 제목: {{ article.title }}</p>
    <hr />
  </div>
</template>

<script>
export default {
  name: "ArticleItem",
  props: {
    article: Object,
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name:'detail', params:{id} })
    }
  },
};
</script>
```

## Delete

1. DetailView 컴포넌트에 삭제 버튼 만들고, mutations 호출
   
```vue
// views.DetailView.vue

<template>
  <div>
  ...
    <button @click="deleteArticle">삭제</button>
    <br />
    <router-link :to="{ name: index }">뒤로가기</router-link>
  </div>
</template>

<script>
export default {
  ...
  methods: {
    ...
    deleteArticle() {
      this.$store.commit('DELETE_ARTICLE', this.article.id)
    }
  },
  ...
};
</script>
```

2. mutations에서 id에 해당하는 게시글 지우기

```javascript
// store/index.js

...
  mutations: {
    ...
    DELETE_ARTICLE(state, id) {
      state.articles = state.articles.filter((article) => {
        return !(article.id === id)
      })
    }
  },
...
```

3. 삭제 후 index 페이지로 이동하도록 네비게이션 작성

```vue
// views/DetailView.vue

<script>
export default {
  ...
  methods: {
    ...
    deleteArticle() {
      this.$store.commit('DELETE_ARTICLE', this.article.id)
      this.$router.push({ name:'index' })
    }
  },
  ...
};
</script>
```

## 404 Not Found

1. NotFound404 컴포넌트 및 라우터 작성

```vue
// views/NotFound404.vue

<template>
  <div>
    <h1>404 Not Found</h1>
  </div>
</template>

<script>
export default {
  name: 'NotFound404'
}
</script>
```
```javascript
// router/index.js

const routes = [
  ...
  {
    path: '/404-not-found',
    name: 'NotFound404',
    component: NotFound404
  },
  {
    path: '/:id',
    name: 'detail',
    component: DetailView
  },
]
```
✔ Detail에 대한 router보다 위에 등록해줘야 한다.  
✔ /404로 등록하면 404번째 게시글과 혼동될 수 있다.  

2. DetailView 컴포넌트에 id에 해당하는 article이 없으면 404 페이지로 이동

```vue
// views/DetailView.vue

<script>
export default {
  ...
  methods: {
    getArticleById() {
      const id = this.$route.params.id;
      for (const article of this.articles) {
        // url은 문자로 들어오므로 형변환해서 비교
        if (article.id === Number(id)) {
          this.article = article;
          break;
        }
        if (!this.article) {
          this.$router.push({ name:'NotFound404' })
        }
      }
    },
    ...
  },
  ...
}
</script>
```

3. 요청한 리소스가 존재하지 않는 경우 없는 id가 아닌 전혀 다른 요청에 대비하여 404page로 redirect 시키기

```javascript
// router/index.js

const routes = [
  ...
  {
    path: '*',
    redirect: { name: 'NotFound404' }
  }
]
```

✔ 최하단에 작성  
✔ `$router.push`와 마찬가지로 name을 이용하여 이동할 수 있다.