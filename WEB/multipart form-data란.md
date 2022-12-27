 프로젝트를 진행하면서 프론트 -> 백엔드로 이미지를 전송하는 경우가 있었다.
오늘은 HTTP, multipart, multipart/form-data 세 가지 키워드에 대해 알아보고,
그 중에서 중요한 개념중에 하나인 **`multipart/form-data`**에 대해서 좀 더 깊이 알아보기로 한다.

# 목차

### HTTP multipart/form-data

- HTTP란?
- multipart & multipart/form-data
- React+axios를 통해 이미지 업로드 예제 알아보기

## 1. HTTP란?

### [HTTP(Hypertext Transfer Protocol) - 위키 피디아](https://en.wikipedia.org/wiki/Hypertext_Transfer_Protocol)

> 인터넷 상에서 클라이언트와 서버가 자원을 주고 받을 때 쓰는 통신 규약.

### 클라이언트 -> 서버 업로드 과정 이해하기

> 1. 파일 업로드를 구현할 때, 클라이언트가 웹브라우저라면 폼을 통해서 파일을 등록해서 전송한다.
> 2. 웹 브라우저가 보내는 HTTP 메시지는 `Content-Type` 속성이 `multipart/form-data`로 지정되고 정해진 형식에 따라 메시지를 인코딩하여 전송한다.
> 3. 이를 처리하기 위한 서버는 멀티파트 메시지에 대해서 각 파트별로 분리하여 개별 파일의 정보를 얻게 된다.

이미지 파일을 전송한다고 해서 이메일에 첨부파일을 붙여 메일을 보내는 것처럼 **png나 jpg 파일 자체가 전송되는 것이 아니다.**
이미지 파일도 문자로 이뤄져 있기 때문에 **`이미지 파일을 문자로 생성하여 HTTP request body에 담아 서버로 전송하는 것이다.`**

![img](https://velog.velcdn.com/images%2Fshin6403%2Fpost%2F969fe14e-44bf-4389-942f-6d6e98e1483e%2F%E1%84%89%E1%85%B3%E1%84%8F%E1%85%B3%E1%84%85%E1%85%B5%E1%86%AB%E1%84%89%E1%85%A3%E1%86%BA%202021-09-11%20%E1%84%8B%E1%85%A9%E1%84%92%E1%85%AE%205.10.46.png)

**HTTP(request와 response)**는 위 이미지와 같이 4개의 파트로 나눌 수 있다.
여기서 `Message Body에 들어가는 데이터 타입을 HTTP Header에 명시해줄 수 있다.`
이 때 명시할 수 있도록 해주는 필드가 바로 **`Content-type`**이다.
추가적으로 Content-type 필드에 MIME(Multipurpose Internet Mail Extensions) 타입을 기술해줄 수 있는데, 여러 타입 중 하나가 바로 **`multipart`** 이다.

## 2. multipart & multipart/form-data

### form이란?

form은 입력 양식 전체를 감싸는 태그이다.

- **`name`** : form의 이름, 서버로 보내질 때 이름의 값으로 데이터 전송한다.
- **`action`** : form이 전송되는 서버 url 또는 html 링크.
- **`method`** : 전송 방법 설정. `get`은 `default`,
  post는 데이터를 url에 공개하지 않고 숨겨서 전송하는 방법이다.
- **`autocomplete`** : 자동 완성. on으로 하면 form 전체에 자동 완성 허용한다.
- **`enctype`** : 폼 데이터(form data)가 서버로 제출될 때
  해당 데이터가 인코딩되는 방법을 명시한다.

그 중 오늘의 포스트는 **`entype의 속성값 중 하나이다.`**

이 속성은 `<form>` 요소의 method 속성값이 **`post`**인 경우에만 사용할 수 있다.

### entype 속성값

- application/x-www-form-urlencoded

  > default 값으로, 모든 문자들을 서버로 보내기 전에 인코딩됨을 명시한다.

- text/plain

  > 공백 문자(space)는 “+” 기호로 변환하지만, 나머지 문자는 모두 인코딩되지 않음을 명시한다.

- **multipart/form-data (오늘의 중요 포인트!)**

  > 모든 문자를 인코딩하지 않음을 명시한다.
  > 이 방식은 `<form>` 요소가 **파일이나 이미지를 서버로 전송할 때 주로 사용한다.**

```javascript
<form action="/home/uploadfiles" method="post" enctype="multipart/form-data">
    파일명 : <input type="file" name="myfile">
    <button type="submit">제출하기</button>
</form>
```

## Multipart가 생긴 배경

HTML의 input 의 type 중에 "file"이 있다.(이를테면 `<input type="file" />` )

이건 파일 업로드를 위한 input 컨트롤이다. 즉 사용자 컴퓨터에서 서버로 파일을 전송하기 위한 input 이다.

form이 submit이 되면 form안에 있는 컨트롤들의 데이터가 서버로 전송된다. 이때 이런 데이터들은 HTTP Request 형태로 서버로 전송된다. 파일 업로드의 원리는 HTTP Request가 가지고 있는데,

그 원리는 아래와 같다.

- `HTTP Request는 Body에 클라이언트가 전송하려고 하는 데이터를 넣을 수 있다.`
- `Body에 들어가는 데이터의 타입을 HTTP Header에 명시해 줌으로써 서버가 타입에 따라 알맞게 처리하게 한다.`
- `이 Body의 타입을 명시하는 Header가 Content-type이다.`

> 그런데 여기서 중요한 점은 보통 HTTP Request의 Body는 한 종류의 타입이 대부분이고, Content-type도 타입을 하나만 명시할 수 있다.
> `ex) text이면 text/plain, xml이면 text/xml, jpg이미지면 image/jpeg 등`

일반적인 form의 submit에 의한 데이터들의 `Content-type`은 `application/x-www-form-urlencoded` 이다.

그런데 파일 업로드의 상황을 살펴보면, 만약 자신이 찍은 사진을 올리는 `form`의 경우, 사진에 대한 설명을 위한 `input`과 사진 파일을 위한 `input` 2개가 들어간다.
그런데 이 두 input 간에 `Content-type`이 전혀 다르다.

이 두 `input` 간에 `Content-type`은 사진 설명은 `application/x-www-form-urlencoded` 이 될 것이고,

사진 파일은 `image/jpeg`이다.

두 종류의 데이터가 하나의 `HTTP Request Body`에 들어가야 하는데,

한 `Body`에서 이 2 종류의 데이터를 구분에서 넣어주는 방법도 필요해졌다.

그래서 등장하는 것이 `multipart` 타입이다.



출처: https://velog.io/@shin6403/HTTP-multipartform-data-%EB%9E%80