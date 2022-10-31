# Axios

## Axios 개요

✔ JavaScript의 HTTP 웹 통신을 위한 라이브러리  
✔ 확장 가능한 인터페이스와 쉽게 사용할 수 있는 비동기 통신 기능 제공

## Axios 기본구조

### Axios 사용해보기

```JavaScript
<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script>
  axios.get('요청할 URL')
    .then(성공하면 수행할 콜백함수)
    .catch(실패하면 수행할 콜백 함수)
</script>
```

✔ get, post 등 여러 method 사용 가능  
✔ **`then`**을 이용해서 성공하면 수행할 로직 작성  
✔ **`catch`**을 이용해서 실패하면 수행할 로직 작성

### 고양이 사진 api 가져오기 (Python)

```Python
import requests

print('고양이는 야옹')

cat_image_search_url = 'https://api.thecatapi.com/v1/images/search'
response = requests.get(cat_image_search_url)

if response.status_code == 200:
    print(response.json())
else:
    print('실패했다옹')

print('야옹야옹')
```

![image](https://user-images.githubusercontent.com/109324637/198167118-c3ffa2c8-2923-46bf-95a5-296bc30421c5.png)  
✔ 처리결과를 보면 동기식으로 처리 된다.

### 고양이 사진 api 가져오기 (JavaScript)

![image](https://user-images.githubusercontent.com/109324637/198168328-75a9ec4a-8cc5-4d54-8b29-7d0b3e032ba4.png)  
![image](https://user-images.githubusercontent.com/109324637/198167607-21969570-2e65-4f16-8679-05d083bc79dc.png)  
✔ 비동기식으로 처리 된다.
