## Django Model (posts 앱 안의 models.py 파일에 다음과 같은 코드 작성)
    From django.db import models

    class Post(models.Model):
        title = models.CharField(max_length=100)
        content = models.TextField()

### 1) models.py를 작성한 후 마이그레이션 작업을 위해 터미널에 작성해야 하는 두 개의 핵심 명령어 작성
> `$ python manage.py makemigrations posts` : model을 변경한 것에 기반한 새로운 마이그레이션(= 설계도)을 만들 때 사용
> `$ python manage.py migrate posts` : 마이그레이션을 DB에 반영하기 위해 사용, 설계도를 실제 DB에 반영하는 과정

### 2) 새로운 Post를 저장하기 위해 작성한 코드 중 옳지 않은 것
    # 1
    post = Post()
    post.title = 'a'
    post.content = 'b'
    post.save()
    # 2
    post = Post(title='가', content='나')
    post.save()
    # 3
    post = Post('제목', '내용')
    post.save()
    # 4
    Post.objects.create(title='1', content='2')

* **# 3** : 키워드 인자가 없음.



### 3) Post가 10개 저장되어 있고 id의 값이 1부터 10까지라고 가정할 때 가장 첫 번째 Post를 가져오려고 한다. 다음 중 옳지 않은 코드는? 
    # 1
    post1 = Post.objects.all()[0]
    # 2
    post2 = Post.objects.all()[-10]
    # 3
    post3 = Post.objects.all().first()
    # 4
    post4 = Post.objects.all().get(id=1)

* **# 3** : `post3 = Post.objects.all().first()` => `post3 = Post.objects.first()`

### 4) my_post 변수에 Post 객체 하나가 저장되어 있다. title을 "안녕하세요" content를 "반갑습니다"로 수정하기 위한 코드는?
    my_post.title = "안녕하세요"
    my_post.content = "반갑습니다"
    my_post.save()
