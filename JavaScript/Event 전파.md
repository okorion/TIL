## ✨ Event 전파

 이번 예제에서는 DOM에서 어떻게 이벤트가 실행되고 처리되는지 매우 간단하게 알아보겠습니다.

<br>

 HTML 문서의 BODY가 로드되면, TABLE의 상단 행에 이벤트 수신기가 등록됩니다. 이벤트 수신기는 이벤트를 처리하기 위해 `stopEvent` 함수를 실행합니다. `stopEvent` 함수는 테이블의 하단 셀의 값을 변경합니다. 

 `stopEvent`는 이벤트 객체 메서드인 `event.stopPropagation`도 호출합니다. 이 메서드는 이벤트가 DOM으로 더 이상 버블링(bubbling)되지 않도록 합니다. 테이블이 클릭될 때 메시지를 표시해야 하는 `onclick` 이벤트 처리기가 있다는 것에 주의하세요. 하지만 `stopEvent` 메서드가 전파를 중지했기 때문에 테이블의 데이터가 업데이트된 후 이벤트 단계는 효과적으로 종료되고, 이를 확인하는 `alert` 창이 표시됩니다.  

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <title>이벤트 전파</title>

    <style>
      #t-daddy { border: 1px solid red }
      #c1 { background-color: pink; }
    </style>

    <script>
    function stopEvent(event) {
      c2 = document.getElementById("c2");
      c2.innerHTML = "안녕하세요";

      // 이벤트가 t-daddy로 전파되지 않도록 합니다.
      ev.stopPropagation();
      alert("이벤트 전파가 중지되었습니다.");
    }

    function load() {
      elem = document.getElementById("tbl1");
      elem.addEventListener("click", stopEvent, false);
    }
    </script>
  </head>

  <body onload="load();">

    <table id="t-daddy" onclick="alert('안녕하세요.');">
      <tr id="tbl1">
        <td id="c1">1</td>
      </tr>
      <tr>
        <td id="c2">2</td>
      </tr>
    </table>
  </body>
