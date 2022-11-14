<template>
  <div id="app" class="vuetube-wrap">
    <div class="container">
      <div class="mt-3 d-flex justify-content-center">
        <h1 class="text-primary">SSAFY TUBE</h1>
        <section v-if="isSelectedVideo" class="mt-2">
          <div class="ratio ratio-16x9">
            <iframe :src="videoSrc" frameborder="0"></iframe>
          </div>
          <div>
            <h4>{{ videoTitle }}</h4>
          </div>
        </section>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";

import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

const URL = "https://www.googleapis.com/youtube/v3/search";
const API_KEY = "AIzaSyBrBjvk68qe3bKQEl8T7nyX7cBTvz7Ff3o";

export default {
  name: "App",
  created() {
    axios
      .get(
        // URL
        URL,
        // params
        {
          params: {
            key: API_KEY,
            type: "video",
            part: "snippet",
            q: "싸피",
          },
        }
      )
      .then((res) => {
        this.videos = res.data.items;
        this.selectedVideo = this.videos[0];
      })
      .catch((error) => {
        console.log(error);
      });
  },
  data() {
    return {
      videos: [],
      selectedVideo: [],
    };
  },
  computed: {
    videoSrc() {
      return `https://www.youtube.com/embed/${this.selectedVideo.id.videoId}`
    },
    videoTitle() {
      return _.unescape(this.selectedVideo.snippet.title)
    },
    isSelectedVideo() {
      return !!Object.keys(this.selectedVideo).length
    }
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
