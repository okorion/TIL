### 🌼 ChatGPT Study 🌼



> 프론트엔드 테스트 코드에 대해 쉽게 설명해줘.

 프론트엔드 테스트 코드는 프론트엔드 웹 애플리케이션의 **동작을 검증하고 버그를 발견**하는 것을 목적으로 작성된 코드입니다. 프론트엔드 테스트 코드는 자동화된 테스트를 수행하며, 개발자가 코드를 수정할 때마다 수동으로 테스트를 반복하는 번거로움을 없애줍니다.

 프론트엔드 테스트 코드를 작성하려면 먼저 테스트 도구를 선택해야 합니다. 대표적인 테스트 도구로는 **Jest,** Mocha, Jasmine 등이 있습니다. 이 도구들은 테스트 수행, 결과 보고, 코드 커버리지 등을 제공합니다.

 테스트 코드를 작성할 때는 일반적으로 다음과 같은 단계를 따릅니다.

1. 테스트 시나리오 작성: 무엇을 테스트할지, 어떻게 테스트할지 계획합니다.
2. 테스트 코드 작성: 테스트 코드를 작성합니다.
3. 테스트 수행: 테스트를 수행하고 결과를 확인합니다.
4. 버그 수정: 테스트에서 발견된 버그를 수정합니다.
5. 테스트 반복: 수정된 코드를 다시 테스트하고 결과를 확인합니다.



 📱 테스트 코드는 일반적으로 단위 테스트, 통합 테스트, UI 테스트 등으로 구분됩니다. 단위 테스트는 개별 컴포넌트나 함수 등을 검증하며, 통합 테스트는 컴포넌트 간 상호작용을 검증합니다. UI 테스트는 사용자의 시나리오를 재현하며, 실제 사용자의 경험을 검증합니다.

 프론트엔드 테스트 코드를 작성하면 개발자는 코드를 수정하고 배포하기 전에 자신감을 가질 수 있습니다. 또한, 테스트 코드는 **코드의 가독성과 유지보수성**을 높여주며, 신뢰성 있는 웹 애플리케이션을 만드는 데 도움이 됩니다.



<br>



> 예시 코드를 보여줘.

 다음은 React 컴포넌트를 테스트하는 예시 코드입니다. Jest와 Enzyme 라이브러리를 사용합니다.

```
javascriptCopy codeimport React from 'react';
import { shallow } from 'enzyme';
import Counter from './Counter';

describe('Counter 컴포넌트', () => {
  let wrapper;

  beforeEach(() => {
    wrapper = shallow(<Counter />);
  });

  it('초기 count 값은 0이어야 한다.', () => {
    expect(wrapper.state().count).toEqual(0);
  });

  it('버튼 클릭시 count 값이 1 증가한다.', () => {
    const button = wrapper.find('button');
    button.simulate('click');
    expect(wrapper.state().count).toEqual(1);
  });
});
```

 위 코드에서는 `Counter` 컴포넌트의 초기값과 버튼 클릭시 `count` 값이 1 증가하는지를 검증합니다. `describe` 함수로 테스트 스위트를 생성하고, `beforeEach` 함수로 각각의 테스트 케이스가 실행되기 전에 `Counter` 컴포넌트를 초기화합니다.

 각각의 테스트 케이스는 `it` 함수를 사용하여 정의되며, `expect` 함수를 사용하여 검증합니다. `shallow` 함수를 사용하여 `Counter` 컴포넌트를 랜더링하고, `find` 함수로 버튼 엘리먼트를 찾아 클릭 이벤트를 시뮬레이트합니다.

 이와 같이 테스트 코드를 작성하면 개발자는 변경된 코드가 예상대로 동작하는지 확인할 수 있으며, 코드를 수정하고 배포하기 전에 테스트를 자동으로 수행할 수 있습니다.



<br>

<br>

# 📜 Jest 공식 문서 - Getting Started



Install Jest using your favorite package manager:

- npm
- Yarn

```bash
npm install --save-dev jest
```



Let's get started by writing a test for a hypothetical function that adds two numbers. First, create a `sum.js` file:

```javascript
function sum(a, b) {
  return a + b;
}
module.exports = sum;
```



Then, create a file named `sum.test.js`. This will contain our actual test:

```javascript
const sum = require('./sum');

test('adds 1 + 2 to equal 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```



Add the following section to your `package.json`:

```json
{
  "scripts": {
    "test": "jest"
  }
}
```



Finally, run `yarn test` or `npm test` and Jest will print this message:

```bash
PASS  ./sum.test.js
✓ adds 1 + 2 to equal 3 (5ms)
```



**You just successfully wrote your first test using Jest!**



참고링크: [Getting Started · Jest (jestjs.io)](https://jestjs.io/docs/getting-started)