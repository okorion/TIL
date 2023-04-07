### MySQL GROUP BY, HAVING 함수

<br>

그룹 함수를 사용하면 로우의 수, 총합, 평균, 최대, 최저 값을 가져올 수 있습니다. 

SELECT 문을 통해 가져온 모든 로우를 하나의 그룹으로 묶고 그 안에서 로우의 수, 총합, 평균, 최대, 최저 값을 구하는 것입니다.

Group by 절은 select 문을 통해 가져온 모든 로우를 개발자가 정한 기준에 따라 그룹으로 나눌 수 있습니다.

Group by 절을 이용해 그룹으로 나눈 후, 그룹 함수를 사용하면 각 그룹 내에서 로우의 수, 총합, 최대, 최저 값을 구할 수 있습니다 .

 <br>

```
# 사원의 수를 성별로 구분하여 가져온다.

select gender, count(*) from employees 
group by gender;
```

| M    | 179973 |
| ---- | ------ |
| F    | 120051 |

 <br>

 <br>

```
# 각 부서에 근무하고 있는 사원들의 수를 가져온다. 

select dept_no, count(*)
from dept_emp
where to_date = '9999-01-01'
group by dept_no;
```

| d001 | 14842 |
| ---- | ----- |
| d002 | 12437 |
| d003 | 12898 |
| d004 | 53304 |
| d005 | 61386 |

 <br>

 <br>

```
# 각 부서별 과거의 매니저의 수를 구한다

select dept_no, count(*)
from dept_manager
where to_date <> '9999-01-01';
```

| d001 | 15   |
| ---- | ---- |
|      |      |

 <br>

 <br>

```
# 급여 수령 시작일별 급여 총합을 구합니다.

select from_date, sum(salary)
from salaries
group by from_date;
```

| 1986-06-26 | 4642169  |
| ---------- | -------- |
| 1987-06-26 | 7298739  |
| 1988-06-25 | 10059890 |
| 1989-06-25 | 12873255 |
| 1990-06-25 | 15843392 |

 <br>

 <br>

```
# 급여 수령 시작일별 평균을 구합니다.

select from_date, avg(salary)
from salaries
group by from_date;
```

| 1986-06-26 | 52751.9205 |
| ---------- | ---------- |
| 1987-06-26 | 53667.1985 |
| 1988-06-25 | 54972.0765 |
| 1989-06-25 | 55970.6739 |
| 1990-06-25 | 56990.6187 |

 <br>

 <br>

```
# 급여 수령 시작일별 급여 최고액을 구합니다.

select from_date, max(salary)
from salaries
group by from_date;
```

| 1986-06-26 | 103344 |
| ---------- | ------ |
| 1987-06-26 | 106130 |
| 1988-06-25 | 108159 |
| 1989-06-25 | 96538  |
| 1990-06-25 | 98371  |

 <br>

 <br>

```
# 급여 수령 시작일별 급여 최적액을 구합니다.

select from_date, min(salary)
from salaries
group by from_date;
```

| 1986-06-26 | 39736 |
| ---------- | ----- |
| 1987-06-26 | 39563 |
| 1988-06-25 | 40000 |
| 1989-06-25 | 39765 |
| 1990-06-25 | 40000 |

 <br>

 <br>

 <br>

## having

group by 절을 이용하여 개발자가 정한 기준으로 그룹을 나눈 후 having 절로 만든 조건에 맞는 그룹의 데이터만 가져올 수 있습니다.

 <br>

```
# 10만명 이상이 사용하고 있는 직함의 이름과 지원의 수를 가지고 옵니다.

select title, count(*)
from titles
group by title
having count(*) >= 10000;
```

| Senior Engineer    | 97750  |
| ------------------ | ------ |
| Staff              | 107391 |
| Engineer           | 115003 |
| Senior Staff       | 92853  |
| Assistant Engineer | 15128  |

 <br>

 <br>

```
# 5만명 이상 근무하고 있는 부서의 부서 번호와 부서 소속 사원의 수를 가져옵니다.

select dept_no, count(*)
from dept_emp
group by dept_no
having count(*) >= 50000;
```

| d004 | 73485 |
| ---- | ----- |
| d005 | 85707 |
| d007 | 52245 |

<br>

<br>

<br>

#### 참고링크: [MySQL : group by, having : 개념, 예제, 사용법 (tistory.com)](https://jjeongil.tistory.com/942)

<br>