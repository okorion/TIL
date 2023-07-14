# 🧆 isNaN() 함수로 NaN 체크하기

자바스크립트 `isNaN()` 함수는 숫자가 아닌 대상은 true, 숫자면 false를 반환합니다. isNaN(‘숫자’)는 숫자로 인식되므로 false입니다. isNaN(”) 및 isNaN(‘ ‘)은 각각 0으로 인식되어 false입니다.

<br>

`isNaN()` 함수는 숫자가 아닌 값을 찾는 함수입니다. 인수가 숫자가 아니면(Not a Number) True를 반환합니다. 인수가 숫자이면 False를 반환합니다.

<br>

isNaN(‘456’) 과 같은 문자형 숫자도 숫자 인식되어 false를 반환합니다. isNaN(‘4 * 5’)의 * 기호와 같은 연산 기호는 ” 따옴표 안에서는 문자 처리되므로 true를 반환합니다.

<br>

```
<script>
	var num1 = isNaN(456);            //숫자
	var num2 = isNaN('456');          //숫자
	var num3 = isNaN('가나다');       //문자
	var num4 = isNaN(4.56);           //소수점
	var num5 = isNaN('4.56');         //'소수점'
	var num6 = isNaN(4 * 5);          //숫자 연산
	var num7 = isNaN('4 * 5');        //'숫자 연산'
	var num8 = isNaN('');             //빈 문자 = 0
	var num9 = isNaN(' ');            //공백 = 0
	var num10 = isNaN(true);          //논리형 자료 = 1
	var num11 = isNaN(false);         //논리형 자료 = 0

	document.write("isNaN(456) = " + num1 + "<br>");
	document.write("isNaN('456') = " + num2 + "lgt;br>");
	document.write("isNaN('가나다') = " + num3 + "<br>");
	document.write("isNaN(4.56) = " + num4 + "<br>");
	document.write("isNaN('4.56') = " + num5 + "<br>");
	document.write("isNaN(4 * 5) = " + num6 + "<br>");
	document.write("isNaN('4 * 5') = " + num7 + "<br>");
	document.write("isNaN('') = " + num8 + "<br>");
	document.write("isNaN(' ') = " + num9 + "<br>");
	document.write("isNaN(true) = " + num10 + "<br>>");
	document.write("isNaN(false) = " + num11 + "<br>");
</script>
```



<br>결과

```
isNaN(456) = false
isNaN('456') = false
isNaN('가나다') = true
isNaN(4.56) = false
isNaN('4.56') = false
isNaN(4 * 5) = false
isNaN('4 * 5') = true
isNaN('') = false
isNaN(' ') = false
isNaN(true) = false
isNaN(false) = false
```



<br>

isNaN(”) 및 isNaN(‘ ‘) 같은 빈 문자 또는 공백은 숫자 0 처리되므로 false를 반환합니다. isNaN(true)와 isNaN(false) 같은 논리형은 각각 숫자 1과 0을 나타내므로 역시 `NaN`이 아닙니다.



<br>

<br>

#### 참고자료: https://dasima.xyz/%EC%9E%90%EB%B0%94%EC%8A%A4%ED%81%AC%EB%A6%BD%ED%8A%B8-isnan-%ED%95%A8%EC%88%98-nan-%EC%B2%B4%ED%81%AC/

<br>