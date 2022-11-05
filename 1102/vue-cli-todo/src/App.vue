<template>
  <div id="app">
    <TodoList :todos="todos" />
    <TodoForm />
  </div>
</template>

<script>
import TodoForm from "@/components/TodoForm";
import TodoList from "@/components/TodoList";

export default {
  name: "App",
  components: {
    TodoForm,
    TodoList,
  },
  data: function () {
    return {
      todos: [
        {
          title: "할 일",
        },
      ],
    };
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
