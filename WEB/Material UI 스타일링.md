## 🥃 Material UI 스타일링

Material UI에서 기본적으로 제공하는 컴포넌트를 그대로 사용해도 훌륭하지만 약간씩 스타일을 변경하고 싶을 때가 있습니다. 이번 포스팅에서는 Material UI에 사용자가 정의한 스타일을 적용하는 방법에 대해서 알아보겠습니다.

> Material UI의 기본적인 셋업에 대한 부분은 [관련 포스팅](https://www.daleseo.com/material-ui-typography)를 참고 바랍니다.

## CssBaseline 컴포넌트

어떤 브라우저를 돌아가느냐에 상관없이 일괄적인 스타일을 적용되려면, CSS를 전역에서 정규화(normalize)시켜주는 것이 권장됩니다. 이를 위해서 우선 `<CssBaseline />` 컴포넌트를 React 애플리케이션의 최상위 컴포넌트에 추가해줘야 합니다.

```jsx
import React from "react";
import CssBaseline from "@material-ui/core/CssBaseline";

export default function App() {
  return (
    <>
      <CssBaseline />
      {/* 다른 컴포넌트 */}
    </>
  );
}
```

## makeStyles Hook

Material UI는 직관적으로 사용자 정의 스타일을 적용할 수 있도록 `makeStyles` React hook을 제공합니다. `makeStyles`는 `@material-ui/core/styles` 패키지에서 임포트 할 수 있으며, 인자로 커스텀 스타일 객체를 받습니다. 커스텀 스타일 객체의 클래스 이름을 키로 갖고 해당 클래스의 CSS 속성을 정의한 객체를 값으로 갖습니다.

```jsx
import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { Typography } from "@material-ui/core";

const useStyles = makeStyles({
  text: {
    color: "white",
    backgroundColor: "black",
  },
});

export default function () {
  const classes = useStyles();
  return <Typography className={classes.text}>Test</Typography>;
}
```

커스텀 스타일을 사용하려면 `makeStyles` hook으로 작성한 함수를 호출한 결과를 `classes` 변수에 저정합니다. 그 다음 커스텀 스타일이 필요한 곳에 `className` prop의 값으로 `classes` 변수에 저정된 클래스 이름을 넘겨줍니다.

## Box 컴포넌트

`padding`이나 `margin`과 같은 단순한 CSS 속성은 직접 스타일을 정의하지 않고도 Material UI가 제공하는 `<Box/>` 컴포넌트를 이용한 간단하게 적용이 가능합니다. 스타일이 필요한 컴포넌트를 `<Box/>` 컴포넌트로 감싸고 CSS 유털리티 prop을 설정해주기만 하면 되기 때문에 매우 편리하게 사용할 수 있습니다.

```jsx
import React from "react";
import { Box, Typography } from "@material-ui/core";

export default function () {
  return (
    <Box clone p={5} mx={2} my={3}>
      <Typography>Test</Typography>
    </Box>
  );
}
```

## 스타일 적용 예제

Material UI를 사용해서 가격 정보를 보여주는 실습용 React UI를 작성해보겠습니다.

먼저 앱의 최상위 컴포넌트 파일에 `<CssBaseline/>` 컴포넌트를 추가해줍니다. 그리고 `<Box/>` 컴포넌트를 이용해서 `<Container/>` 컴포넌트 주변에 약간의 `padding`을 주었습니다.

```jsx
import React from "react";
import { CssBaseline, Box, Container } from "@material-ui/core";

import PricingCard from "./PricingCard";

export default function () {
  return (
    <>
      <CssBaseline />
      <Box clone p={5}>
        <Container maxWidth="xs">
          <PricingCard />
        </Container>
      </Box>
    </>
  );
}
```

다음으로 `styles.js` 파일을 생성하고, 그 안에 `makeStyles` hook을 이용해서 3개의 클래스에 대한 커스텀 스타일을 작성합니다.

```js
import { makeStyles } from "@material-ui/core/styles";

export const useStyles = makeStyles({
  header: {
    backgroundColor: "#EEE",
  },
  pricing: {
    display: "flex",
    justifyContent: "center",
    alignItems: "baseline",
    marginBottom: "16px",
  },
  descriptions: {
    margin: 0,
    padding: 0,
    listStyle: "none",
  },
});
```

마지막으로 Material UI의 여러 가지 컴포넌트를 이용해서 `<PricingCard/>` 컴포넌트를 작성합니다. 위에서 작성한 `useStyles` hook을 임포트한 후 커스텀 스타일이 필요한 곳에 적용해줍니다.

```jsx
import React from "react";
import {
  Button,
  Card,
  CardActions,
  CardContent,
  CardHeader,
  Typography,
} from "@material-ui/core";

import { useStyles } from "./styles";

export default function () {
  const classes = useStyles();
  return (
    <Card>
      <CardHeader
        title="Free"
        titleTypographyProps={{ align: "center" }}
        className={classes.header}
      />
      <CardContent>
        <div className={classes.pricing}>
          <Typography variant="h3" color="textPrimary">
            $0
          </Typography>
          <Typography variant="h6" color="textSecondary">
            /mo
          </Typography>
        </div>
        <ul className={classes.descriptions}>
          {["2 GB of storage", "Help center access", "Email support"].map(
            (line) => (
              <Typography
                component="li"
                variant="subtitle1"
                align="center"
                key={line}
              >
                {line}
              </Typography>
            )
          )}
        </ul>
      </CardContent>
      <CardActions>
        <Button fullWidth variant="contained" color="primary">
          Sign up for free
        </Button>
      </CardActions>
    </Card>
  );
}
```



## 마치면서

이상으로 Material UI에서 사용자 정의 스타일을 적용하는 방법에 대해서 간단한게 살펴보았습니다.



<br>

<br>

#### 참고링크: [Material UI 스타일링 | Engineering Blog by Dale Seo](https://www.daleseo.com/material-ui-styles/)

<br>