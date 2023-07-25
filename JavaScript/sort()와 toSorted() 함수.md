# 🏁 sort()와 toSorted() 함수

<iframe src="https://www.youtube.com/embed/FcLaq6JY-zg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen="" style="box-sizing: inherit; margin: 0px; padding: 0px; border: 0px; font: inherit; vertical-align: baseline; top: 0px; left: 0px; width: 700px; height: 393.75px;"></iframe>



<br>배열 안의 값들을 원하는 순서로 정렬하는 것은 백엔드 프런트엔드 가라지 않고 빈번하게 필요한 작업인데요. 자바스크립트에서 배열을 정렬할 때는 `sort()` 함수나 `toSorted()` 함수를 사용합니다.

이번 글에서는 이 두 함수를 사용하여 자바스크립트에서 배열을 정렬하는 기본적인 방법과 주의해야 할 부분에 대해서 알아보겠습니다.

## 배열의 sort() 함수

자바스크립트에서 배열을 정렬을 하는 가장 유명한 방법은 뭐니뭐니 해도 `sort()` 함수일텐데요.

배열을 상대로 `sort()` 함수를 호출하면 해당 배열 내의 값들이 오름차순으로 정렬됩니다.

```js
[3, 1, 2].sort();
// [1, 2, 3]
```



<br>`sort()` 함수는 원래 배열 내에 값들을 재배치하며 정렬한 배열을 다시 반환합니다.

```js
const nums = [3, 1, 2];
const sortedNums = nums.sort();
console.log({ nums, sortedNums });
```

결과

```js
{
  nums: [1, 2, 3],
  sortedNums: [1, 2, 3]
}
```



<br>즉 `sort()` 함수가 반환한 배열은 `sort()` 함수를 호출한 원래 배열과 동일합니다.

```js
nums === sortedNums; // true
```



<br>

<br>

## 흔히 하는 실수

많은 개발자 분들이 `sort()` 함수를 사용하실 때 중요한 부분을 간과하시다가 당혹스러운 경험을 하시게 되는데요. **바로 정렬하기 전에 배열 내의 값을 내부적으로 문자열로 변환한다는 사실입니다.**

이 부분 때문에 특히 숫자로 이뤄진 배열을 정렬할 때는 정말로 엉뚱한 결과를 얻을 수 있습니다.

예를 들어, 다음 숫자 배열을 `sort()` 함수로 정렬해보면 다음과 같이 예상치 못한 결과를 얻게 됩니다.

```js
[100, 3, 1, 20].sort();
// [1, 100, 20, 3]
```

문자열 대소비교에서는 숫자처럼 자리수는 중요하지 않으며 첫 번째 글자가 크면 뒤에 아무리 더 큰 글자가 있어도 결과에 영향을 주지 않죠?



<br>게다가 `sort()` 함수로 정렬한 배열이 음수를 포함하고 있다면 더욱 혼란스러운 결과를 얻을 수 있는데요.

```js
[-3, 2, 0, 1, 3, -2, -1].sort();
// [-1, -2, -3, 0, 1, 2, 3]
```

문자열에서 마이너스 기호도 특별할 거 없는 단지 하나의 문자일 뿐이기 때문에 이러한 결과가 나오는 것이지요.



<br>

<br>

## 숫자 배열 정렬

그럼 숫자 배열을 제대로 정렬하려면 어떻게 해야할까요?

`sort()` 함수는 인자로 정렬 기준을 나타내는 콜백 함수를 함수를 받는데요. 이 대소비교를 위한 함수에는 2개의 인자가 넘어오며 다음과 같은 규칙을 따라야 합니다.

- 첫 번째 인자가 두 번째 인자보다 작으면 음수를 반환
- 첫 번째 인자가 두 번째 인자보다 크면 양수를 반환
- 첫 번째 인자가 두 번째 인자와 같으면 `0`을 반환

따라서 숫자 배열을 제대로 오름차순 정렬하기 위해서는 첫 번째 인자에서 두 번째 인자를 빼줍니다.

