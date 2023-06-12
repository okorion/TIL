## 🧋 onKeyPress/onKeyUp/onKeyDown 비교

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>enter event</title>
</head>
<body>
    
    <input type = "password" onkeypress="test(event)">
<script>
function test(event){
    if(event.keyCode==13){
        alert("enterkey");
    }
}

</script>
</body>
</html>
```

<br>

1. keyup

키보드에서 손을 땠을 때 실행

<br>

2. keydown

키보드를 눌렀을 때 실행

키보드를 누르고 있을 때 한번만 실행됨

<br>

3. keypress

키보드를 눌렀을 때 실행

키보드를 누르고 있을 때 계속 실행됨

 

\* Ctrl, Alt, Shift 키 등은 keydown에서는 작동하지만 keypress 에서 작동하지 않음

<br>

\* keyCode ASCII code 값

keydown, keyup에서는 a = 65, A = 65로 동일하게 보여짐

keypress에서는 a = 97, A = 65로 다른 값이 보여짐

 -> Caps Lock 여부 체크, 대소문자 구분을 통한 로직 작성 가능

 <br>

\* FireFox 에서의 버그

event.keyCode 가 파이어폭스에서 동작안할 수 있음 따라서 keyCode 사용 시 아래와 같이 사용하면 됨

 <br>

var keyCode = event.keyCode ? event.keyCode : event.which;

 <br>

출처: https://silver0r.tistory.com/119 [어흥]

<br>

<br>

#### 참고링크: [[Javascript\] onkeypress() / keyup, keypress, keydown (tistory.com)](https://ninetynine-2026.tistory.com/511)

<br>