## 1. 한국어로 번역하기
### 1-1. 한국어 번역 관련 settings.py 변수와 할당값

> `LANGUAGE_CODE` 변수에 `'ko-kr'` 할당

### 1-2. 1-1을 활성화 시키기 위한 변수

> `USE_I18N = True`

## 2.Django Template Language
    #1 menus 리스트를 반복문으로 출력
    {% for menu in menus %}
      <p>{{ menu }}</p>
    {% endfor %}

    #2 posts 리스트를 반복문 활용하여 0번 글부터 출력
    {% for post in posts %}
      <p>{{ forloop.counter0 }}번 글 : {{ post }}</p>
    {% endfor %}

    #3 users 리스트가 비어있다면 pass를 출력
    {% for user in users %}
      <p>{{ user }}</p>
    {% empty %}
      <p>pass</p>
    {% endfor %}

    #4 첫 번째 반복문일 때와 아닐 때를 조건문으로 분기처리
    {% if forloop.first %}
      <p> 첫 번째 </p>
    {% else %}
      <p> 아닐 때 </p>
    {% endif %}

    #5 출력된 결과가 주석과 같게 만들기
    <!-- 5 -->
    <p>{{ 'hello'|length }}</p>
    <!-- My Name Is Tom -->
    <p>{{ 'my name is tom'|title }}</p>

    #6 변수 today에 datetime 객체가 들어있을 때 출력된 결과가 주석과 같게 만들기
    <!-- 2020년 02월 02일 (Sun) PM 02:02 -->
    {{ today|date:"Y년 m월 d일 (D) A h:i" }}
    
