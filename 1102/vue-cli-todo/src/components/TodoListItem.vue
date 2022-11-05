<template>
  <li>
    {{ todo.title }}
  </li>
</template>

<script>
export default {
  name: "TodoListItem",
  props: {
    todo: Object,
  },
};
</script>

<style></style>
