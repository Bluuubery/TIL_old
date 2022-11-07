# DynamicFieldsModelSerializer

## 개요
Django의 DjangoRESTFramework(DRF)는 자체적으로 serializer 클래스를 제공한다.

그런데 view 함수에서 해당 model의 특정 field만 출력하거나, 혹은 nested relationship에서 특정 field만 상속받고 싶은 경우가 있다.

한두 개라면 따로 serializer를 만들어줄 수 있겠지만 여러 개라면 코드가 복잡해지고 변수명 짓기도 어려워진다.

따라서 **'field' 인자를 따로 정의해 원하는 field만 출력**하도록 하는 `DynamicFieldsModelSerializer` 클래스를 따로 정의해 해결할 수 있다.

## 코드
### Serializer 클래스 정의
```python
from rest_framework import serializers


class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop("fields", None)

        # Instantiate the superclass normally
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields that are not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields)
            for field_name in existing - allowed:
                self.fields.pop(field_name)
```

### 사용 예시 (nested relationship)
```python
class ActorNameSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Actor
        fields = ["name"]


class ReviewSerializer(DynamicFieldsModelSerializer):
    movie = MovieTitleSerializer(read_only=True)

    class Meta:
        model = Review
        fields = "__all__"


class MovieSerializer(DynamicFieldsModelSerializer):
    actors = ActorNameSerializer(many=True, read_only=True)
    # ReviewSerializer에서 title, content 필드만 받아온다.
    review_set = ReviewSerializer(
        many=True,
        read_only=True,
        fields=[
            "title",
            "content",
        ],
    )

    class Meta:
        model = Movie
        fields = "__all__"

```

### 사용 예시 (views.py)
```python
@api_view(["GET"])
def review_list(request):
    if request.method == "GET":
        reviews = get_list_or_404(Review)
        # ReviewSerializer에서 특정 필드만 선택해서 데이터를 보내준다.
        serializer = ReviewSerializer(
            reviews,
            many=True,
            fields=[
                "title",
                "content",
            ],
        )
        return Response(serializer.data)
```

## 참고 자료
공식문서: [https://www.django-rest-framework.org/api-guide/serializers/#dynamically-modifying-fields](https://www.django-rest-framework.org/api-guide/serializers/#dynamically-modifying-fields)