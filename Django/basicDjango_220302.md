## 1. MTV
> MTV : Model Template View => Model은 DB에 저장되는 데이터를 의미, Template은 유저에게 보여지는 화면을 의미, View는 요청에 따라 적절한 로직을 수행하여 결과를 템플릿으로 렌더링하며 응답.
> MVC : Model View Controller
> M-M, T-V, V-C로 매칭. 


## 2. URL
> (a) 는 Django에서 URL 자체를 변수처럼 사용해서 동적으로 주소를 만드는 것을 의미한다. (a)는 무엇인지 작성하시오.
> > **Dynamic URL** => path('member/<str:name>/', view.member),

## 3. Django template path
> Django 프로젝트는 render할 template 파일들을 찾을 때, 기본적으로 settings.py에 등록된 각 앱 폴더 안의 (a) 폴더 내부를 탐색한다. (a)에 들어갈 폴더 이름을 작성하시오.
> > **BASE_DIR**

