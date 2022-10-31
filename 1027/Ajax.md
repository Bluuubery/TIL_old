# AJAX

## AJAX 개요

✔ Asynchronous Javascript And XML (비동기 통신 웹 개발 기술)  
✔ 비동기 통신을 이용해 화면 전체를 새로고침 하지 않고도 서버 요청을 보내고, 데이터를 받아 화면의 일부분만 업데이트 하는 기능

### AJAX의 특징

1. 페이지 새로 고침 없이 서버에 요청
2. 서버로부터 응답(데이터)를 받아 작업을 수행

## AJAX를 이용해 Django follow 기능 구현하기

### 사전준비

1. 템플릿에 script 코드 작성을 위한 block tag 영역 작성

```django
<!-- base.html -->

<body>
  ...
  {% block script %}
  {% endblock script %}
</body>
```

2. axios CDN 작성

```django
<!-- accounts/profile.html -->

{% block script %}
  <script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
  <script>
  </script>
{% endblock script %}
```

3. id 속성 지정 및 선택, 불필요한 action과 method 삭제 (요청은 axios로 대체된다.)

```html
<!-- accounts/profile.html -->

<form id="follow-form">...</form>
```

```html
<!-- accounts/profile.html -->

<script>
  const form = document.querySelector("#follow-form");
</script>
```

4. form 요소에 이벤트 핸들러 작성 및 submit 이벤트 취소

```html
<!-- accounts/profile.html -->

<script>
  const form = document.querySelector("#follow-form");

  form.addEventListener("submit", function (event) {
    event.preventDefault();
  });
</script>
```

5. axios 요청 준비

```html
<!-- accounts/profile.html -->

<script>
  const form = document.querySelector('#follow-form')

  form.addEventListener('submit', function (event) {
    event.preventDefault()
    axios({
      method: 'post',
      url: `/accounts/${???}/follow/`,
    })
  })
</script>
```

### 1. url에 작성할 user pk 작성

1. url에 작성할 user pk 가져오기 (HTML > JavaScript)

```html
<!-- accounts/profile.html -->

<form id="follow-form" data-user-id="{{ person.pk }}">...</form>
```

```html
<!-- accounts/profile.html -->

<script>
  const form = document.querySelector("#follow-form");

  form.addEventListener("submit", function (event) {
    event.preventDefault();

    const userId = event.target.dataset.userId;
  });
</script>
```

2. url 작성 마치기

```html
<!-- accounts/profile.html -->

<script>
  const form = document.querySelector("#follow-form");

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    axios({
      method: "post",
      url: `/accounts/${userId}/follow/`,
    });
  });
</script>
```

### `data-* attributes`

✔ 사용자 지정 데이터 특성을 만들어 임의의 데이터를 HTML과 DOM 사이에서 교환할 수 있는 방법  
✔ 사용 예시

```html
<div data-my-id="my-data"></div>
<script>
  const myId = event.targe.dataset.myId;
</script>
```

✔ `data-test-value`라는 이름의 특성을 지정했다면 JavaScript에서는 `element.dataset.testValue`로 접근할 수 있다.  
✔ 속성명 작성 요령

- 대소문자 여부에 상관없이 xml로 시작하면 안된다.
- 세미 콜론 포함 x
- 대문자 포함 x

### 2. csrftoken 작성