```js
[-3, 2, 0, 1, 3, -2, -1].sort((a, b) => a - b);
// [-3, -2, -1, 0, 1,  2,  3]
```



<br>반대로 숫자 배열을 내림차순으로 정렬하고 싶다면 피연산자의 순서를 바꿔줘야겠죠?

```js
[-3, 2, 0, 1, 3, -2, -1].sort((a, b) => b - a);
// [3, 2, 1, 0, -1, -2, -3]
```



<br>

<br>

## 객체 배열 정렬

실제 웹 애플리케이션을 개발할 때는 단순한 숫자나 문자보다는 복잡한 객체 배열을 정렬해야할 때가 더 많을 텐데요.

<br>

예를 들어, 아래와 같이 번호와 코드, 이름으로 이루어진 국가 배열이 있다고 가정해보겠습니다.

```js
const countries = [
  { no: 1, code: "KR", name: "Korea" },
  { no: 2, code: "CA", name: "Canada" },
  { no: 3, code: "US", name: "United States" },
  { no: 4, code: "GB", name: "United Kingdom" },
  { no: 5, code: "CN", name: "China" },
];
```

이 배열을 상대로 `sort()` 함수를 호출하면 아무 일도 일어나지 않는 것을 볼 수 있습니다. 구체적으로 어떤 기준에 의해서 객체 간에 대소비교를 해야하는지 정해주지 않았기 때문입니다.



<br>좀 더 엄밀히 얘기하면 자바스크립트에서 객체를 문자열로 변환하면 `[object Object]`가 되어 배열 내의 모든 객체의 크기가 동일하다고 판단되는 것이죠.

```js
countries.sort();
/**
[
  { no: 1, code: "KR", name: "Korea" },
  { no: 2, code: "CA", name: "Canada" },
  { no: 3, code: "US", name: "United States" },
  { no: 4, code: "GB", name: "United Kingdom" },
  { no: 5, code: "CN", name: "China" },
]
*/
```



<br>그럼 국가 코드 기준으로 오름차순 정렬해볼까요? 숫자가 아니기 때문에 뺄샘을 하는 대신에 문자열의 `localeCompare()` 함수를 사용하고 있습니다.

```js
countries.sort((a, b) => a.code.localeCompare(b.code));
/**
[
  { no: 2, code: 'CA', name: 'Canada' },
  { no: 5, code: 'CN', name: 'China' },
  { no: 4, code: 'GB', name: 'United Kingdom' },
  { no: 1, code: 'KR', name: 'Korea' },
  { no: 3, code: 'US', name: 'United States' }
]
*/
```



<br>이번에는 국가 번호를 기준으로 내림차순 정렬을 해볼까요?

```js
countries.sort((a, b) => b.no - a.no);
/**
[
  { no: 5, code: "CN", name: "China" },
  { no: 4, code: "GB", name: "United Kingdom" },
  { no: 3, code: "US", name: "United States" },
  { no: 2, code: "CA", name: "Canada" },
  { no: 1, code: "KR", name: "Korea" },
]
*/
```



<br>

<br>

## 다중 기준 정렬

좀 더 큰 데이터 세트를 다룰 때는 하나의 기준이 아닌 우선 순위에 따라 여러 기준으로 배열을 정렬해야할 때도 있는데요. 대표적인 사례로 정렬이 가능한 여러 칼럼으로 이루어진 테이블 UI를 들 수 있겠습니다.



<br>예를 들어 다양한 속성을 가진 사용자들을 담은 배열을 성별을 기준으로 1차 내림차순 정렬하고, 나이 기준으로 2차 오름차순 정렬을 하려면 어떻게 해야할까요?

