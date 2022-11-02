// MyComponent.vue

<template>
  <div class="border">
    <h1>This is my Component</h1>
    <!-- 3. 보여주기 -->
    <MyComponentItem />
  </div>
</template>

<script>
// 1. 불러오기
import MyComponentItem from "@/components/MyComponentItem";

export default {
  name: "MyComponet",
  // 2. 등록하기
  components: {
    MyComponentItem,
  },
};
</script>

<style>
.border {
  border: solid 1px black;
}
</style>
