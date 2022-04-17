* 20220415 Django pjt07 ~ TIL

  

  > Django 프레임워크 특징

  MVC 패턴 기반 MTV (기본적으로 Model-View-Controller 를 기반으로 한 프레임워크)
  ORM(Object-relational mapping) 기능 지원
  쉬운 DB관리를 위해 프로젝트를 생성하면서 관리자기능을 제공
  쉬운 URL 파싱 기능 지원
  동일한 소스코드에서 다른 나라에서 용이하도록 번역, 날짜/시간/숫자 등의 포맷 타임존 지정 등의 기능을 제공

  인기 프레임워크 https://devsnote.com/writings/2122
  백엔드, 프론트엔드 프레임워크/개발언어 https://it-ist.tistory.com/82

  Django 프로젝트 진행 순서도 (articles, accounts 두 개 앱 동시에)

  

  #### 1. 깃 재설정

  -rm rf .git
  git add .
  git commit -m 'first project commit'
  git remote add origin <url>

  *** git remote -v 명령어로 클론한 저장소의 remote 정보를 확인 가능

  

  #### 2. 프로젝트 시작

  django-admin startproject <프로젝트 이름>
  cd <프로젝트 이름>
  python manage.py startapp <추가 앱 이름>

  ```
  articles : 게시글
  accounts : auth와 관련해 Django 내부적으로 accounts라는 이름으로 사용되고 있기 때문에 되도록 accounts 지정 권장
  pjt07, CRUD, one_to_many : 기본 프로젝트
  ```

  

  #### 3. 가상환경 설정

  python -m venv venv
  source venv/Scripts/activate
  pip install -r requirements.txt

  *** pip freeze > requirements.txt => 현재 패키지 txt 파일로 저장하기

  

  #### 4. 기본 프로젝트 세팅

  > <기본 프로젝트>/settings.py

  ```
  INSTALLED_APPS에서 추가 앱, 3rd party apps(django_extensions) 작성
  TEMPLATES에서 기본 템플릿 경로 설정
  ```

  *** 'DIRS': [BASE_DIR / 'templates'], => 이 코드를 통해 경로가 추가되어야만 base.html 템플릿을 찾을 수 있게 된다. 만약 DIRS에 여러 경로가 추가되면, Django는 경로 순서대로 템플릿 탐색.

  > 기본 템플릿 templates/base.html 만들기
  > ! + tab
  > body 태그 사이에 block (템플릿 상속) => {% block content %}{% endblock content %}

  > <기본 프로젝트>/urls.py
  > import에 include 추가 후 urlpatterns 에 url 추가 작성. (관리 용이하도록 추가 앱의 url과 연결)
  > *** include('articles.urls') => articles의 urls파일을 불러옴. 그러나 현재 앱에 urls 파일 없으므로 만들어주기. accounts도 동일.

  settings.py 내 추가 설정
  *** AUTH_USER_MODEL = 'accounts.User' => accounts/models.py 내 AbstractUser를 상속받은 User 모델을 새로 만들었으므로, 이 모델을 유저모델로 사용하기 위해 settings.py 내 추가 설정
  AUTH_USER_MODEL을 지정하기 전에 manage.py migrate는 절대!! 금지!!

  

  #### 5. 각 앱의 urls 파일 세팅

  app_name = 'articles'

  urlpatterns = [

  path('\<str:username>/', views.profile, name='profile'),

  ]

  * \<str:username>는 주소창에 입력된 값을 str(문자열) 형태의 'username'이라는 파라미터로 views.py에 있는 profile 함수에 전달된다.

  * name='profile' 은 템플릿(html)이나 views에 전달하기 위한 네이밍.

    => views에는 `return redirect('articles:article_detail', article.pk)`와 같은 형식

  

  ```html
  # templates/profile.html
  
  <a href="{% url 'articles:profile' username %}">{{ username }}</a>
  ```

  => `username`는 URL 매핑에 정의된 `<str:username>`에 전달해야 하는 값을 의미한다.

  => 각자 앱에서 profile, index, detail 등의 URL 별칭을 사용하고 싶을 때를 위해 urls.py에 app_name을 설정하고 html에 `articles:profile`와 같은 방식으로 표기한다. 

  *** from . import views => 현재 폴더에서 views를 가져오라는 의미

  

  

  #### 6. 각 앱의 models 파일 세팅

  > models.py
  > django framework 에서 데이터모델을 만들어주는 역할을 하고 있는 파일이다. models.py 파일안에 클래스형으로 데이터 모델을 만들어주면 장고가 ORM(object-oriented-mapping)을 통해 데이터베이스에 데이터 모델을 생성해준다.

  -articles models.py 코드 분석-
  from django.conf import settings => 외래키

  ```
  django.conf => config : 구성 파일
  ```

  class Article(models.Model): 

  ```
  Article이라는 모델이 있고, (models.Model) 이라고 해주는 것은  django.db.models.Model 의 subclass 이라는 뜻입니다. 
  ```

  ``` # 서브클래스
  class Unit:
      def __init__(self, rank, size, life):
          self.name = self.__class__.__name__
          self.rank = rank
          self.size = size
          self.life = life
  
      def show_status(self):
          print('이름: {}'.format(self.name))
          print('등급: {}'.format(self.rank))
          print('사이즈: {}'.format(self.size))
          print('라이프: {}'.format(self.life))
  
  
  class Goblin(Unit):
      pass
  
  
  goblin_1 = Goblin('병사', 'Small', 100)
  
  goblin_1.show_status()
  ```

  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

  ```
  settings의 AUTH_USER_MODEL을 참조함. ('accounts.User' 참조)
  on_delete 옵션은 Django에서 모델을 구현할 때 데이터베이스 상에서 참조무결성을 유지하여 ForeignKeyField가 바라보는 값이 삭제될 때 해당 요소를 처리하는 방법을 지정해 준다.
  CASCADE : ForeignKeyField를 포함하는 모델 인스턴스(row)도 같이 삭제한다
  
  참조 무결성
  - 기본 키와 참조 키 간의 관계가 항상 유지됨을 보장합니다. 
  - 참조되는 테이블의 행을 이를 참조하는 참조키가 존재하는 한 삭제될 수 없고, 기본키도 변경될 수 없습니다.
  ```

  def \__str__(self):

  ```
  self는 해당 함수를 호출한 객체를 가리키는 것. __str__ 함수는 객체를 문자열로 표현한 것을 반환해주는 함수.
  ```

  

  -accounts models.py 코드 분석-

  ```
  from django.contrib.auth.models import AbstractUser
  
  class User(AbstractUser): # 기본적으로 제공하는 필드 외에 원하는 필드를 적어준다.
  ```

  => `AbstractUser`를 import하여 `User`가 `AbstractUser`를 상속받도록 해주고 원하는 필드를 적어주면 됨

  PositiveIntegerField => 음수가 없는 IntegerField

  

  #### 7. 각 앱의 views 파일 세팅

  -articles views.py 코드 분석-

  ```python
  from django.shortcuts import get_object_or_404, render, redirect
  ```

  => `get_object_or_404` : 만약 객체가 존재하지 않을 때 `get()` 을 사용하여 `Http404` 예외를 발생시킴.

  => render의 경로는 하드코딩, redirect의 경로는 urls.py의 name 이용. 왜냐하면 `render` 는 템플릿을 불러오고, `redirect` 는 URL로 이동하기 때문

  데코레이터

  ```python
  from django.views.decorators.http import require_http_methods, require_POST, require_safe
  ```

  => 다양한 HTTP 기능을 지원하기 위해 Django에서는 몇 가지 데코레이터를 제공

  * require_http_methods : view가 특정 요청 메서드만 허용하도록 요구하는 데코레이터
  * require_GET() : view가 GET 메서드만 허용하도록 요구하는 데코레이터
  * require_POST() : view가 POST 메서드만 허용하도록 요구하는 데코레이터
  * require_safe() : view가 GET 및 HEAD 메서드만 허용하도록 요구하는 데코레이터. 이러한 메서드는 일반적으로 "안전"한 것으로 간주되는데, 이는 요청된 리소스를 검색하는 것 이외의 작업을 수행하는 의미가 없어야 하기 때문

  

  ```python
  from django.contrib.auth.decorators import login_required
  ```

  => authentication(인증) 관련 데코레이터

  * login_required : 사용자가 로그인하지 않은 경우 설정으로 리디렉션하고, 사용자가 로그인한 경우 보기를 정상적으로 실행하는 데코레이터

  

  ```python
  from django.contrib.auth import get_user_model
  ```

  => 어디서 쓰이는지 질문///

  ```python
  def article_create(request):
      if request.method == 'POST':
          form = ArticleForm(request.POST)
          if form.is_valid():  # 유효성 검사
              article = form.save(commit=False)  # 저장 직전에 멈추고, article 객체만 리턴해라
              article.user = request.user
              article.save()
              return redirect('articles:article_detail', article.pk)  # urls.py 파라미터
      else:
          form = ArticleForm()
      context = { 'form': form, }
      return render(request, 'articles/article_form.html', context)
  ```

  => create 함수에서 게시글을 저장하기 전에 요청을 보낸 user 정보를 담도록 코드를 바꿔야 한다.

  (이때, article = form.save() -> 이렇게 바로 저장하면 필수로 들어가야하는 user 값이 안 들어간 상황이기 때문에 에러가 난다)

  => context는 템플릿(article_form.html)에서 쓰이는 변수명과 Python 객체를 연결하는 사전형 값

  

  ```python
  	articles = Article.objects.order_by('-pk')
  ```

  => 게시글들을 내림차순으로 정리

  

  -accounts views.py 코드 분석-

  ```python
  from django.contrib.auth import login as auth_login, logout as auth_logout
  ```
  
  => views.py 내 정의한 함수 login과 구분하기 위해 auth_log로 재 명명함
  
  ```python
  from .forms import CustomUserCreationForm
  
  
  def signup(request):
      if not request.user.is_authenticated:
          if request.method == 'POST':
              form = CustomUserCreationForm(request.POST)
  ```
  
  => signup 함수 내에서 사용하는 `UserCreationForm`을 `CustomUserCreationForm` 으로 변경
  
  
  
  #### 8. 각 앱의 forms 파일 세팅
  
  
  ```
  Form 클래스는 form내 field, field 배치, 디스플레이 위젯, 라벨, 초기값, 유효한 값(유효성 체크 이후에) 비유효 field에 관련된 에러메시지를 결정한다. Form 클래스는 또한 미리 정의된 포맷(테이블, 리스트 등)의 템플릿으로 그 자신을 렌더링하는 method나 어떤 요소의 값이라도 얻는 method를 제공한다. 즉, forms.py에 있는 클래스들은 사용자가 제출하는 데이터들을 통과시켜주는 매개체로 작동한다.
  ```
  
  -articles forms.py 코드 분석-
  
  ```python
  class ArticleForm(forms.ModelForm):
  
      class Meta:
  ```
  
  Meta 클래스는 내부 클래스로 활용되며, 이는 기본 필드의 값을 재정의할 때 사용
  
  
  
  - Form (일반 폼) : 직접 필드 정의, 위젯 설정이 필요
  - Model Form (모델 폼) : 모델과 필드를 지정하면 모델폼이 자동으로 폼 필드를 생성
  
  ```python
  from django import forms
  from .models import Post
  
  # Form (일반 폼)
  class PostForm(forms.Form):
  	title = forms.CharField()
  	content = forms.CharField(widget=forms.Textarea)
  
  # Model Form (모델 폼)
  class PostForm(forms.ModelForm):
  	class Meta:
  		model = Post
  		fields = ['title', 'content'] # '__all__' 설정시 전체 필드 추가
  ```
  
  ​    fields의 필드
  
  ​    1. 유효성 검사를 하겠다.
  
  ​    2. HTML에 출력될 것이다.
  
  
  
  - Model Form 클래스에는 .save(self, commit=True) 메소드가 구현되어 있음
  - DB 저장 여부를 commit flag를 통해서 결정
  - commit=False flag를 통해 함수 호출을 지연 (views.py)
  
  
  
  -accounts forms.py 코드 분석-
  
  기능 구현하다 만 것인지???
  
  
  
  \# python manage.py makemigrations 중 발생한 오류 1
  
  ```bash
  ~~~
  django.core.exceptions.ImproperlyConfigured: Creating a ModelForm without either the 'fields' attribute or the 'exclude' attribute is prohibited; form CommentForm needs updating.
  ```
  
  => When you are creating a form using model, you need to specify which fields you want to be included in the form.
  
  For example you have a model with the named Article and you want to create a form for the model article.
  
  => forms.py 에서 fields를 fiels로 오타
  
  \# 오류 2
  
  ```bash
  ~~~
  TypeError: CommentForm.Meta.fields cannot be a string. Did you mean to type: ('content',)?
  ```
  
  =>
  
      class Meta:
          model = Comment
          fields = ('content',)  # 'content' 뒤에 쉼표 필수로 넣기
  
  
  
  #### 9. 각 앱의 html 파일 세팅
  
  -base.html-
  
  ```python
        {% if user.is_authenticated %}
        <li><a href="{% url 'articles:article_create' %}">New Article</a></li>
        <li><a href="{% url 'accounts:profile' user.username %}">{{ user.username }} - Profile</a></li>
        <li><a href="{% url 'accounts:logout' %}">Logout</a></li>
        {% else %}
        <li><a href="{% url 'accounts:login' %}">Login</a></li>
        <li><a href="{% url 'accounts:signup' %}">Signup</a></li>
        {% endif %}
  ```
  
   `is_authenticated `
  
  - User class의 속성(attributes)
  - 사용자가 인증되었는지 확인하는 방법
  - User에 항상 `True`이며, AnomymousUser에 대해서만 항상 ` False`
  - 단, 이것은 권한(permission)과는 관련이 없으며 사용자가 활성화 상태(active)이거나 유효한 세션(valid session)을 가지고 있는지도 확인하지 않음
  
  `{% url 'accounts:profile' user.username %}{{ user.username }}`
  
  => user.username 은 정확히 어느 경로를 거쳐서 온건지???
  
  
  
  -article_index.html-
  
  ```python
    {% for article in articles %}
    <li><a href="{% url 'articles:article_detail' article.pk%}">{{ article.title }} </a></li>
    {% endfor %}
  ```
  
  => url 태그와 for문, {{}}는 독립(?)
  
  =>  views.py의 article_index 함수에서 `articles = Article.objects.order_by('-pk')`이므로 articles가 `{% for article in articles %}`와  `{{ article.title }}`를 통해 pk 순서대로 나열된 리스트로 보여짐.
  
  
  
  -article_form.html-
  
  ```python
  <form method="POST">
    {% csrf_token %}
    {{ form.as_p }}
    <button>submit</button>
  </form>
  ```
  
  => 템플릿에서 사용한 `{{ form.as_p }}`의 form은 views.py의 article_create 함수에서 전달한 ArticleForm의 객체
  
  
  
  => ` {{ article.content|linebreaksbr }}`에서 linebreaksbr은 텍스트에서 행이 바뀌면 문단으로 변환하도록 하라는 의미
  
  
  
  *** {{ form }} 을  {{ form.as_p }} 로 바꾸면 인라인이 p 태그로 변한다.(한줄에 있는데 title과 content로 2줄로 바뀐다.)
  
  
  
  #### 10. 마이그레이션
  
  python manage.py makemigrations
  python manage.py migrate
  
  
  
  #### 11. 서버 실행
  
  python manage.py runserver
  
  
  
  
  
  -comment-
  
  흡수하는 시간 Good.
  
  내 의지로 처음 공식 문서에 들어가서 구경해봄. (장고 파일의 역할들에 대해 알아보려고)
  
  처음엔 다양한 변수들이 무엇을 의미하는지 아예 몰랐고, 공부하기 두려웠는데 막상 시작하니 재밌었다.
  
  추후 간단한 SNS를 만들어보고 싶다는 생각이 들었다.
  
  SSAFY를 시작하고 나서 가장 열심히, 집중해서, 재밌게 공부한 날이 된 것 같다.
  
  
  
  작성 기간 4/15~4/17 (4/16 휴식)
  
  
  
  추후 여유로울 때 글 다듬으면서 복습하기.