```js
const users = [
  {
    mail: "gregorythomas@gmail.com",
    name: "Brett Holland",
    gender: "M",
    age: 73,
  },
  {
    mail: "hintc12@hotmail.com",
    name: "Madison Martinez",
    gender: "F",
    age: 29,
  },
  {
    mail: "wwagner33@gmail.com",
    name: "Michael Jenkins",
    gender: "M",
    age: 51,
  },
  {
    mail: "ujacksonxejyen@gmail.com",
    name: "Amber Rhodes",
    gender: "F",
    age: 42,
  },
  {
    mail: "daniel7900@gmail.com",
    name: "Karen Rodriguez",
    gender: "F",
    age: 32,
  },
];
```



<br>이렇게 성별이 같을 때만 나이 기준으로 정렬하도록 대소비교 함수를 구현해주면 되겠죠?

```js
users.sort((a, b) => {
  if (a.gender === b.gender) {
    return a.age - b.age;
  } else {
    return b.gender.localeCompare(a.gender);
  }
});
/**
[
  {
    mail: "wwagner33@gmail.com",
    name: "Michael Jenkins",
    gender: "M",
    age: 51,
  },
  {
    mail: "gregorythomas@gmail.com",
    name: "Brett Holland",
    gender: "M",
    age: 73,
  },
  {
    mail: "hintc12@hotmail.com",
    name: "Madison Martinez",
    gender: "F",
    age: 29,
  },
  {
    mail: "daniel7900@gmail.com",
    name: "Karen Rodriguez",
    gender: "F",
    age: 32,
  },
  {
    mail: "ujacksonxejyen@gmail.com",
    name: "Amber Rhodes",
    gender: "F",
    age: 42,
  },
]
 */
```



<br>

<br>

## 배열의 toSorted() 함수

`sort()` 함수로 정렬을 할 때 원본 배열을 건드리지 않아야하는 경우에는 반드시 배열을 먼저 복제한 후에 배열 사본을 상대로 정렬을 해야하는데요.

```js
const nums = [3, 1, 2];
const sortedNums = [...nums].sort();
console.log({ nums, sortedNums });
```

결과

```js
{
  nums: [3, 1, 2],
  sortedNums: [1, 2, 3]
}
```



<br>그런데 요즘에는 더 이상 위와 같이 번거롭게 배열을 복제한 다음에 정렬할 필요가 없다는 것을 혹시 아시나요?

바로 최근에 자바스크립트 배열에 추가된 `toSorted()` 함수 덕분인데요. `sort()` 함수 대신에 이 함수를 사용하면 원본 배열을 건드리지 않고 정렬된 배열 사본을 바로 얻을 수 있습니다.

```js
const nums = [3, 1, 2];
const sortedNums = nums.toSorted();
console.log({ nums, sortedNums });
```

결과

```js
{
  nums: [3, 1, 2],
  sortedNums: [1, 2, 3]
}
```



<br>`toSorted()` 함수가 반환한 배열은 원래 배열과 다르다는 것도 확인할 수 있습니다.

```js
nums === sortedNums; // false
```

새로운 배열을 반환하다는 점을 제외하고는 `toSorted()` 함수의 사용법은 `sort()` 함수와 대동소이합니다. 즉, `sort()` 함수처럼 백 함수를 넘겨서 자유롭게 정렬 기준을 바꿀 수 있습니다.

참고로 `toSorted()` 함수는 인터넷 익스플로러를 제외한 대부분의 모던 브라우저에서 사용이 가능하며, Node.js에서는 v20부터 사용이 가능합니다.



<br>

## 마치면서

이상으로 자바스크립트에서 `sort()` 함수를 사용해서 여러 종류의 배열을 원하는 기준으로 정렬하는 법에 대해서 배워보았습니다. 또한 최근에 추가된 `toSorted()` 함수를 통해서 어떻게 원본 배열을 건드리지 않고 안전하게 정렬을 할 수 있는지도 살펴보았습니다.

자바스크립트에서 배열을 실수없이 자유자재로 정렬하시는데 본 글이 도움이 되었으면 좋겠습니다.

<br>

<br>

#### 참고링크: [자바스크립트 배열 정렬: sort()와 toSorted() 함수 | Engineering Blog by Dale Seo](https://www.daleseo.com/js-sort-to-sorted/)

<br>