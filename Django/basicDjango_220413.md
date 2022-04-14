basicDjango_220413



#### 1. 아래의 설명을 읽고 T/F 여부를 작성 후 이유를 설명하시오.

- URI 는 정보의 자원을 표현하고 자원에 대한 행위는 HTTP Method 로 표현한다. 

  => T : REST API란 "Representational State Transfer". HTTP URI를 통해 자원을 명시하고,  HTTP METHOD를 통해 해당 자원에 대한 CRUD Operation을 적용하는 것을 의미한다.

- HTTP Method 는 GET 과 POST 두 종류 뿐이다.

  => F : HTTP Method(GET, POST, PUT, DELETE)로 표현한다.

- ‘https://www.fifa.worldcup/teams/team/43822/ 는 계층 관계를 잘 표현한 RESTful한 URI라고 할 수 있다.

  ????

  

#### 2. 다음의 HTTP status code 의 의미를 간략하게 작성하시오.

- 200 : **성공**, 서버가 요청을 제대로 처리했다는 뜻이다. 이는 주로 서버가 요청한 페이지를 제공했다는 의미로 쓰인다.
- 400 : **잘못된 요청**, 서버가 요청의 구문을 인식하지 못했다.
- 401 : **권한 없음**, 이 요청은 인증이 필요하다. 서버는 로그인이 필요한 페이지에 대해 이 요청을 제공할 수 있다. 상태 코드 이름이 권한 없음(Unauthorized)으로 되어 있지만 실제 뜻은 인증 안됨(Unauthenticated)에 더 가깝다.
- 403 : **Forbidden, 금지됨**, 서버가 요청을 거부하고 있다. 예를 들자면, 사용자가 리소스에 대한 필요 권한을 갖고 있지 않다. (401은 인증 실패, 403은 인가 실패라고 볼 수 있음)
- 404 : **Not Found, 찾을 수 없음**, 서버가 요청한 페이지(Resource)를 찾을 수 없다. 예를 들어 서버에 존재하지 않는 페이지에 대한 요청이 있을 경우 서버는 이 코드를 제공한다.
- 500 : **내부 서버 오류**, 서버에 오류가 발생하여 요청을 수행할 수 없다.



#### 3. 아래의 모델을 바탕으로 ModelSerializer인 StudentSerializer class를 작성하시오.

```python
class Student(models.Model):
    name = models.TextField()
    age = models.CharField(max_length=20)
    address = models.TextField()
```

```python
class StudentSerializer(serializers.ModelSerializer):
    
    name = forms.TextField()
    
    class Meta:
        model = Student
        fields = ('name', 'age', 'address',)
```



#### 4. Serializers 의 의미를 DRF(Django REST Framework) 공식 문서 를 참고하여 간단하게 설명하시오.

* Serializers : 쿼리셋, 모델 인스턴스 등의 복잡한 데이터를 JSON, XML 등의 컨텐트 타입으로 쉽게 변환 가능한 python datatype으로 변환시켜줌.

