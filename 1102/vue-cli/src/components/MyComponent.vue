<!-- MyComponent.vue -->

<template>
  <div class="border">
    <h1>This is my Component</h1>
    <MyComponentItem
      static-props="Data from MyComponent"
      :dynamic-props="dynamicProps"
      @child-to-parent="parentGetEvent"
      @child-input="getDynamicData"
    />
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
  data: function () {
    return {
      dynamicProps: "It's in data",
    };
  },
  methods: {
    parentGetEvent: function (inputData) {
      console.log("event from child!");
      console.log(`get ${inputData} from child component`);
    },
    getDynamicData: function (inputData) {
      console.log(12);
      console.log(`get dynamic ${inputData} from child component`);
    },
  },
};
</script>

<style>
.border {
  border: solid 1px black;
}
</style>
