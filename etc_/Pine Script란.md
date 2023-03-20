## 🍍 파인 스크립트 (Pine Script)란?

파인 스크립트는 트레이딩뷰가 개발한 프로그래밍 언어입니다. 파인 스크립트를 사용하면 본인만의 지표를 만들고 이를 사용하여 전략을 만들 수 있습니다. 만들어진 전략은 트레이딩뷰가 제공하는 데이터를 사용하여 전략의 성과를 쉽게 백테스팅할 수 있습니다.

파인 스크립트는 일반적인 프로그래밍 언어와 달리 웹 브라우저에서 코드를 작성하고 실행합니다. 또한 파인 스크립트의 코드는 차트의 각 바(bar)마다 실행됩니다. 여러분이 작성한 파인 스크립트 코드는 트레이딩뷰 서버(server)에 저장되면 실행되게 됩니다.



[02) 파인 스크립트 - 파인 스크립트로 나만의 전략 만들기 (wikidocs.net)](https://wikidocs.net/175219)

<br>


### 🌼 ChatGPT Study 🌼



```TradingView
/*
HYPOTHESIS: If a stock closes below its open price more often in the last month compared to the last year, there could be a reversal in the stock price and it may increase in the short term.

IMPLEMENTATION: Buy more of stocks for which such days occur more often (ts_sum) in last month (20 days), compared to the last year (250 days).

HINT TO IMPROVE THE ALPHA: Can introducing the intensity of daily stock fluctuations or price instability improve the alpha?
*/

a = ts_sum(open > close, 20) / ts_sum(open < close, 20);

b = ts_sum(open > close, 250) / ts_sum(open < close, 250);

rank(a / b)
```



 위 코드는 먼저 "가설"과 "구현"을 설명하고, 이에 따라 주식을 매매하는 방법을 구현한 것입니다. 가설은 "만약 주식 종가가 최근 1개월(20일) 동안 개장가보다 종가가 낮은 날이 최근 1년(250일) 동안 보다 더 자주 발생한다면, 주가가 반전하여 단기간 동안 상승할 가능성이 있을 것이다" 입니다.

 구현 방법은, 이러한 조건을 만족하는 주식의 수를 20일 동안과 250일 동안 각각 계산하여 비교한 후, 비율을 구하고, 이를 랭크로 매기는 것입니다. 비율이 높을수록 랭크가 높아지며, 높은 랭크를 가진 주식을 매수하는 전략입니다.

 하지만 이전에 언급한 것처럼, 단순한 수학적 계산만으로는 좋은 매매 전략을 만들기 어렵습니다. 따라서 추가적인 분석과 지식이 필요합니다. 예를 들어, 주가의 변동성과 안정성을 고려하여 조건을 추가하는 것도 가능합니다. 또한, 주가와 관련된 다양한 지표와 정보를 고려하여 전략을 개선하는 것도 중요합니다.
