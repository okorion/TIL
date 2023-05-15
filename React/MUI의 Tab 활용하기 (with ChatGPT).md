## ⭐ MUI의 Tab 활용하기 (with ChatGPT)

Material-UI의 `Tab` 컴포넌트는 탭 형식의 네비게이션을 생성하는 데 사용됩니다. 탭은 사용자가 선택할 수 있는 여러 항목 중 하나를 나타내며, 선택한 항목에 대한 컨텐츠를 표시하는 역할을 합니다.

<br>

`Tab` 컴포넌트는 `Tabs` 컴포넌트 내에서 사용됩니다. `Tabs` 컴포넌트는 여러 개의 `Tab` 컴포넌트를 자식으로 가질 수 있으며, 각 `Tab` 컴포넌트는 고유한 `value` prop을 가져야 합니다.

<br>

탭의 작동 원리를 예시와 함께 설명해드리겠습니다. 아래의 예시 코드를 참고해주세요:

```
jsxCopy codeimport React, { useState } from "react";
import { Tabs, Tab } from "@mui/material";

const TabExample = () => {
  const [value, setValue] = useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Tabs value={value} onChange={handleChange}>
      <Tab label="Tab 1" value={0} />
      <Tab label="Tab 2" value={1} />
      <Tab label="Tab 3" value={2} />
    </Tabs>
  );
};
```

 위의 예시에서는 `Tabs` 컴포넌트 내에 세 개의 `Tab` 컴포넌트가 있습니다. 각 `Tab` 컴포넌트는 `label` prop으로 표시될 텍스트를 받고, 고유한 `value` prop을 가지고 있습니다.

<br>

`Tabs` 컴포넌트에는 `value` prop과 `onChange` prop이 필요합니다. `value` prop은 현재 선택된 탭의 `value` 값을 나타내며, `onChange` prop은 탭이 변경될 때 호출되는 콜백 함수입니다.

<br>

`handleChange` 함수는 탭이 변경될 때마다 호출되며, 선택된 탭의 `value` 값을 업데이트하여 현재 선택된 탭을 유지합니다.

<br>

위의 예시에서는 초기값으로 첫 번째 탭을 선택하도록 `useState` 훅을 사용하여 `value` 상태를 초기화합니다.

<br>

탭을 클릭하면 `onChange` 핸들러가 호출되고, 선택된 탭의 `value` 값이 변경됩니다. 이렇게 `value` 값이 업데이트되면, `Tabs` 컴포넌트는 해당하는 `value` 값을 가진 `Tab` 컴포넌트를 활성화하고 나머지 탭은 비활성화합니다.

<br>

이렇게 작동하여 사용자는 탭을 클릭하여 다양한 컨텐츠를 전환하거나 탭 간에 탐색할 수 있습니다.Material-UI의 `Tab` 컴포넌트는 탭 형식의 네비게이션을 생성하는 데 사용됩니다. 탭은 사용자가 선택할 수 있는 여러 항목 중 하나를 나타내며, 선택한 항목에 대한 컨텐츠를 표시하는 역할을 합니다.

<br>

`Tab` 컴포넌트는 `Tabs` 컴포넌트 내에서 사용됩니다. `Tabs` 컴포넌트는 여러 개의 `Tab` 컴포넌트를 자식으로 가질 수 있으며, 각 `Tab` 컴포넌트는 고유한 `value` prop을 가져야 합니다.

<br>

탭의 작동 원리를 예시와 함께 설명해드리겠습니다. 아래의 예시 코드를 참고해주세요:

```
jsxCopy codeimport React, { useState } from "react";
import { Tabs, Tab } from "@mui/material";

const TabExample = () => {
  const [value, setValue] = useState(0);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  return (
    <Tabs value={value} onChange={handleChange}>
      <Tab label="Tab 1" value={0} />
      <Tab label="Tab 2" value={1} />
      <Tab label="Tab 3" value={2} />
    </Tabs>
  );
};
```

위의 예시에서는 `Tabs` 컴포넌트 내에 세 개의 `Tab` 컴포넌트가 있습니다. 각 `Tab` 컴포넌트는 `label` prop으로 표시될 텍스트를 받고, 고유한 `value` prop을 가지고 있습니다.

<br>

`Tabs` 컴포넌트에는 `value` prop과 `onChange` prop이 필요합니다. `value` prop은 현재 선택된 탭의 `value` 값을 나타내며, `onChange` prop은 탭이 변경될 때 호출되는 콜백 함수입니다.

<br>

`handleChange` 함수는 탭이 변경될 때마다 호출되며, 선택된 탭의 `value` 값을 업데이트하여 현재 선택된 탭을 유지합니다.

<br>

위의 예시에서는 초기값으로 첫 번째 탭을 선택하도록 `useState` 훅을 사용하여 `value` 상태를 초기화합니다.

<br>

탭을 클릭하면 `onChange` 핸들러가 호출되고, 선택된 탭의 `value` 값이 변경됩니다. 이렇게 `value` 값이 업데이트되면, `Tabs` 컴포넌트는 해당하는 `value` 값을 가진 `Tab` 컴포넌트를 활성화하고 나머지 탭은 비활성화합니다.

<br>

이렇게 작동하여 사용자는 탭을 클릭하여 다양한 컨텐츠를 전환하거나 탭 간에 탐색할 수 있습니다.

<br>

<br>