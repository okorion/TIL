## 🧮 CSS flexbox 속성 및 완벽 가이드

css에서의 flexbox는 보다 쉽게 레이아웃 구조를 잡을 수 있는 css 속성입니다.

flex 박스는 요소의 크기가 정확하지 않거나, 반응형일 때 유용하게 사용할 수 있습니다.

정렬, 방향, 크기, 순서 모두 css만으로 유연하게 조절할 수 있기때문에 다양한 레이아웃을 보다 쉽게 구현할 수 있습니다.

 



<br>

### **flexbox의 구성**



![img](https://blog.kakaocdn.net/dn/bW3fLC/btq3t32nwwH/KPYcK4aDm9yWNuPfEAWLCk/img.png)사진출처:sharkcoder



flexbox는 상위 부모요소인 flex container와, 자식 요소인 flex item으로 구성되어 있습니다.

 

<br>

#### **flexbox 기본 구조**

**[html]**

```
<div class="container">
    <div class="item">
        <p>Item1</p>
    </div>
    <div class="item">
        <p>Item2</p>
    </div>
    <div class="item">
        <p>Item3</p>
    </div>
    <div class="item">
        <p>Item4</p>
    </div>
</div>
```

**[css]**

```
.container {
  display: flex;
}
```

flexbox css 적용방법은 부모요소인 container에 display:flex를 선언하면 됩니다.

####  

<br>

#### **속성 구분**

flexbox는 부모요소인 **flex container**와 자식 요소인 **flex item**에 정의하는 속성이 다릅니다.

전체적인 정렬에 관련된 속성은 부모요소인 **flex container**에 정의하고,

자식 요소의 크기나 순서는 **flex item**에 정의합니다.

속성의 구분은 다음과 같습니다.

 

 **flex container(부모요소)**

- align-content
- align-items
- display
- flex-direction
- flex-flow
- flex-wrap
- justify-content

 

**flex item(자식요소)**

- align-self
- flex
- flex-basis
- flex-grow
- flex-shrink
- order

 

<br>

------

#### **부모요소 속성 : flex-direction 속성**

flex-direction은 플렉스 컨테이너 내의 아이템을 배치할 때, 주축 및 방향을 지정합니다.

```
/* 한 줄의 글을 작성하는 방향대로 */
{flex-direction: row;}

/* 역방향 */
{flex-direction: row-reverse;}

/* 세로 정렬 */
{flex-direction: column;}

/* 세로정렬 -> 역방향 */
{flex-direction: column-reverse;}

/* 전역 값 */
{flex-direction: inherit;}
{flex-direction: initial;}
{flex-direction: unset;}
```

 

 

**flex-direction: row 결과화면**



![img](https://blog.kakaocdn.net/dn/biCfUN/btq3zoxIMr5/Pitu3JL5cHmGOHSgGVjKak/img.png)



 

**flex-direction: row-reverse 결과화면**



![img](https://blog.kakaocdn.net/dn/zzJgk/btq3CzyxLUe/baiF6ALH5Rl8N0k7HBCPGK/img.png)



 

***\*flex-direction: column\** 결과화면**



![img](https://blog.kakaocdn.net/dn/ni7ET/btq3DFE26HJ/iKA7076r9URg0FchWzN2K1/img.png)



 

 

***\**\*flex-direction: column-reverse\*\* 결과화면\****



![img](https://blog.kakaocdn.net/dn/bJJ3yH/btq3xnl09hA/Ey2WwMYQUjeaReLXY1fsJ1/img.png)



 

 

 

 

<br>

 

#### **부모요소 속성 : flex-wrap**

flex-wrap 속성은 flex-item의 요소를 한줄로 배치할 것인지, 여러줄에 배치할 것인지 결정하는 속성입니다.

```
.container{flex-wrap: nowrap | flex-wrap: wrap | flex-wrap: wrap-reverse}
```

- nowrap : 한줄로 배치합니다. 부모요소를 넘어갈 수 있습니다.
- wrap : 부모요소의 크기에 벗어나지 않게 줄바꿈합니다. 정방향입니다.
- wrap-reverse : 부모오쇼에 크기에 벗어나지 않게 줄바꿈합니다. 역방향입니다.

**norwrap 결과화면**



![img](https://blog.kakaocdn.net/dn/c9MjmQ/btq3ySy8V06/krhJt95I4eo6wdEfwKxlVk/img.png)



 

***\*wrap 결과화면\****



![img](https://blog.kakaocdn.net/dn/2SCjz/btq3yT5NU4b/njYfPLwkGTVKSYxyWK8CN0/img.png)



 

**wrap-reverse**



![img](https://blog.kakaocdn.net/dn/VPlZ6/btq3yJWtn0S/Vb4SnJkoBUG3BAR0yOG6c0/img.png)



 

<br>

#### **부모요소 속성 : justify-content**

justify-content는 자동 여백을 사용해서 flex item의 간격을 조정할 수 있고, 시작과 끝을 정렬할 수 있습니다.

```
.container {
  justify-content: flex-start | flex-end | center | space-between | space-around | space-evenly;
}
```

- **flex-start :** 항목이 컨테이너의 왼쪽에서 시작합니다. (기본값).
- **flex-end :** 항목이 컨테이너의 오른쪽에서 시작됩니다.
- **center :** 항목이 **중앙** 에 배치됩니다.
- **space-between :** 항목이 줄에 균등하게 분포됩니다 (첫 번째 항목은 왼쪽에, 마지막 항목은 오른쪽에 있음).
- **space-around :** 항목이 항목의 양쪽에 동일한 공간을두고 일렬로 고르게 분포됩니다. 모든 항목의 양쪽에 동일한 공간이 있으므로 시각적으로 공간이 동일하지 않습니다. 인접한 플렉스 아이템의 여백은 축소되지 않습니다. 첫 번째 항목은 컨테이너 가장자리에 대해 한 단위의 공간을 갖지만 다음 항목에는 적용되는 자체 간격이 있기 때문에 다음 항목 사이에 두 단위의 공간이 있습니다.
- **space-evenly :** 두 항목 (및 가장자리까지의 공간) 사이의 간격이 같도록 항목이 분산 됩니다.

**flex-start 결과화면**



![img](https://blog.kakaocdn.net/dn/qCmE8/btq3y6jB2cs/4NYHndWPUTW4Uf0tOjsXQ0/img.png)



 

**flex-end 결과화면**



![img](https://blog.kakaocdn.net/dn/6nEQU/btq3AR7hw4D/vgqAXOJqmb5VQbnWBK0PBk/img.png)



 

**center 결과화면**



![img](https://blog.kakaocdn.net/dn/y2Rl0/btq3zOwcpAu/LKP3vKfQFY9EtlON2TgFkK/img.png)



**space-between 결과화면**



![img](https://blog.kakaocdn.net/dn/GDT5b/btq3znyQ4ZL/E6wziI64y5l1IWwDpcbUu0/img.png)



 

**space-around 결과화면**



![img](https://blog.kakaocdn.net/dn/oPdc8/btq3CAYusVG/pWkdj6XUHbWW6DMX90SzK1/img.png)



 

**space-evenly 결과화면**



![img](https://blog.kakaocdn.net/dn/bxRyjD/btq3zN49m1J/9kYe1TJrgt2BhvgTtWryPk/img.png)



####  

<br>

#### **부모요소 속성 : align-items**

align-items는 여러 줄의 항목에서, 수직 정렬을 하는 속성입니다. 이 속성은 항목이 *한 줄일때는 효과가 없습니다*.

```
.container {
  align-content: flex-start | flex-end | center | space-between | space-around | stretch;
}
```

- **flex-start :** 컨테이너 상단에 배치됩니다.
- **flex-end :** 컨테이너의 바닥 부분에 배치됩니다.
- **center :** 컨테이너 중앙에 정렬됩니다.
- **space-between :** 컨테이너에 균등하게 분산됩니다.
- **space-around :** 각 줄 주위에 동일한 간격으로 균등하게 분산됩니다.
- **stretch :** 컨테이너에서 사용 가능한 모든 공간을 차지하도록 줄이 늘어납니다 (기본값).

**flex-start 결과화면**



![img](https://blog.kakaocdn.net/dn/bOFLFO/btq3CegUM4o/z68dMaWW3RF4LQOFouFZX0/img.png)



 

***\*flex-end\** 결과화면**



![img](https://blog.kakaocdn.net/dn/cfN3Be/btq3EuQPble/KnNMdb03GCOFN0bO26SmV0/img.png)



 

***\*center\** 결과화면**



![img](https://blog.kakaocdn.net/dn/2yR79/btq3y5dXbKi/otgKfWrvDh4BGtYUm378Yk/img.png)



**space-between 결과화면**



![img](https://blog.kakaocdn.net/dn/bta0xU/btq3y6KEbx3/vtYKwzvKGVbyDdZZsNbcN1/img.png)



**space-around 결과화면**



![img](https://blog.kakaocdn.net/dn/GOPmN/btq3z5dFlNr/8pkwuCAqDq7STIF9ZDfTek/img.png)



 

***\*stretch\** 결과화면**



![img](https://blog.kakaocdn.net/dn/b1CgIz/btq3xOX4qyB/ToKQ9u4CM5UK8z5eSTLAa1/img.png)



<br>

 

------

### **자식요소 속성 : align-self**

flexbox item의 수직 정렬에 대한 속성입니다. 자세한 사항은 아래 그림을 참고해주세요.

```
.item {
  align-self: auto | stretch | flex-start | flex-end | center | baseline;
}
```

- **auto :** 기본값입니다.
- **stretch :** 컨테이너를 채우기 위해 항목이 늘어나면서 여전히 min-width 및 max-width 속성을 유지합니다.
- **flex-start :** 항목이 컨테이너 상단에 배치됩니다.
- **flex-end :** 항목이 컨테이너 하단에 배치됩니다.
- **center :** 항목이 컨테이너 중앙에 있습니다

**align-self 결과화면**



![img](https://blog.kakaocdn.net/dn/oqeUk/btq3xPirl5x/q6QwAwsvwJqk4UPxxjnY3k/img.png)



 

 

<br>

### **자식요소 속성 : flex-basis**

flex-basis속성은 flexbox item의 초기 크기를 지정하는 속성입니다.

- **flex-basis 값 :** auto
- **flex-basis 값 :** 숫자

```
.item {
  flex-basis: auto; ㅣ flex-basis: 0 ㅣ flex-basis: 200px;
}
```

 

**flex-basis:auto 결과화면(item one에 적용)**



![img](https://blog.kakaocdn.net/dn/rxc0q/btq3CeaNaBo/KQ4YWizjAbvtkgzrftEDo0/img.png)



 

**flex-basis:0 결과화면(item one에 적용)**



![img](https://blog.kakaocdn.net/dn/HceUe/btq3DrVczd2/yQQITv7VuUKFfBCzRCy7xK/img.png)



**flex-basis:200px 결과화면(item one에 적용)**



![img](https://blog.kakaocdn.net/dn/ehNoVT/btq3y5FCXWc/G7gwZghXVIBI3S32KHhUPk/img.png)



 

 

<br>

### **자식요소 속성 : flex-grow**

flex-grow속성은 형제 요소인 flex-item이 **동일한** **flex-grow 값**을 갖는다면 , **동일한 크기**를 갖게 됩니다.

하나의 flex-item에만 flex-grow 값을 준다면, 나머지 요소들은 나머지 넓이를 균등하게 갖게 됩니다.

```
.item{flex-grow: 1;}
```

 

**flex-grow:1 결과 화면**



![img](https://blog.kakaocdn.net/dn/Gn9hU/btq3ARtotup/tWBOeveaqOvh3MASuG9nt1/img.png)



 

**flex-grow:2 결과화면**



![img](https://blog.kakaocdn.net/dn/byPpbf/btq3GEeYREJ/SE9oHklUOgJNrSKuWXjdB0/img.png)



 

**flex-grow:3 결과화면**



![img](https://blog.kakaocdn.net/dn/bxVlyF/btq3GFrtyRT/LKzKw5YHA9jZwBmA3sUcEK/img.png)

<br>

<br>

#### 참고링크: [[CSS\] flex 속성 및 완벽 가이드 (tistory.com)](https://eunyoe.tistory.com/103)

<br>