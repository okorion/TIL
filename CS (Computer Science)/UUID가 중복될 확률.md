## ☄️ UUID가 중복될 확률

## Intro

최근 UOS공지사항 앱의 백엔드 시스템을 교체하는 작업을 하고 있습니다.

기존 Firebase의 Firestore를 사용하고 있었는데 이번에 새롭게 Nestjs로 서버를 작성하는 중입니다.

UOS공지사항의 서버에는 총 3개의 데이터베이스 모델( department, notice, user )이 있습니다.

각 모델의 레코드 마다 고유의 id값을 발급했는데 모두 uuid(v4)로 발급했습니다.

작업을 진행하면서 생긴 궁금한 점이 있어서 자료를 찾아봤습니다.

> uuid를 마구잡이로 발급하게 되면 혹시 나중에 겹치는 uuid가 있지 않을까?

<br>

## UUID 소개

- uuid는 범용고유식별자(Universal Unique IDentifier)라고 한다.

- 네트워크상에 존재하는 개체들을 식별하고 구별하기 위해 개발 주체가 스스로 이름을 짓도록 하며 고유성을 충족시킬 수 있는 방법이다.

- 총 36개의 문자로 이루어져 있다.(32개의 문자와 4개의 하이픈으로 구성된 총 5개의 그룹)

  - 예시: 550e8400-e29b-

    *4*

    1d4-

    *a*

    716-446655440000

    - a~f까지의 알파벳 값들이 대문자인지 소문자인지는 중요하지 않다.(16진수)

  - 128비트의 값이다.

- 총 `340,282,366,920,938,463,463,374,607,431,768,211,456`개의 사용가능한 UUID가 있다고 한다...

<br>

## UUID(v4)를 만드는 과정

1. 랜덤한 16바이트(128비트)를 만든다.

2. 특정 비트를 RFC 4122의 section 4.4에 따라 값을 변경해줍니다.

   - 예시 uuid: 550e8400-e29b-

     *4*

     1d4-

     *a*

     716-446655440000

     - 위에서 밑줄 친 ***4\***의 위치는 항상 '4'가 존재해야 한다.
     - ***a\***가 위치한 자리는 항상 '8', '9', 'a', 'b' 문자 중 하나가 존재해야 한다.

<br>

## UUID v4는 중복될 가능성이 없을까?

uuid v4는 생성 원리상 중복이 가능하다. 다만 그 중복될 가능성이 매우 희박하다. 총 `340,282,366,920,938,463,463,374,607,431,768,211,456` 개의 uuid가 생성 가능한데 이 중 중복되는 uuid가 생성될 가능성이 얼핏 봐도 희박해보인다.

<br>

### 그래도 나의 uuid가 중복되면 어떻게 하지?

인간이 매년 하늘에서 떨어지는 운석에 맞을 확률이 `0.00000000006` 이라고 한다. 이 확률은 수십조의 uuid(v4)를 생성할 때 단 하나의 중복된 uuid가 생성될 확률과 같다.

또한, 매 초 10억개의 uuid를 100년에 걸쳐서 생성할 때 단 하나의 uuid가 중복될 확률은 50%이다.

![img](https://miro.medium.com/max/1400/1*nAyhwGzJghFJRfFm5pykYA.png)

UOS공지사항의 서버에는 약 3~4만개의 공지사항이 저장될 예정인데 이 중 uuid의 중복이 발생할 확률은 매우 적어보인다.

<br>

### 그래도... 혹시..?

uuid v4는 거의 랜덤한 uuid를 생성하기 때문에 *그래도..? 혹시..?* uuid가 겹칠수도 있다. 그런 걱정이 있다면 uuid v1을 사용하면 된다.

uuid v1은 네트워크 카드의 MAC주소(48비트)와 현재 시각(60비트)을 기반으로 uuid를 생성한다. 여기서 말하는 현재 시각은 1582년 10월 15일과 현재 시각의 nanosecond의 차이를 말한다. 3603년도까지 가능하다고 한다.

따라서 uuid v1을 사용하여 uuid를 사용하면 오히려 uuid v4에 비해 중복 가능성이 훨씬 낮은 uuid를 생성할 수 있다. 하지만 uuid v1을 사용할 경우 uuid값을 통해 MAC주소를 알아낼 수 있다는 문제가 있다. 또한 MAC주소와 생성 시간이 유추 가능하기 때문에 uuid 역시 유추할 수 있다는 보안 문제가 있다.

<br>

## 결론

uuid v4는 충분히 안전하게 유일한 uuid를 발급해주며 uuid가 중복될 수 있는 통계적 가능성 역시 극히 희박하기에 uuid가 중복되면 어쩌지 하는 걱정은 안해도 된다. uuid v1은 현재 시각을 기반으로 uuid값을 생성하는데 uuid가 생성된 시각과 MAC주소로 uuid를 유추할 수 있기 때문에 안전하지 않다.

<br>

## 참고 자료

[범용 고유 식별자](https://ko.wikipedia.org/wiki/범용_고유_식별자)

[Generate a UUID compliant with RFC 4122](https://www.cryptosys.net/pki/uuid-rfc4122.html)

[RFC 4122 - A Universally Unique IDentifier (UUID) URN Namespace](https://tools.ietf.org/html/rfc4122#section-4.1.3)

[Universally unique identifier](https://en.wikipedia.org/w/index.php?title=Universally_unique_identifier&oldid=755882275#Random_UUID_probability_of_duplicates)

[How unique is UUID?](https://stackoverflow.com/questions/1155008/how-unique-is-uuid)

<br>

<br>

#### 참고링크: [UUID가 겹치면 어쩌지? (velog.io)](https://velog.io/@koreanhole/UUID가-겹치면-어쩌지)

<br>