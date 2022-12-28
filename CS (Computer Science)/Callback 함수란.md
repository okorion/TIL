#### Callback 함수란 도대체 무엇인가?

StackOverflow의 한 이용자의 답변을 인용하겠다.

 

A callback function is a function which is:

- passed as an argument to another function, and,
- is invoked after some kind of event.

간단명료한 답변이다.

 

즉, 콜백 함수란

\1. 다른 함수의 인자로써 이용되는 함수.

\2. 어떤 이벤트에 의해 호출되어지는 함수.



#### 예제 코드 1

```
// The callback method
function meaningOfLife() {
    log("The meaning of life is: 42");
}


// A method which accepts a callback method as an argument
// takes a function reference to be executed when printANumber completes
function printANumber(int number, function callbackFunction) {
    print("The number you provided is: " + number);
}

// Driver method
function event() {
   printANumber(6, meaningOfLife);
}
```

 

슈도 코드를 별로 좋아하는 편은 아니지만... 딱히 이해하기에 어렵지 않은 코드이기 때문에 그대로 인용하겠다.

 

printANumber()의 두 번째 매개변수로 function 타입의 callbackFunction을 인자로 받는다.

 

event()내부에서 printANumber(6, meaningOfLife); 를 하고 있는데,

meaningOfLife는 printANumber의 매개변수인 callbackFunction에 전달된다.

 

따라서 meaningOfLife는 위에서 밝힌 1번 정의(다른 함수의 인자로써 이용되는 함수)에 부합하여 callback 함수라고 할 수 있다.

 

https://stackoverflow.com/questions/824234/what-is-a-callback-function





출처: https://satisfactoryplace.tistory.com/18