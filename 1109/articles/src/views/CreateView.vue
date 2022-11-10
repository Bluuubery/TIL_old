<template>
  <div>
    <h1>게시글 작성</h1>
    <form @submit.prevent="createArticle">
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
    <router-link :to="{ name: 'index' }">뒤로가기</router-link>
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
  methods: {
    createArticle() {
      const title = this.title
      const content = this.content
      const payload = {
        title, content
      }
      this.$store.dispatch('createArticle', payload)
      this.$router.push({ name: 'index' })
    }
  }
}
</script>

<style>

</style>