# 자신만의 Hook 만들기

> Try the new React documentation.
>
> These new documentation pages teach modern React and include live examples:
>
> - [Reusing Logic with Custom Hooks](https://beta.reactjs.org/learn/reusing-logic-with-custom-hooks)
>
> The new docs will soon replace this site, which will be archived. [Provide feedback.](https://github.com/reactjs/reactjs.org/issues/3308)

*Hook*은 React 16.8 버전에 새로 추가되었습니다. Hook은 클래스 컴포넌트를 작성하지 않아도 state와 같은 특징들을 사용할 수 있습니다.

자신만의 Hook을 만들면 컴포넌트 로직을 함수로 뽑아내어 재사용할 수 있습니다.

[Effect Hook 사용하기](https://ko.reactjs.org/docs/hooks-effect.html#example-using-hooks-1)를 배울 때, 채팅 애플리케이션에서 친구가 온라인 상태인지 아닌지에 대한 메시지를 표시하는 컴포넌트를 보았을 것입니다.

```
import React, { useState, useEffect } from 'react';

function FriendStatus(props) {
  const [isOnline, setIsOnline] = useState(null);  useEffect(() => {    function handleStatusChange(status) {      setIsOnline(status.isOnline);    }    ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);    return () => {      ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);    };  });
  if (isOnline === null) {
    return 'Loading...';
  }
  return isOnline ? 'Online' : 'Offline';
}
```

이제 채팅 애플리케이션에 연락처 목록이 있으며 그중에서 온라인 상태인 사용자들의 이름을 초록색으로 표시하는 상황을 가정해 보겠습니다. 위의 코드와 비슷한 로직을 복사하여 `FriendListItem` 컴포넌트 안에 붙여넣을 수도 있지만, 가장 좋은 방법이라고 할 수는 없습니다.

```
import React, { useState, useEffect } from 'react';

function FriendListItem(props) {
  const [isOnline, setIsOnline] = useState(null);  useEffect(() => {    function handleStatusChange(status) {      setIsOnline(status.isOnline);    }    ChatAPI.subscribeToFriendStatus(props.friend.id, handleStatusChange);    return () => {      ChatAPI.unsubscribeFromFriendStatus(props.friend.id, handleStatusChange);    };  });
  return (
    <li style={{ color: isOnline ? 'green' : 'black' }}>
      {props.friend.name}
    </li>
  );
}
```

그 대신 이 로직을 `FriendStatus`와 `FriendListItem`에서 공유하도록 하고 싶습니다.

React에는 상태 관련 로직을 컴포넌트에서 공유하는 두 가지 전통적인 방법이 있는데 [render props](https://ko.reactjs.org/docs/render-props.html)와 [고차 컴포넌트](https://ko.reactjs.org/docs/higher-order-components.html)입니다. Hook을 사용하여 트리에 컴포넌트를 더하지 않고 위의 문제를 해결하는 방법을 보도록 하겠습니다.

## 사용자 정의 Hook 추출하기

두 개의 자바스크립트 함수에서 같은 로직을 공유하고자 할 때는 또 다른 함수로 분리합니다. 컴포넌트와 Hook 또한 함수이기 때문에 같은 방법을 사용할 수 있습니다!

**사용자 정의 Hook은 이름이 `use`로 시작하는 자바스크립트 함수입니다. 사용자 Hook은 다른 Hook을 호출할 수 있습니다.** 예를 들자면, 아래의 `useFriendStatus`가 우리의 첫 번째 사용자 정의 Hook입니다.

```
import { useState, useEffect } from 'react';

function useFriendStatus(friendID) {  const [isOnline, setIsOnline] = useState(null);

  useEffect(() => {
    function handleStatusChange(status) {
      setIsOnline(status.isOnline);
    }

    ChatAPI.subscribeToFriendStatus(friendID, handleStatusChange);
    return () => {
      ChatAPI.unsubscribeFromFriendStatus(friendID, handleStatusChange);
    };
  });

  return isOnline;
}
```

딱히 새로운 것은 없습니다. 로직은 위의 컴포넌트로부터 복사해왔습니다. 다만 컴포넌트에서처럼 다른 Hook들은 사용자 Hook의 위로 놓여야 하며 사용자 정의 Hook은 조건부 함수가 아니어야 합니다.

React 컴포넌트와는 다르게 사용자 정의 Hook은 특정한 시그니처가 필요 없습니다. 무엇을 인수로 받아야 하며 필요하다면 무엇을 반환해야 하는 지를 사용자가 결정할 수 있습니다. 다시 말하지만, 보통의 함수와 마찬가지입니다. 이름은 반드시 `use`로 시작해야 하는데 그래야만 한눈에 보아도 [Hook 규칙](https://ko.reactjs.org/docs/hooks-rules.html)이 적용되는지를 파악할 수 있기 때문입니다.

`useFriendStatus` Hook의 목표는 친구의 상태를 구독하기 위함입니다. 이를 위하여 `friendID`를 인수로 받고 온라인 상태의 여부를 반환합니다.

```
function useFriendStatus(friendID) {
  const [isOnline, setIsOnline] = useState(null);

  // ...

  return isOnline;
}
```

이제 사용자 정의 Hook을 어떻게 이용하는지 보겠습니다.

## 사용자 정의 Hook 이용하기

처음 우리의 목표는 `FriendStatus`와 `FriendListItem` 컴포넌트에 중복되어있는 로직을 제거하는 것이었습니다. 두 컴포넌트 모두 친구의 온라인 상태 여부를 알아야 하죠.

이제 이 로직을 `useFriendStatus` hook으로 뽑아내었으니, *바로 사용할 수 있습니다.*

```
function FriendStatus(props) {
  const isOnline = useFriendStatus(props.friend.id);
  if (isOnline === null) {
    return 'Loading...';
  }
  return isOnline ? 'Online' : 'Offline';
}
function FriendListItem(props) {
  const isOnline = useFriendStatus(props.friend.id);
  return (
    <li style={{ color: isOnline ? 'green' : 'black' }}>
      {props.friend.name}
    </li>
  );
}
```

**본래의 예시와 동일한 코드인가요?** 네 정확히 같은 방식으로 작동합니다. 자세히 보면 작동방식에 어떤 변화도 없다는 것을 알 수 있습니다. 바뀐 것은 오로지 공통의 코드를 뽑아내 새로운 함수로 만든 것뿐입니다. **사용자 정의 Hook은 React의 특별한 기능이라기보다 기본적으로 Hook의 디자인을 따르는 관습입니다.**

**사용자 정의 Hook의 이름은 “`use`”로 시작되어야 하나요?** 네 그렇습니다. 이 관습은 아주 중요합니다. 이를 따르지 않으면 특정한 함수가 그 안에서 Hook을 호출하는지를 알 수 없기 때문에 [Hook 규칙](https://ko.reactjs.org/docs/hooks-rules.html)의 위반 여부를 자동으로 체크할 수 없습니다.

**같은 Hook을 사용하는 두 개의 컴포넌트는 state를 공유하나요?** 아니요. 사용자 정의 Hook은 *상태 관련 로직*(구독을 설정하고 현재 변숫값을 기억하는 것)을 재사용하는 메커니즘이지만 사용자 Hook을 사용할 때마다 그 안의 state와 effect는 완전히 독립적입니다.

**사용자 정의 Hook은 어떻게 독립된 state를 얻는 건가요?** 각각의 Hook에 대한 *호출*은 서로 독립된 state를 받습니다. `useFriendStatus`를 직접적으로 호출하기 때문에 React의 관점에서 이 컴포넌트는 `useState`와 `useEffect`를 호출한 것과 다름없습니다. 또한 우리가 [이전에](https://ko.reactjs.org/docs/hooks-effect.html#tip-use-multiple-effects-to-separate-concerns) [배웠듯이](https://ko.reactjs.org/docs/hooks-state.html#tip-using-multiple-state-variables), 하나의 컴포넌트 안에서 `useState`와 `useEffect`를 여러 번 부를 수 있고 이들은 모두 완전히 독립적입니다.

### 팁: Hook에서 Hook으로 정보 전달하기

Hook은 함수이기 때문에 Hook 사이에서도 정보를 전달할 수 있습니다.

상황설명을 위해 채팅 예시에 있는 다른 컴포넌트를 사용하겠습니다. 현재 선택된 친구가 온라인 상태인지를 표시하는 채팅 수신자 선택기입니다.

```
const friendList = [
  { id: 1, name: 'Phoebe' },
  { id: 2, name: 'Rachel' },
  { id: 3, name: 'Ross' },
];

function ChatRecipientPicker() {
  const [recipientID, setRecipientID] = useState(1);  const isRecipientOnline = useFriendStatus(recipientID);
  return (
    <>
      <Circle color={isRecipientOnline ? 'green' : 'red'} />      <select
        value={recipientID}
        onChange={e => setRecipientID(Number(e.target.value))}
      >
        {friendList.map(friend => (
          <option key={friend.id} value={friend.id}>
            {friend.name}
          </option>
        ))}
      </select>
    </>
  );
}
```

현재 선택된 친구의 ID를 `recipientID` state 변수에 저장하고 사용자가 `<select>` 선택기에 있는 다른 친구를 선택하면 이를 업데이트합니다.

`useState` Hook 호출은 `recipientID` state 변수의 최신값을 돌려주기 때문에 이를 `useFriendStatus` Hook에 인수로 보낼 수 있습니다.

```
  const [recipientID, setRecipientID] = useState(1);
  const isRecipientOnline = useFriendStatus(recipientID);
```

이를 통해 *지금 선택되어있는* 친구의 온라인 상태 여부를 알 수 있습니다. 다른 친구를 선택하고 `recipientID` state 변수를 업데이트하면 `useFriendStatus` Hook은 이미 선택되어있는 친구의 구독을 해지하고 새로이 선택된 친구의 상태를 구독할 것입니다.



참고링크: [자신만의 Hook 만들기 – React (reactjs.org)](https://ko.reactjs.org/docs/hooks-custom.html)