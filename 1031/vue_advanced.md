# Vue Advanced

## Computed

✔ Vue instance 가 가진 option 중 하나  
✔ computed 객체에 정의된 함수를 **페이지가 최초로 렌더링 될 때 호출하여 계산**

- 계산 결과가 변하기 전까지 함수를 재호출 하는 것이 아닌 **계산된 값을 반환**

### method vs computed

```html
<body>
  <div id="app">
    <h1>data_01 : {{ number1 }}</h1>
    <h1>data_02 : {{ number2 }}</h1>
    <hr />
    <!-- method -->
    <h1>add_method : {{ add_method() }}</h1>
    <h1>add_method : {{ add_method() }}</h1>
    <h1>add_method : {{ add_method() }}</h1>
    <hr />
    <!-- computed -->
    <h1>add_computed : {{ add_computed }}</h1>
    <h1>add_computed : {{ add_computed }}</h1>
    <h1>add_computed : {{ add_computed }}</h1>
    <hr />
    <button v-on:click="dataChange">Change Data</button>
  </div>

  <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
  <script>
    const app = new Vue({
      el: "#app",
      data: {
        number1: 100,
        number2: 100,
      },
      computed: {
        add_computed: function () {
          console.log("computed 실행됨!");
          return this.number1 + this.number2;
        },
      },
      methods: {
        add_method: function () {
          console.log("method 실행됨!");
          return this.number1 + this.number2;
        },
        dataChange: function () {
          this.number1 = 200;
          this.number2 = 300;
        },
      },
    });
  </script>
</body>
```

![image](https://user-images.githubusercontent.com/109324637/199140039-d59ee4a5-038e-4760-b215-7288896df7f1.png)

✔ method

- 호출 될 때마다 함수를 실행
- 같은 결과여도 매번 새롭게 계산

✔ computed

- 함수의 종속 대상의 변화에 따라 계산 여부가 결정됨
- 종속 대상이 변하지 않으면 항상 저장(캐싱) 된 값을 반환

## watch

```html
<button @click="number++">+</button>
```

```html
<script>
  const app = new Vue({
    el: "#app",
    data: {
      number: 0,
    },
    watch: {
      number: function (val, oldVal) {
        console.log(val, oldVal);
      },
    },
  });
</script>
```

✔ **특정 데이터의 변화 감지**

1. watch 객체 정의
2. 감시할 대상 data 지정
3. data가 변할 시 실행 함수 정의

✔ 첫 번째 인자는 **변동 전** data  
✔ 두 번째 인자는 **변동 후** data

## filter

```html
  <body>
    <div id="app">
      <p>{{ numbers | getOddNums }}</p>
    </div>

    <script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
    <script>
      const app = new Vue({
        el: "#app",
        data: {
          numbers: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
        },
        filters: {
          getOddNums: function (nums) {
            const oddNums = nums.filter((num) => {
              return num % 2;
            });
            return oddNums;
          },
        },
      });
    </script>
  </body
```

✔ 자바스크립트 표현식 마지막에 `|`(파이프) 함께 추가  
✔ 이어서 사용(chaning) 가능
