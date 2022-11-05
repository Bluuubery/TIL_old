<!-- MyComponentItem.vue -->

<template>
  <div>
    <h3>Child Component of MyComponent</h3>
    <p>{{ staticProps }}</p>
    <p>{{ dynamicProps }}</p>
    <button @click="childInput">클릭!</button>
    <input type="text" v-model="childInputData" />
  </div>
</template>

<script>
export default {
  name: "MyComponentItem",
  props: {
    staticProps: String,
    dynamicProps: String,
  },
  data: function () {
    return {
      childInputData: null,
    };
  },
  methods: {
    childToParent: function () {
      this.$emit("child-to-parent", "child data");
    },
    childInput: function () {
      this.$emit("child-input", this.childInputData);
    },
  },
};
</script>

<style></style>
