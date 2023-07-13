## 👔 MUI Dialog 스타일링

MuiDialog-paper 클래스는 Material-UI의 Dialog 컴포넌트의 콘텐츠 영역을 스타일링하는 데 사용되는 클래스입니다. 이 클래스를 사용하여 배경색을 변경하려면 다음과 같은 방법을 사용할 수 있습니다:

<br>

1. **테마(theme)를 사용하는 방법:**

- Material-UI의 테마를 사용하고 있다면, 테마를 사용하여 MuiDialog-paper의 배경색을 변경할 수 있습니다.

- createTheme() 함수를 사용하여 커스텀 테마를 생성하거나, 기존 테마를 오버라이딩할 수 있습니다.

- 예를 들어, 테마에서 MuiDialog-paper의 배경색을 변경하려면 다음과 같이 하십시오:

  ```react
  jsxCopy codeimport { createTheme, ThemeProvider } from '@mui/material/styles';
  
  const theme = createTheme({
    components: {
      MuiDialog: {
        styleOverrides: {
          paper: {
            backgroundColor: 'your-color',
          },
        },
      },
    },
  });
  
  function App() {
    return (
      <ThemeProvider theme={theme}>
        {/* 나머지 컴포넌트 */}
      </ThemeProvider>
    );
  }
  ```

<br>

2. **직접 CSS 스타일링을 사용하는 방법:**

- 직접 CSS 스타일링을 사용하는 경우, MuiDialog-paper 클래스에 직접 스타일을 적용하여 배경색을 변경할 수 있습니다.

- 예를 들어, 다음과 같이 스타일 객체를 생성하고 클래스 이름을 지정하여 배경색을 변경할 수 있습니다:

  ```react
  jsxCopy codeimport Dialog from '@mui/material/Dialog';
  
  const styles = {
    customDialog: {
      backgroundColor: 'your-color',
    },
  };
  
  function App() {
    return (
      <Dialog classes={{ paper: styles.customDialog }}>
        {/* 다이얼로그 내용 */}
      </Dialog>
    );
  }
  ```

위의 방법 중 하나를 사용하여 MuiDialog-paper 클래스의 배경색을 변경할 수 있습니다. 선택한 방법에 따라 프로젝트에 맞게 구현해보세요.

<br>

<br>

🛫 With ChatGPT 🛬

<br>

참고자료: [Themed components - Material UI (mui.com)](https://mui.com/material-ui/customization/theme-components/)

<br>