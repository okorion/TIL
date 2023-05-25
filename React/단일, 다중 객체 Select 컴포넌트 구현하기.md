## 🚀 단일, 다중 객체 Select 컴포넌트 구현하기

### 🎣 단일/다중 객체 Select 기능 컴포넌트의 예시

```
import React, { useState } from 'react';

const ObjectComponent = ({ object, selectedObjects, updateSelectedObjects }) => {
  const isSelected = selectedObjects.includes(object);

  const handleClick = () => {
    let updatedSelectedObjects;

    if (isSelected) {
      // 이미 선택된 객체인 경우 선택 해제
      updatedSelectedObjects = selectedObjects.filter((selectedObject) => selectedObject !== object);
    } else {
      // 선택되지 않은 객체인 경우 선택
      updatedSelectedObjects = [...selectedObjects, object];
    }

    updateSelectedObjects(updatedSelectedObjects);
  };

  return (
    <div
      className={`object ${isSelected ? 'selected' : ''}`}
      onClick={handleClick}
    >
      {object.name}
    </div>
  );
};

const ObjectList = () => {
  const [selectedObjects, setSelectedObjects] = useState([]);
  const objects = [
    { id: 1, name: 'Object 1' },
    { id: 2, name: 'Object 2' },
    { id: 3, name: 'Object 3' },
  ];

  const updateSelectedObjects = (newSelectedObjects) => {
    setSelectedObjects(newSelectedObjects);
  };

  return (
    <div>
      {objects.map((object) => (
        <ObjectComponent
          key={object.id}
          object={object}
          selectedObjects={selectedObjects}
          updateSelectedObjects={updateSelectedObjects}
        />
      ))}
    </div>
  );
};

export default ObjectList;
```
 위의 예시 코드에서는 `ObjectComponent`라는 각 객체를 표시하는 컴포넌트를 정의하고, `ObjectList` 컴포넌트에서 `ObjectComponent`를 사용하여 여러 개의 객체를 렌더링합니다.

 `ObjectComponent` 컴포넌트에서는 `isSelected` 변수를 사용하여 선택된 객체인지 확인합니다. 클릭 이벤트 핸들러인 `handleClick` 함수에서는 선택된 객체를 업데이트하고, `updateSelectedObjects` 함수를 호출하여 `selectedObjects` 상태를 업데이트합니다. 선택된 객체의 상태에 따라 CSS 클래스를 추가하여 선택된 객체를 시각적으로 나타냅니다.

 `ObjectList` 컴포넌트에서는 `selectedObjects` 상태와 `updateSelectedObjects` 함수를 선언하여 `ObjectComponent`에 전달합니다. 객체 리스트를 순회하며 `ObjectComponent`를 렌더링하고, 각 객체에 대한 상태 업데이트를 처리합니다.

 위의 예시 코드를 사용하면 객체를 클릭하여 선택 및 선택 해제할 수 있으며, 선택된 객체의 상태를 업데이트할 수 있습니다. 선택된 객체의 상태에 따라 추가적인 로직을 수행하거나 시각적인 표시를 변경할 수 있습니다.

 <br>
 <br>

 ### 🪢 React와 MobX에서의 컴포넌트 구현

 > React + MobX 환경에서 단일/다중 객체 Select 기능의 컴포넌트에 적절한 상태 관리 방법은 뭘까?

-  [MobX] **`observable`**과 **`computed`** 사용
-  [MobX] **`useObservable`** Hook 사용

 <br>

#### 1. observable과 computed 사용

```
import { observable, computed } from 'mobx';

class SelectionStore {
  @observable selectedObjects = [];

  @computed get isSelected() {
    return this.selectedObjects.length > 0;
  }

  selectObject(object) {
    this.selectedObjects.push(object);
  }

  deselectObject(object) {
    const index = this.selectedObjects.indexOf(object);
    if (index > -1) {
      this.selectedObjects.splice(index, 1);
    }
  }
}

const selectionStore = new SelectionStore();

const ObjectComponent = ({ object }) => {
  const handleClick = () => {
    if (selectionStore.isSelected) {
      selectionStore.deselectObject(object);
    } else {
      selectionStore.selectObject(object);
    }
  };

  return (
    <div
      className={selectionStore.isSelected && selectionStore.selectedObjects.includes(object) ? 'selected' : ''}
      onClick={handleClick}
    >
      {object.name}
    </div>
  );
};
```
 위의 예시 코드에서는 `SelectionStore` 클래스를 만들어 `selectedObjects` 배열을 `observable`로 정의하고, `isSelected`를 `computed`로 정의합니다. `ObjectComponent`에서는 `SelectionStore` 인스턴스를 생성하고 선택 및 선택 해제에 대한 로직을 수행합니다. 선택된 객체의 상태에 따라 클래스를 추가하여 선택된 객체를 시각적으로 나타냅니다.