1. hidden 타입으로 숨겨져 있는 csrf값을 가진 input 태그를 선택한다.

   ![image](https://user-images.githubusercontent.com/109324637/198935405-5fb3dab1-4cbb-4c49-9c48-8d7a0a8e9398.png)

```html
<!-- accounts/profile.html -->

<script>
  const form = document.querySelector("#follow-form");
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;
</script>
```

2. AJAX로 csrftoken 보내기

```html
<!-- accounts/profile.html -->

<script>
  const form = document.querySelector("#follow-form");

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    axios({
      method: "post",
      url: `/accounts/${userId}/follow/`,
      headers: { "X-CSRFToken": csrftoken },
    });
  });
</script>
```

3. 팔로우 여부를 확인할 수 있는 변수를 담아 JSON 타입으로 응답하기

```python
# accounts/views.py

from django.http import JsonResponse

@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                'is_followed': is_followed,
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

4. views함수에서 응답한 is_followed를 사용해 버튼 토글하기

```html
<!-- accounts/profile.html -->

<script>
  axios({
  method: 'post',
  url: `/accounts/${userId}/follow/`,
  headers: {'X-CSRFToken': csrftoken,}
  })
  .then((response) => {
    const isFollowed = response.data.is_followed
    const followBtn = document.querySelector('#follow-form > input[type=submit]')
    if (isFollowed === true) {
      followBtn.value = '언팔로우'
    } else {
      followBtn.value = '팔로우'
    }
  })
```

5. 개발자 도구로 결과 확인해보기

   ![image](https://user-images.githubusercontent.com/109324637/198936287-6b44627e-b1bb-4c89-b316-a40c09892c18.png)
   ![image](https://user-images.githubusercontent.com/109324637/198936397-a5885b8e-b5fb-46d3-8b93-935423d76adb.png)

## 팔로워 & 팔로잉 수 비동기 적용

1. 해당 요소를 선택할 수 있도록 span 태그와 id 속성 작성

```django
<!-- accounts/profile.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span> / 팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span>
  </div>
```

2. 직전에 작성한 span 태그 각각 선택

```html
<!-- accounts/profile.html -->

<script>
  axios({
  method: 'post',
  url: `/accounts/${userId}/follow/`,
  headers: {'X-CSRFToken': csrftoken,}
  })
  .then((response) => {
    ...
    const followersCountTag = document.querySelector('#followers-count')
    const followingsCountTag = document.querySelector('#followings-count')
  })
```

3. 팔로워, 팔로잉 인원 수 연산은 view 함수에서 진행하여 결과를 응답으로 전달

```python
# accounts/views.py

from django.http import JsonResponse

@require_POST
def follow(request, user_pk):
    ...
            context = {
                'is_followed': is_followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

4. view 함수에서 응답한 연산 결과를 사용해 각 태그의 인원 수 값 변경하기

```html
<!-- accounts/profile.html -->

<script>
  axios({
  method: 'post',
  url: `/accounts/${userId}/follow/`,
  headers: {'X-CSRFToken': csrftoken,}
  })
  .then((response) => {
    ...
    const followersCountTag = document.querySelector('#followers-count')
    const followingsCountTag = document.querySelector('#followings-count')
    const followersCount = response.data.followers_count
    const followingsCount = response.data.followings_count
    followersCountTag.innerText = followersCount
    followingsCountTag.innerText = followingsCount
  })
```

### 최종 코드

1. HTML 템플릿

```django
{% extends 'base.html' %}

{% block content %}
  <h1>{{ person.username }}님의 프로필</h1>
  <div>
    팔로워 : <span id="followers-count">{{ person.followers.all|length }}</span> / 팔로잉 : <span id="followings-count">{{ person.followings.all|length }}</span>
  </div>


  {% if request.user != person %}
  <div>
    <form id="follow-form" data-user-id="{{ person.pk }}">
      {% csrf_token %}
      {% if request.user in person.followers.all %}
        <input type="submit" value="언팔로우">
      {% else %}
        <input type="submit" value="팔로우">
      {% endif %}
    </form>
  <div>
  {% endif %}
```

2. Python 코드

```python
@require_POST
def follow(request, user_pk):
    if request.user.is_authenticated:
        User = get_user_model()
        me = request.user
        you = User.objects.get(pk=user_pk)
        if me != you:
            if you.followers.filter(pk=me.pk).exists():
                you.followers.remove(me)
                is_followed = False
            else:
                you.followers.add(me)
                is_followed = True
            context = {
                'is_followed': is_followed,
                'followers_count': you.followers.count(),
                'followings_count': you.followings.count(),
            }
            return JsonResponse(context)
        return redirect('accounts:profile', you.username)
    return redirect('accounts:login')
```

3. JavaScript 코드

```javascript
<script>
    const form = document.querySelector('#follow-form')
    const csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value

    form.addEventListener('submit', function (event) {
      event.preventDefault()

      const userId = event.target.dataset.userId

      axios({
        method: 'post',
        url: `/accounts/${userId}/follow/`,
        headers: {'X-CSRFToken': csrftoken,}
      })
        .then((response) => {

          // 버튼 토글
          const isFollowed = response.data.is_followed
          const followBtn = document.querySelector('#follow-form > input[type=submit]')

          if (isFollowed === true) {
            followBtn.value = '언팔로우'
          } else {
            followBtn.value = '팔로우'
          }

          // 팔로우, 팔로워 인원 수
          const followersCountTag = document.querySelector('#followers-count')
          const followingsCountTag = document.querySelector('#followings-count')
          const followersCount = response.data.followers_count
          const followingsCount = response.data.followings_count
          followersCountTag.innerText = followersCount
          followingsCountTag.innerText = followingsCount
        })
        .catch((error) => {
          console.log(error.response)
        })
    })
  </script>
```

## 좋아요(like)

✔ 팔로우와 동일한 흐름 + `forEach()` & `querySelectorAll()`

- index 페이지 각 게시글마다 좋아요 버튼

1. HTML 코드

```django
<!-- articles/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Articles</h1>
  {% if request.user.is_authenticated %}
    <a href="{% url 'articles:create' %}">CREATE</a>
  {% endif %}
  <hr>
  {% for article in articles %}
    <p>
      <b>작성자 : <a href="{% url 'accounts:profile' article.user %}">{{ article.user }}</a></b>
    </p>
    <p>글 번호 : {{ article.pk }}</p>
    <p>제목 : {{ article.title }}</p>
    <p>내용 : {{ article.content }}</p>
    <div>
      <form class="like-forms" data-article-id="{{ article.pk }}">
        {% csrf_token %}
        {% if request.user in article.like_users.all %}
          <input type="submit" value="좋아요 취소" id="like-{{ article.pk }}">
        {% else %}
          <input type="submit" value="좋아요" id="like-{{ article.pk }}">
        {% endif %}
      </form>
    </div>
    <a href="{% url 'articles:detail' article.pk %}">상세 페이지</a>
    <hr>
  {% endfor %}
{% endblock content %}
```

2. Python 코드

```python
# articles/views.py

from django.http import JsonResponse

@require_POST
def likes(request, article_pk):
    if request.user.is_authenticated:
        article = Article.objects.get(pk=article_pk)

        if article.like_users.filter(pk=request.user.pk).exists():
            article.like_users.remove(request.user)
            is_liked = False
        else:
            article.like_users.add(request.user)
            is_liked = True
        context = {
            'is_liked': is_liked,
        }
        return JsonResponse(context)
    return redirect('accounts:login')
```

3. JavaScript 코드

```html
<!-- articles/index.html -->

<script>
  const forms = document.querySelectorAll(".like-forms");
  const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

  forms.forEach((form) => {
    form.addEventListener("submit", function (event) {
      event.preventDefault();
      // onsole.log(event.target.dataset)

      const articleId = event.target.dataset.articleId;

      axios({
        method: "post",
        url: `http://127.0.0.1:8000/articles/${articleId}/likes/`,
        headers: { "X-CSRFToken": csrftoken },
      })
        .then((response) => {
          // console.log(response)
          // console.log(response.data)

          const isLiked = response.data.is_liked;

          const likeBtn = document.querySelector(`#like-${articleId}`);
          if (isLiked === true) {
            likeBtn.value = "좋아요 취소";
          } else {
            likeBtn.value = "좋아요";
          }
          // likeBtn.value = isLiked ? '좋아요 취소' : '좋아요'
        })
        .catch((error) => {
          console.log(error.response);
        });
    });
  });
</script>
```
