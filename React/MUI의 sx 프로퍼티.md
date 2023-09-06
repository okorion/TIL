## 💎 MUI의 sx 프로퍼티

처음 저를 혼란에 빠뜨린 프로퍼티이기도 합니다.

sx 프로퍼티는 불필요한 스타일 구성 요소 코드 작성을 피하고

대신 구성 요소 자체 내에서 직접 스타일을 정의하는 방법입니다.

얼핏 보면 jsx 문법의 style={} 프로퍼티와 비슷하면서도 내부 사용은 tailwindcss와 비슷해보이기도 합니다.

```bash
<Box
  sx={{
    bgcolor: 'background.paper',
    boxShadow: 1,
    borderRadius: 1,
    p: 2,
    minWidth: 300,
  }}
>
  <Box sx={{ color: 'text.secondary' }}>Sessions</Box>
  <Box sx={{ color: 'text.primary', fontSize: 34, fontWeight: 'medium' }}>
    98.3 K
  </Box>
  <Box
    component={TrendingUpIcon}
    sx={{ color: 'success.dark', fontSize: 16, verticalAlign: 'sub' }}
  />
  <Box
    sx={{
      color: 'success.dark',
      display: 'inline',
      fontWeight: 'medium',
      mx: 0.5,
    }}
  >
    18.77%
  </Box>
  <Box sx={{ color: 'text.secondary', display: 'inline', fontSize: 12 }}>
    vs. last week
  </Box>
</Box>
```

sx라는 프로퍼티에 객체의 형태로 값을 넣어주어야하니

{{}} 형태가 됩니다.

자동완성은 지원되기는 하는데 제 기준에서는 살짝 느리더라구요

mx , mb, mt등 단축된 이름으로도 속성을 적용할 수 있습니다.

테일윈드에 익숙하다면 예상할 수 있듯이 마진에 대한 속성입니다.

 

sx는 디자인 토큰을 일회성으로 사용할때 빠르고 효율적인 솔루션이 됩니다.

만약 디자인 토큰들을 일회성으로 한 컴포넌트에서만 사용할것인데

styledcomponent를 이용한다면 어떻게 될까요?

```bash
const StatPrevious = styled('div')(
  ({ theme }) => `
  color: ${theme.palette.text.secondary};
  display: inline;
  font-size: 12px;
`,
);
```

이렇게 변수를 만들고 그 안에 styled로 래핑을 해주는 불필요한 형태가 됩니다.

sx 프로퍼티는 반응형도 간단히 지원할 수 있습니다.

```bash
      <Box
        component="img"
        sx={{
          height: 233,
          width: 350,
          maxHeight: { xs: 233, md: 167 },
          maxWidth: { xs: 350, md: 250 },
        }}
        alt="The house from the offer."
        src="https://images.unsplash.com/photo-1512917774080-9991f1c4c750?auto=format&w=350&dpr=2"
      />
```

이런 형태로요!

```bash
<Box sx={{ width: [100, 200, 300] }}>This box has a responsive width.</Box>
```

배열 형태로도 지정해줄 수 있지만

많은 브레이크포인트를 설정해줘야하는 경우면 object 형태로 작성하는 걸 더 추천하네요

 

 

mui의 설명에 따르면

재사용하기 좋은 컴포넌트를 구축하는 데 이상적인 styled component 의 방식과 대조적으로

일회성으로 사용하는 css를 설정해줄때 sx가 좋다고합니다.

 

위에서 본 바와같이 mx, mb 등 약식 정의를 지원하기 때문에 이를 사용할 수 있지만

약식 정의만 사용 가능한 것은 아닙니다.

 

sx는 모든 핵심 mui 구성요소에서 지원됩니다.

https://mui.com/system/getting-started/the-sx-prop/

 

The sx prop - MUI System

The sx prop is a shortcut for defining custom styles that has access to the theme.

mui.com

여기서 간단히 넣을 수 있는 값들을 체크할 수 있습니다.

 

공유하기

게시글 관리

*구독하기*

<br>

<br>

#### 참고링크: [mui 개념과 사용 방법 시작하고 sx 프로퍼티 알아보기 — React와 JavaScript를 좋아하는 개발자 (tistory.com)](https://xionwcfm.tistory.com/364)

<br>