#### 2. useObservable Hook 사용

```
import { useObservable } from 'mobx-react';

const ObjectList = () => {
  const selectionStore = useObservable({
    selectedObjects: [],

    get isSelected() {
      return this.selectedObjects.length > 0;
    },

    selectObject(object) {
      this.selectedObjects.push(object);
    },

    deselectObject(object) {
      const index = this.selectedObjects.indexOf(object);
      if (index > -1) {
        this.selectedObjects.splice(index, 1);
      }
    }
  });

  return (
    <div>
      {objects.map((object) => (
        <ObjectComponent
          key={object.id}
          object={object}
          selectionStore={selectionStore}
        />
      ))}
    </div>
  );
};

const ObjectComponent = ({ object, selectionStore }) => {
  const handleClick = () => {
    if (selectionStore.isSelected) {
      selectionStore.deselectObject(object);
    } else {
      selectionStore.selectObject(object);
    }
  };

  return (
    <div
      className={selectionStore.isSelected && selectionStore.selectedObjects.includes(object) ? 'selected' : ''}
      onClick={handleClick}
    >
      {object.name}
    </div>
  );
};
```
 위의 예시 코드에서는 `useObservable` 훅을 사용하여 `selectionStore` 객체를 생성합니다. `selectedObjects` 배열과 `isSelected` getter, `selectObject`, `deselectObject` 메서드를 정의합니다. `ObjectList` 컴포넌트에서는 `selectionStore` 객체의 상태를 업데이트하는 방법은 이전과 동일한 방법을 사용할 수 있습니다. `selectionStore` 객체의 메서드를 호출하여 선택된 객체를 추가하거나 제거할 수 있습니다.

> `selectedObjects` 배열을 사용하여 다중 선택된 객체를 관리합니다. `selectObject` 메서드는 선택된 객체를 배열에 추가하고, `deselectObject` 메서드는 해당 객체를 배열에서 제거합니다. 따라서 여러 개의 객체를 동시에 선택할 수 있습니다.

<br>

---

<br>

#### ⛄ Select된 객체를 하나만 유지하는 컴포넌트 구현
 단일 선택의 경우에는 선택된 객체를 한 번에 하나만 유지하는 방식으로 구현할 수 있습니다. 다음은 해당 예시입니다:

```
import { useObservable } from 'mobx-react';

const ObjectList = () => {
  const selectionStore = useObservable({
    selectedObject: null,

    selectObject(object) {
      this.selectedObject = object;
    },

    deselectObject() {
      this.selectedObject = null;
    }
  });

  return (
    <div>
      {objects.map((object) => (
        <ObjectComponent
          key={object.id}
          object={object}
          isSelected={selectionStore.selectedObject === object}
          selectObject={selectionStore.selectObject}
          deselectObject={selectionStore.deselectObject}
        />
      ))}
    </div>
  );
};

const ObjectComponent = ({ object, isSelected, selectObject, deselectObject }) => {
  const handleClick = () => {
    if (isSelected) {
      deselectObject();
    } else {
      selectObject(object);
    }
  };

  return (
    <div
      className={isSelected ? 'selected' : ''}
      onClick={handleClick}
    >
      {object.name}
    </div>
  );
};
```
 위의 예시 코드에서는 `selectionStore` 객체에 `selectedObject` 상태를 추가하고, `selectObject` 메서드와 `deselectObject` 메서드를 정의합니다. `ObjectComponent`에서는 `isSelected` prop을 통해 선택 여부를 전달받고, `selectObject`와 `deselectObject` 메서드를 호출하여 선택 및 선택 해제를 처리합니다.

 이와 같이 MobX를 사용하면 객체의 상태를 효과적으로 관리할 수 있으며, 선택된 객체의 상태에 따라 추가적인 동작이나 시각적인 변경을 적용할 수 있습니다. 선택된 객체의 수에 제한이 있는 다중 선택의 경우에도 비슷한 방식으로 구현할 수 있습니다.


> `selectedObject` 단일 상태를 사용하여 단일 선택된 객체를 관리합니다. `selectObject` 메서드는 선택된 객체를 `selectedObject`에 할당하고, `deselectObject` 메서드는 `selectedObject`를 null로 설정합니다. 이로써 하나의 객체만 선택할 수 있습니다.

<br>

<br>

**👨‍💻 With ChatGPT 👨‍💻**

<br>