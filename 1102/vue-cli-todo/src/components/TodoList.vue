<template>
  <div>
    <ul v-for="(todo, index) in todos" :key="index">
      <TodoListItem :todo="todo" />
    </ul>
  </div>
</template>

<script>
import TodoListItem from "./TodoListItem.vue";

export default {
  name: "TodoList",
  components: {
    TodoListItem,
  },
  props: {
    todos: Array,
  },
};
</script>

<style></style>
