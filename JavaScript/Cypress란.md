## 🅿️ Cypress란?

- Cypress는 자바스크립트 E2E 테스트 프레임워크입니다.
- 개발자 또는 QA 엔지니어가 Cypress를 이용하여 테스트를 할 수 있습니다.
- Cypress를 이용하여 다음과 같은 테스트를 할 수 있습니다.

> End-to-end tests
> Integration tests
> Unit tests

## Cypress 특징

Cypress의 특징은 다음과 같습니다.

- 완벽한 E2E Tesing을 경험할 수 있습니다.
- Cypress Test Runner를 설치하고 로컬에서 테스트를 작성합니다.
- CI 테스트를 구축 및 결과를 기록합니다.
- Cypress는 테스트가 실행될 때 스냅샷을 만듭니다. 각 단계에서 정확히 어떤 일이 발생했는지 확인할 수 있습니다.
- Chrome DevTools과 같은 익숙한 도구에서 빠르게 직접 디버깅할 수 있습니다.
- Cypress는 테스트를 변경할 때마다 자동으로 다시 로드합니다.

## Cypress의 특별한 점

#### Architecture

- Selenium과 같은 대부분의 테스트 도구는 브라우저 외부에서 실행하고 네트워크를 통해 원격 명령을 실행하여 작동하는 것과 달리 Cypress는 애플리케이션과 동일한 환경에서 실행됩니다.
- Cypress는 Node위에 동작하는 서버를 띄우게 됩니다. 실제 브라우저 위에서 테스트를 진행합니다.
- Cypress는 궁극적으로 전체 자동화 프로세스를 제어하므로 브라우저 안팎에서 일어나는 모든 일을 이해할 수 있기 때문에 Cypress가 다른 어떤 테스트 도구보다 일관된 결과를 제공할 수 있음을 의미합니다.

node위에 동작하는 서버를 띄우고

#### Native access

- Cypress는 응용 프로그램 내에서 작동하므로 document, window, DOM 요소, 응용 프로그램 인스턴스, 함수, 타이머 등 Cypress 테스트할 때 접근할 수 있습니다.

#### Debuggability

- 무엇보다도 Cypress는 사용성을 위해 제작되었습니다.
- Cypress는 애플리케이션의 스냅샷을 만들고 명령이 실행되었을 때의 상태를 볼 수 있도록 합니다.
- 테스트가 실행되는 동안 개발자 도구를 사용할 수 있으며 모든 콘솔 메시지, 모든 네트워크 요청을 볼 수 있습니다.

### Cypress Test Types

- End-to-end
  - Cypress는 원래 브라우저에서 실행되는 모든 항목에 대해 종단 간(E2E) 테스트를 실행하도록 설계되었습니다.
  - 일반적인 E2E 테스트는 브라우저에서 App을 방문하고 실제 User처럼 UI를 통해 작업을 수행합니다.

```
it('adds todos', () => {
  cy.visit('https://todo.app.com')
  cy.get('.new-input').type('write code{enter}')
		.type('write tests{enter}')
  cy.get('li.todo').should('have.length', 2)
})
```

- Component
  - Cypress를 사용하여 일부 web framework에서 [Component tests](https://docs.cypress.io/guides/component-testing/introduction#What-is-Component-Testing)를 실행할 수도 있습니다

```
import { mount } from '@cypress/react' // or @cypress/vue
import TodoList from './components/TodoList'

it('contains the correct number of todos', () => {
  const todos = [
    { text: 'Buy milk', id: 1 },
    { text: 'Learn Component Testing', id: 2 },
  ]

  mount(<TodoList todos={todos} />)
  cy.get('[data-testid=todos]')
		.should('have.length', todos.length)
})
```

- API
  - Cypress는 임의의 HTTP 호출을 수행할 수 있으므로 API 테스트에 사용할 수 있습니다.

```
it('adds a todo', () => {
  cy.request({
    url: '/todos',
    method: 'POST',
    body: {
      title: 'Write REST API',
    },
  })
    .its('body')
    .should('deep.contain', {
      title: 'Write REST API',
      completed: false,
    })
})
```

 

 

 

출처
https://www.cypress.io/

https://docs.cypress.io/guides/overview/why-cypress

https://docs.cypress.io/guides/overview/key-differences#Architecture



<br>

<br>

#### 참고링크: [Cypress에 대해 (tistory.com)](https://taenami.tistory.com/132)

<br>