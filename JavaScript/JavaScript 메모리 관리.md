# (번역) 🔥 자바스크립트 메모리 관리: 일반적인 메모리 누수를 방지하고 성능을 개선하는 방법

원문: [JavaScript Memory Management: How to Avoid Common Memory Leaks and Improve Performance](https://itnext.io/javascript-memory-management-how-to-avoid-common-memory-leaks-and-improve-performance-c018dbbca954)

<br>

애플리케이션을 최적화하는 데 도움이 되는 JS의 메모리 관리에 대해 설명합니다.

![javascript memory leak](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*bCpGATft8RX8_SfH8WMcoQ.png)

<br>

## 목차

- [도입](https://ykss.netlify.app/translation/javascript_memory_management/#도입)
- [자바스크립트 메모리 관리의 이해](https://ykss.netlify.app/translation/javascript_memory_management/#자바스크립트-메모리-관리의-이해)
  - [1. 가비지 컬렉터](https://ykss.netlify.app/translation/javascript_memory_management/#1-가비지-컬렉터)
  - [2. 스택 vs 힙](https://ykss.netlify.app/translation/javascript_memory_management/#2-스택-vs-힙)
- [메모리 누수의 일반적인 원인](https://ykss.netlify.app/translation/javascript_memory_management/#메모리-누수의-일반적인-원인)
  - [1. 순환 참조](https://ykss.netlify.app/translation/javascript_memory_management/#1-순환-참조)
  - [2. 이벤트 리스너](https://ykss.netlify.app/translation/javascript_memory_management/#2-이벤트-리스너)
  - [3. 전역 변수](https://ykss.netlify.app/translation/javascript_memory_management/#3-전역-변수)
- [수동 메모리 관리 모범 사례](https://ykss.netlify.app/translation/javascript_memory_management/#수동-메모리-관리-모범-사례)
  - [1. 약한 참조 사용](https://ykss.netlify.app/translation/javascript_memory_management/#1-약한-참조-사용)
  - [2. 가비지 컬렉터 API 사용](https://ykss.netlify.app/translation/javascript_memory_management/#2-가비지-컬렉터-API-사용)
  - [3. 힙 스냅샷과 프로파일러 사용하기](https://ykss.netlify.app/translation/javascript_memory_management/#3-힙-스냅샷과-프로파일러-사용하기)
- [결론](https://ykss.netlify.app/translation/javascript_memory_management/#결론)

<br>

## 도입

웹 개발자는 작성하는 모든 코드가 애플리케이션의 성능에 영향을 미칠 수 있다는 것을 알고 있습니다. 자바스크립트에서 집중해야 할 가장 중요한 영역 중 하나는 메모리 관리입니다.

사용자가 웹사이트와 상호작용할 때마다 새로운 객체, 변수, 함수가 생성된다고 생각해보세요. 주의하지 않으면 이러한 객체가 쌓여 브라우저의 메모리를 막고 전체 사용자 경험을 느리게 만들 수 있습니다. 이는 마치 정보 고속도로의 교통 체증과 같아서 사용자를 이탈하게 만드는 답답한 병목 현상입니다.

이러한 현상을 꼭 겪을 필요는 없습니다. 올바른 지식과 기술을 활용하면 자바스크립트 메모리를 제어하고, 애플리케이션이 원활하고 효율적으로 실행되도록 할 수 있습니다. 이 글에서는 메모리 누수의 일반적인 원인과 이를 방지하기 위한 전략을 포함해 자바스크립트 메모리 관리의 전반적인 내용을 살펴봅니다. 전문가든 초보 개발자든 깔끔하고 간결하며 빠른 코드를 작성하는 방법을 더 깊이 이해하게 될 것입니다.

<br>

<br>

## 자바스크립트 메모리 관리의 이해

### 1. 가비지 컬렉터

자바스크립트 엔진은 **가비지 컬렉터**를 사용하여 더 이상 사용하지 않는 메모리를 확보합니다. 가비지 컬렉터의 역할은 애플리케이션에서 더 이상 사용하지 않는 객체를 식별하고 제거하는 것입니다. 가비지 컬렉터는 코드의 *객체*와 *변수*를 지속적으로 *모니터링하고* 어떤 객체가 여전히 *참조되고* 있는지 추적하여 이를 수행합니다. 가비지 컬렉터는 사용되지 않는 객체를 삭제할 대상으로 표시하고 객체가 사용 중이던 메모리를 확보합니다.

가비지 컬렉터는 ”**표시(mark) 및 정리(sweep)**“라는 기술을 사용하여 메모리를 관리합니다. 아직 사용 중인 모든 객체를 표시한 다음, 힙을 ’**정리**‘하여 사용중으로 표시되지 않은 객체를 모두 제거합니다. 이 프로세스는 주기적으로 수행되며 힙의 메모리가 부족할 때도 수행되어 애플리케이션의 메모리 사용량이 항상 최대한 효율적으로 유지되도록 합니다.

<br>

### 2. 스택 vs 힙

자바스크립트에서 메모리는 **스택**과 **힙**이라는 두 가지 주요 요소가 있습니다.

**스택**은 *함수*를 실행하는 동안에만 필요한 데이터를 저장하는 데 사용됩니다. 빠르고 *효율적*이지만 *용량이 제한*되어 있습니다. 함수가 호출되면 *자바스크립트 엔진은 함수의 변수와 매개변수를 스택으로 밀어넣고, 함수가 반환되면 다시 스택에서 꺼냅니다.* 스택은 빠른 액세스와 빠른 메모리 관리를 위해 사용됩니다.

반면 **힙**은 *애플리케이션의 전체 수명* 동안 필요한 데이터를 저장하는 데 사용됩니다. 스택보다 *조금 느리고 덜 체계적*이지만 용량이 훨씬 큽니다. 힙은 여러 번 액세스해야 하는 *객체*, *배열* 및 기타 *복잡한 데이터 구조*를 저장하는 데 사용됩니다.

<br>

## 메모리 누수의 일반적인 원인

메모리 누수는 애플리케이션에 잠입해 성능 문제를 일으키는 교활한 적이 될 수 있다는 것을 잘 알고 계실 것입니다. 메모리 누수의 일반적인 원인을 이해하면 메모리 누수를 방지하는 데 도움이 될 수 있습니다.

<br>

### 1. 순환 참조

메모리 누수의 가장 일반적인 원인 중 하나는 **순환 참조**입니다. 순환 참조는 두 개 이상의 *객체가 서로를 참조*하여 가비지 컬렉터가 끊을 수 없는 순환을 생성할 때 발생합니다. 이로 인해 객체가 더 이상 필요하지 않게 되어도 오랫동안 메모리에 유지될 수 있습니다. 다음은 예시입니다.

<br>

```js
let object1 = {};
let object2 = {};

// 객체1과 객체2 사이에 순환 참조를 생성합니다.
object1.next = object2;
object2.prev = object1;

// object1과 object2로 무언가를 수행합니다.
// ...

// 순환 참조를 끊으려면 object1과 object2를 null로 설정합니다.
object1 = null;
object2 = null;
```

<br>이 예제에서는 `object1`과 `object2`라는 두 개의 객체를 생성하고 `next` 및 `prev` 프로퍼티를 추가하여 두 객체 사이에 순환 참조를 생성합니다. 그런 다음 `object1`과 `object2`를 `null`로 설정하여 순환 참조를 끊지만, 가비지 컬렉터가 순환 참조를 끊을 수 없기 때문에 객체가 더 이상 필요하지 않은 후에도 오랫동안 메모리에 유지되어 메모리 누수가 발생합니다.

<br>

이러한 유형의 메모리 누수를 방지하려면 자바스크립트의 `delete` 키워드를 사용하여 순환 참조를 생성하는 프로퍼티를 제거하는 `"수동 메모리 관리"`라는 기술을 사용할 수 있습니다.

<br>

```js
delete object1.next;
delete object2.prev;
```

이러한 유형의 메모리 누수를 방지하는 또 다른 방법은 객체와 변수에 대한 약한 참조를 생성할 수 있는 `WeakMap`과 `WeakSet`을 사용하는 것입니다. [이 옵션에 대한 자세한 내용은 이 글의 뒷부분에서 확인할 수 있습니다.](https://ykss.netlify.app/translation/javascript_memory_management/#1-약한-참조-사용)

<br>

### 2. 이벤트 리스너

메모리 누수의 또 다른 일반적인 원인은 **이벤트 리스너**입니다. 이벤트 리스너를 *요소에 연결*하면 리스너 함수에 대한 *참조가 생성*되어 가비지 컬렉터가 요소에서 사용하는 메모리를 확보하지 못하게 할 수 있습니다. 요소가 더 이상 필요하지 않을 때 리스너 함수를 제거하지 않으면 메모리 누수가 발생할 수 있습니다. 아래 예시를 참조하세요.

<br>

```js
let button = document.getElementById('my-button');

// 버튼 요소에 이벤트 리스너를 붙입니다.
button.addEventListener('click', function() {
  console.log('Button was clicked!');
});

// 버튼이 무언가 동작을 합니다.
// ...

// DOM에서 버튼을 제거합니다.
button.parentNode.removeChild(button);
```

<br>이 예제에서는 버튼 요소에 이벤트 리스너를 연결한 다음 DOM에서 버튼을 제거합니다. 버튼 요소가 더 이상 문서에 없지만 이벤트 리스너는 여전히 연결되어 있으므로 리스너 함수에 대한 참조가 생성되어 **가비지 컬렉터**가 요소에서 사용하는 메모리를 확보하지 못합니다. 요소가 더 이상 필요하지 않을 때 리스너 함수를 제거하지 않으면 메모리 누수가 발생할 수 있습니다.

<br>

이러한 유형의 메모리 누수를 방지하려면 요소가 더 이상 필요하지 않을 때 이벤트 리스너를 제거하는 것이 중요합니다.

<br>

```js
button.removeEventListener('click', function() {
  console.log('Button was clicked!');
});
```

<br>또 다른 방법은 특정 이벤트 대상에 추가된 모든 이벤트 리스너를 제거하는 `EventTarget.removeAllListeners()` 메서드를 사용하는 것입니다.

<br>

```js
button.removeAllListeners();
```

<br>

### 3. 전역 변수

메모리 누수의 세 번째 일반적인 원인은 전역 변수입니다. **전역 변수**를 생성하면 코드의 어느 위치에서나 접근할 수 있으므로 더 이상 필요하지 않은 시점을 판단하기 어려울 수 있습니다. 이로 인해 변수가 필요하지 않게 되어도 오랫동안 메모리에 유지될 수 있습니다. 예를 들어 보겠습니다.

<br>

```js
// 전역 변수를 선언합니다.
let myData = {
  largeArray: new Array(1000000).fill('some data'),
  id: 1,
};

// myData 변수로 무언가를 수행합니다.
// ...

// 참조를 끊기 위해 myData를 null로 설정합니다.
myData = null;
```

<br>이 예제에서는 전역 변수 `myData`를 생성하고 그 안에 대량의 데이터 배열을 저장합니다. 그런 다음 참조를 끊기 위해 `myData`를 `null`로 설정했지만 변수가 전역이므로 코드의 어느 위치에서나 여전히 접근할 수 있습니다. 더 이상 필요하지 않은 시점을 판단하기 어렵기 때문에, 변수가 더 이상 필요하지 않음에도 오랫동안 메모리에 유지되어 메모리 누수를 일으킬 수 있습니다.

<br>

이러한 유형의 메모리 누수를 방지하려면 `"함수 스코핑"` 기법을 사용할 수 있습니다. 이 기법은 함수를 생성하고 해당 함수 내에서 변수를 선언하여 해당 *함수의 스코프* 내에서만 접근할 수 있도록 하는 것입니다. 이렇게 하면 함수가 더 이상 필요하지 않게 될 때, 변수가 자동으로 가비지 컬렉팅됩니다.

<br>

```js
function myFunction() {
  let myData = {
    largeArray: new Array(1000000).fill('some data'),
    id: 1,
  };

  // myData 변수로 무언가를 수행합니다.
  // ...
}
myFunction();
```

<br>또 다른 방법은 `var` 대신 자바스크립트의 `let`과 `const`를 사용하여 *블록 스코프 변수*를 생성하는 것입니다. `let`과 `const`로 선언된 변수는 해당 변수가 정의된 블록 내에서만 접근할 수 있으며 스코프를 벗어나면 자동으로 가비지 컬렉팅됩니다.

<br>

```js
{
  let myData = {
    largeArray: new Array(1000000).fill('some data'),
    id: 1,
  };

  // myData 변수로 무언가를 수행합니다.
  // ...
}
```

<br>

## 수동 메모리 관리 모범 사례

자바스크립트는 애플리케이션의 메모리 사용량을 관리하는 데 도움이 되는 메모리 관리 도구와 기법을 제공합니다.

<br>

### 1. 약한 참조 사용

자바스크립트에서 가장 강력한 메모리 관리 도구 중 하나는 `WeakMap`과 `WeakSet`입니다. 이들은 *객체와 변수에 대한 약한 참조*를 생성할 수 있는 특수 데이터 구조입니다. 약한 참조는 **가비지 컬렉터**가 객체가 사용하는 메모리를 확보하지 못하도록 막는다는 점에서 일반 참조와 다릅니다. 따라서 순환 참조로 인한 메모리 누수를 방지하는 데 유용한 도구입니다. 다음은 예시입니다.

<br>

```js
let object1 = {};
let object2 = {};

// WeakMap을 생성합니다.
let weakMap = new WeakMap();

// object1을 WeakMap에 추가한 다음
// object1에 WeakMap을 추가하여 순환 참조를 생성합니다.
weakMap.set(object1, 'some data');
object1.weakMap = weakMap;

// weakSet을 생성하고 object2를 추가합니다.
let weakSet = new WeakSet();
weakSet.add(object2);

// 이 경우 가비지 컬렉터는 object1과 object2가 사용하는 메모리를 확보할 수 있습니다.
// object1 과 object2의 참조가 약하기 때문입니다.
```

<br>이 예제에서는 `object1`과 `object2`라는 두 개의 객체를 생성하고 각각 `WeakMap`과 `WeakSet`에 추가하여 이들 사이에 순환 참조를 생성합니다. 이러한 객체에 대한 참조가 약하기 때문에 가비지 컬렉터는 객체가 계속 참조되고 있음에도 불구하고 객체가 사용하는 메모리를 확보할 수 있습니다. 이렇게 하면 순환 참조로 인한 메모리 누수를 방지하는 데 도움이 될 수 있습니다.

<br>

### 2. 가비지 컬렉터 API 사용

또 다른 메모리 관리 기법은 **가비지 컬렉터 API**를 사용하여 수동으로 가비지 컬렉션을 트리거하고 힙의 현재 상태에 대한 정보를 얻는 것입니다. 이는 메모리 누수 및 성능 문제를 디버깅하는 데 유용합니다. 다음은 예시입니다.

<br>

```js
let object1 = {};
let object2 = {};

// object1과 object2 사이에 순환 참조를 만듭니다.
object1.next = object2;
object2.prev = object1;

// 수동으로 가비지 컬렉터를 호출합니다.
gc();
```

<br>이 예제에서는 `object1`과 `object2`라는 두 개의 객체를 생성하고 `next` 및 `prev` 프로퍼티를 추가하여 두 객체 사이에 순환 참조를 생성합니다. 그런 다음 `gc()` 함수를 사용하여 가비지 컬렉션을 수동으로 트리거하면 객체가 계속 참조되고 있음에도 불구하고 객체가 사용하는 메모리를 확보할 수 있습니다.

<br>

`gc()` 함수는 모든 자바스크립트 엔진에서 지원되는 것은 아니며, 엔진에 따라 동작이 다를 수 있다는 점에 유의해야 합니다. 또한 가비지 컬렉션을 수동으로 트리거하면 *성능에 영향을 미칠 수 있으므로* 필요한 경우에만 사용하는 것이 좋습니다.

<br>

자바스크립트는 `gc()` 함수 외에도 자바스크립트 엔진의 `global.gc()` 함수와 일부 브라우저 엔진의 `performance.gc()` 함수를 제공합니다. 이 함수들은 힙의 현재 상태를 확인하고 가비지 컬렉션 프로세스의 성능을 측정하는 데 사용할 수 있습니다.

<br>

### 3. `힙 스냅샷과` 프로파일러 사용하기

자바스크립트는 애플리케이션이 메모리를 사용하는 방식을 이해하는 데 도움이 되는 **힙 스냅샷**과 **프로파일러**도 제공합니다. **힙 스냅샷**을 사용하면 힙의 현재 상태를 스냅샷으로 찍고 이를 분석하여 어떤 객체가 가장 많은 메모리를 사용하는지 확인할 수 있습니다.

다음은 힙 스냅샷을 사용하여 애플리케이션의 메모리 누수를 식별하는 방법에 대한 예시입니다.

<br>

```js
// 힙 스냅샷을 시작합니다.
let snapshot1 = performance.heapSnapshot();

// 메모리 누수를 유발하는 어떤 동작을 수행합니다.
for (let i = 0; i < 100000; i++) {
  myArray.push({
    largeData: new Array(1000000).fill('some data'),
    id: i,
  });
}

// 다른 힙 스냅샷을 실행합니다.
let snapshot2 = performance.heapSnapshot();

// 두 스냅샷을 비교하여 어떤 객체가 생성되었는지 확인합니다.
let diff = snapshot2.compare(snapshot1);

// 차이를 분석하여 어떤 객체가 가장 많은 메모리를 사용하는지 확인 합니다.
diff.forEach(function(item) {
  if (item.size > 1000000) {
    console.log(item.name);
  }
});
```

<br>이 예제에서는 대용량 데이터를 배열로 푸시하는 루프를 실행하기 전후에 두 개의 힙 스냅샷을 생성한 다음, 두 스냅샷을 비교하여 루프 중에 생성된 객체들을 확인합니다. 그런 다음 차이를 분석하여 어떤 객체가 가장 많은 메모리를 사용하는지 확인할 수 있으며, 이를 통해 대용량 데이터로 인한 메모리 누수를 식별하는 데 도움이 될 수 있습니다.

<br>

**프로파일러**를 사용하면 애플리케이션의 성능을 추적하고 메모리 사용량이 많은 영역을 식별할 수 있습니다.

<br>

```js
let profiler = new Profiler();

profiler.start();

// 메모리 누수를 유발하는 어떤 동작을 수행합니다.
for (let i = 0; i < 100000; i++) {
  myArray.push({
    largeData: new Array(1000000).fill('some data'),
    id: i,
  });
}

profiler.stop();

let report = profiler.report();

// 보고서를 분석하여 메모리 사용량이 많은 영역을 식별합니다.
for (let func of report) {
  if (func.memory > 1000000) {
    console.log(func.name);
  }
}
```

<br>이 예제에서는 자바스크립트 **프로파일러**를 사용하여 애플리케이션의 성능 추적을 시작 및 중지하고 있습니다. 보고서에는 호출된 함수와 각 함수에 대한 메모리 사용량에 대한 정보가 표시됩니다.

**힙 스냅샷**과 **프로파일러**는 모든 자바스크립트 엔진과 브라우저에서 지원되는 것은 아니므로 애플리케이션에서 사용하기 전에 호환성을 확인하는 것이 중요합니다.

<br>

## 결론

이제까지 가비지 컬렉션 프로세스, 다양한 메모리 유형, 자바스크립트에서 사용할 수 있는 메모리 관리 도구와 기법 등 자바스크립트 메모리 관리의 기본을 살펴보았습니다. 또한 메모리 누수의 일반적인 원인에 대해 설명하고 이를 방지하는 방법에 대한 예시를 제공했습니다.

이러한 메모리 관리 모범 사례를 이해하고 구현하는 데 시간을 투자하면 메모리 누수 가능성을 줄이며 애플리케이션을 만들어낼 수 있습니다. 이 글이 도움이 되었다면 **박수**를 보내주셔서 응원해주시고, Medium에서 저를 **팔로우**하여 기술을 한 단계 더 발전시키는 데 도움이 되는 새로운 글과 학습 기회에 대한 최신 소식을 받아보세요.

<br>

<br>

<br>

#### 참고링크: [(번역) 🔥 자바스크립트 메모리 관리: 일반적인 메모리 누수를 방지하고 성능을 개선하는 방법 | Ykss](https://ykss.netlify.app/translation/javascript_memory_management/)

<br>