</html>
```

<br>

<br>

### 🤔 `stopPropagation()` 메서드를 호출하지 않는다면?

 `stopPropagation()` 메서드를 호출하지 않는다면 `id`가 `tbl1`인 `<tr>`을 클릭했을 때, `id`가 `c2`인 `<td>`의 내용이 "안녕하세요"로 변경되고, `alert("이벤트 전파가 중지되었습니다.")`가 실행됩니다. 그리고 이후에 `id`가 `t-daddy`인 `<table>`의 `onClick` 속성에 선언된 `alert('안녕하세요.')`가 실행됩니다.

 기본적으로 이벤트 전파는 하위 요소에서 상위 요소로 이벤트가 전파되는 메커니즘입니다. 따라서 클릭 이벤트가 `<tr>` 요소에서 발생하면, 이벤트는 `<tr>` 요소의 상위 요소인 `<table>`로 전파됩니다. 따라서 `<td>`의 내용이 변경되고 `alert("이벤트 전파가 중지되었습니다.")`가 실행됩니다.

 하지만 `stopPropagation()` 메서드가 호출되면 이벤트 전파가 중지되고, 이벤트는 더 이상 상위 요소로 전파되지 않습니다. 따라서 `<table>`의 `onClick` 속성에 선언된 `alert('안녕하세요.')`는 실행되지 않습니다.

 따라서 `stopPropagation()` 메서드를 호출하지 않으면 클릭 이벤트가 이벤트 전파에 따라 `<tr>`에서 `<table>`로 전파되어 다음과 같은 동작이 발생합니다:

- `<td>`의 내용이 "안녕하세요"로 변경됨
- `alert("이벤트 전파가 중지되었습니다.")` 실행됨
- `<table>`의 `onClick` 속성에 선언된 `alert('안녕하세요.')` 실행됨

<br>

<br>

### 🖐️ Q&A

> `stopPropagation()` 코드는 이벤트 버블링이 많이 일어나는 상황이고 작동 순서가 복잡하다는 뜻이니 `stopPropagation()` 코드를 써야 되는 상황 자체를 안 만드는 게 좋지 않아?

<br>

 `stopPropagation()` 메서드는 이벤트 버블링을 중지시키는 역할을 합니다. 이를 사용하면 이벤트가 상위 요소로 전파되지 않으므로, 상위 요소에 연결된 이벤트 핸들러가 실행되지 않습니다. 

`stopPropagation()` 메서드를 사용하면 작동 순서가 복잡해질 수 있습니다. 이벤트가 하위 요소에서 상위 요소로 전파되는 것은 웹 애플리케이션에서 일반적인 동작이지만, 이를 중지시키면 이러한 전파 동작을 컨트롤하기 어려울 수 있습니다. 따라서 `stopPropagation()` 메서드를 사용할 때는 신중하게 고려해야 합니다.

 일반적으로 이벤트 핸들러를 작성할 때는 이벤트 버블링을 이해하고 필요에 따라 적절하게 활용하는 것이 좋습니다. 이벤트 버블링은 상위 요소에 대한 이벤트 처리를 더 쉽게 구현할 수 있도록 도와주는 메커니즘이며, 이를 이용하면 중복되는 코드를 줄일 수 있습니다.

  하지만 특정 상황에서 이벤트 버블링을 제어해야 하는 경우가 있다면 `stopPropagation()` 메서드를 사용할 수 있습니다. 이 경우에는 코드의 명확성과 유지보수성을 고려하여 사용하는 것이 중요합니다. `stopPropagation()`을 사용할 때는 이벤트의 흐름을 잘 이해하고, 코드가 복잡해지거나 예상치 못한 동작이 발생하지 않도록 주의해야 합니다.

 따라서 `stopPropagation()`을 사용할지 여부는 개발자의 판단에 달려 있으며, 상황과 요구 사항에 따라 적절하게 활용하는 것이 좋습니다.

<br>

<br>

> 예상치 못한 이벤트 전파를 막기 위해 모든 이벤트들에게 stopPropagation() 코드를 쓰는 방법은 어때?

<br>

 예상치 못한 이벤트 전파를 막기 위해 모든 이벤트에 `stopPropagation()`을 적용하는 것은 일반적으로 권장되지 않습니다. 이유는 다음과 같습니다: 

1. 예외 처리의 어려움: 모든 이벤트에 `stopPropagation()`을 사용하면 특정 상황에서 원치 않는 동작이 발생할 수 있습니다. 예를 들어, 특정 요소에서 발생한 이벤트가 상위 요소로 전파되어야 하는 경우가 있는데, `stopPropagation()`을 사용하면 이러한 동작을 막게 됩니다. 이는 예외적인 상황을 처리하기 어렵게 만들 수 있습니다. 
2. 다른 이벤트 핸들러의 중단: 이벤트 전파를 막으면 상위 요소에 연결된 다른 이벤트 핸들러도 실행되지 않습니다. 이는 웹 애플리케이션에서 다양한 기능을 구현하는 데 제한을 줄 수 있습니다. 
3. 코드의 가독성과 유지보수성 저하: 모든 이벤트에 `stopPropagation()`을 사용하면 코드가 복잡해지고, 이벤트의 흐름을 파악하기 어려워집니다. 이는 코드의 가독성과 유지보수성을 저하시킬 수 있습니다.

 따라서, 일반적으로는 이벤트 전파를 적절하게 활용하고, 필요한 경우에만 `stopPropagation()`을 사용하여 예상치 못한 동작을 방지하는 것이 좋습니다. 이벤트 전파를 적절하게 이해하고 활용함으로써 코드의 명확성과 유연성을 유지할 수 있습니다. 필요한 경우에는 특정 요소에서 이벤트 전파를 중단하고 싶을 때에만 `stopPropagation()`을 사용하는 것이 바람직합니다. 이를 통해 코드의 가독성과 유지보수성을 향상시킬 수 있습니다.

<br>

<br>

#### 참고링크: [Examples - Web API | MDN (mozilla.org)](https://developer.mozilla.org/ko/docs/Web/API/Document_Object_Model/Examples#example_5_event_propagation)

<br>

👨‍🏫 **With ChatGPT** 💻

<br>