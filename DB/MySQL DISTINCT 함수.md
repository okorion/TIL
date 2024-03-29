## `SELECT DISTINCT`

중복된 값을 없애기 위해서 `DISTINCT`를 사용합니다. `GROUP BY`를 사용했을 때와 거의 동일한 방식으로 처리됩니다. 다만 `DISTINCT`는 정렬이 되지 않는다는 차이 정도가 있습니다.

```
SELECT DISTINCT emp_no FROM salaries;
SELECT emp_no FROM salaries GROUP BY emp_no;
```

그리고 `DISTINCT`를 사용하면서 많은 사람들이 헷갈리는 부분이 있습니다. 바로 `DISTINCT`는 SELECT 되는 레코드를 유니크하게 SELECT 하는 것이지 컬럼을 유니크하게 조회하는 것이 아니라는 것입니다.

<br>

예를들면 아래와 같은 쿼리를 보겠습니다.

```
SELECT DISTINCT first_name, last_name FROM employees;
```

위의 쿼리는 first_name만 유니크한 값을 가져오는 것이 아니라 (first_name + last_name) 전체가 유니크한 레코드를 가져오는 것입니다. 또 다른 하나의 예시 쿼리를 보겠습니다.

<br>

```
SELECT DISTINCT (first_name), last_name FROM employees;
```

이번에는 `first_name`에 괄호를 넣었는데요. 이렇게 되면 first_name만 유니크한 결과를 가져오게 되는 것이라고 생각할 수 있지만, 이것도 `(first_name + last_name)`이 유니크한 값을 가져오게 되는 것입니다. 즉, 괄호는 의미가 없는 것입니다. (어떻게 보면 당연한 것이지만.. 헷갈릴 수 있는 부분이니 잘 생각하고 있으면 좋을 거 같습니다.)

<br>

<br>

<br>

#### 참고링크: https://devlog-wjdrbs96.tistory.com/359

<br>