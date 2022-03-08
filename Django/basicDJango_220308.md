## 1. Model 반영하기 

> Migrations : Django가 Model에 생긴 변화를 Db에 반영하는 방법

## 2. Model 변경사항 저장하기
    class Article(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
### 1) 위에서 작성한 Model의 변경사항을 저장하기 위한 명령어
> `$ python manage.py makemigrations articles`
### 2) 마이그레이션 파일에 대응되는 SQL문을 확인하기 위한 명령어와 출력결과 작성 (app의 이름은 articles)
> `$ python manage.py sqlmigrate articles <migration-name>`

## 3. Python Shell
* Django에서 사용 가능한 모듈 및 메서드를 대화식 Python Shell에서 사용하려고 할 때, 어떤 명령어를 통해 해당 Shell을 실행할 수 있는지 작성
> `$ python manage.py shell`

## 4. Django Model Field

* Django에서 Model을 정의할 때 사용할 수 있는 필드 타입을 5가지 이상 작성
- **TextField** : max_length 속성 지정이 가능한 큰 텍스트를 위한 필드
- **CharField** : 작은 문자열에서 큰 사이즈의 문자열을 위한 필드
- **DateField** : 파이썬의 datetime.date 인스턴스에 의해 표현되는 날짜 필드
- **ImageField** : 이미지를 위한 필드
- **IntegerField** : 정수를 위한 필드