# 1. progress & meter

## progress

```html
    <progress value="50" max="100"></progress>
```

![img](https://images.velog.io/images/jiseon-han/post/8dded01d-053a-41ba-86c0-27cdcfa13276/progress_example.mov.gif)

## meter

```html
<meter value="10" min="0" max="100" low="20" high="65" optimum="15"></meter>
```

![img](https://images.velog.io/images/jiseon-han/post/509658c9-fc08-4932-9a82-bf2c99b71979/%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202022-01-17%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%208.48.49.png)

> **meter와 progress 차이 ✨**
> meter는 속성에 따라 값이 높고 낮을때 색상을 다르게 설정하여 작업의 진행 상태를 표현할 수 있지만, progress는 값의 상태만 전달.

# 2. detail & summary

유저의 클릭으로 정보를 보여주고 숨기는 패턴 적용 가능

```html
<details>
	<summary>클릭 전 볼 수 있는 영역</summary>
	<span>클릭 후에만 표시되는 영역</span>
</details>
```

![img](https://images.velog.io/images/jiseon-han/post/fbd727d0-cf39-4986-aa21-6b4b05ab5c7d/%E1%84%92%E1%85%AA%E1%84%86%E1%85%A7%E1%86%AB%20%E1%84%80%E1%85%B5%E1%84%85%E1%85%A9%E1%86%A8%202022-01-17%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%209.12.42.mov.gif)

> css로 유저의 클릭 여부에 따라 스타일 변경 할 때 🔖
>
> ```
>   	details[open]{
> 		background-color: #cdedfd;
> 	}
>   	
> ```

# 3. 달력, 날짜 선택기

input 태그의 type으로 설정 가능. 브라우저마다 UI 다름.

```html
<input type="date"/>
<input type="week"/>
<input type="month"/>
<input type="time"/>
```

type=date 일때 : 
type=week 일때 : 
type=month 일때 : 
type=time 일때 : 

# 4. picture

유저의 장치나 환경에 따라 각기 다른 버전의 이미지 표시하거나 브라우저가 이미지 포맷 지원하지 않을 때 다른 포맷 제공할 수 있음.
picture태그는 img태그, source 태그와 함께 사용됨.

> **장점 💡**
> 환경에 맞는 이미지를 다운로드 해서 보여줄 수 있으므로, 페이지 로딩 속도를 높일 수 있음.

```html
<picture>
	<source srcset="src/01.jpeg" media="(min-width:1200px)"/>
    <source srcset="src/02.jpeg" media="(min-width:900px)"/>
    <source srcset="src/03.jpeg" media="(min-width:500px)"/>
    <img src="src/04.jpeg" />
</picture>
```

- media 사이즈에서 각 해당 이미지 보여줌
- img태그는 default 이미지. 브라우저가 picture, source태그 미지원시 사용.

# 5. datalist

javascript 없이 **auto complete(자동완성)🔥** 사용 가능. 입력에 따른 필터 기능 제공.

> **주의사항**
> input의 list와 datalist의 id는 동일해야됨

```html
<label for="movie">What is your favourite movie?</label>
<input type="text" list="movie-options"/>

<datalist id="movie-options">
  <option value="Dune"/>
  <option value="Dark waters"/>
  <option value="The Artist"/>
  <option value="The Avengers"/>
  <option value="Iron Man"/>
  <option value="Iron Man II"/>
  <option value="Matrix"/>
</datalist>
```

![img](https://images.velog.io/images/jiseon-han/post/b85ccc6a-8815-4b8e-80a8-dfcba407c8f4/%E1%84%92%E1%85%AA%E1%84%86%E1%85%A7%E1%86%AB%20%E1%84%80%E1%85%B5%E1%84%85%E1%85%A9%E1%86%A8%202022-01-17%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%209.03.42.mov.gif)





출처: [신기한 HTML 태그 5개 (velog.io)](https://velog.io/@jiseon-han/신기한-HTML-태그-5개)