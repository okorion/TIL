

# Amazon CloudFront Functions — 더 짧은 지연 시간으로 엣지에서 코드 실행을 위한 신규 기능



![img](https://jirak.net/wp/wp-content/uploads/2021/05/cloudfront-functions-where-1024x532-1-678x381.png)

Amazon CloudFront Functions — 더 짧은 지연 시간으로 엣지에서 코드 실행을 위한 신규 기능
![img](https://jirak.net/wp/wp-content/uploads/2021/05/cloudfront-functions-where-1024x532-1.png)

[Amazon CloudFront](https://aws.amazon.com/cloudfront/)를 사용하면 짧은 지연 시간과 빠른 전송 속도로 전 세계 고객에게 데이터, 비디오, 애플리케이션 및 API를 안전하게 전송할 수 있습니다. 사용자 지정 경험을 제공하고 가장 낮은 지연 시간을 제공하기 위해 대부분의 최신 애플리케이션은 엣지에서 특정 형태의 로직(Logic)을 실행합니다. 엣지에 로직을 적용하는 사용 사례는 두 가지 주요 범주로 그룹화할 수 있습니다.

- 첫 번째 범주는 객체가 캐시에 없을 때 실행되는 컴퓨팅 집약적인 복잡한 작업입니다. 여러 복잡한 사용자 지정을 구현할 수 있는 완전히 프로그래밍 가능한 서버리스 엣지 컴퓨팅 환경을 제공하기 위해 2017년에 [Lambda@Edge](https://aws.amazon.com/lambda/edge/)를 [출시](https://aws.amazon.com/ko/blogs/korea/coming-soon-lambda-at-the-edge/)하였습니다. Lambda@Edge 함수는 [리전 엣지 캐시](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/HowCloudFrontWorks.html#CloudFrontRegionaledgecaches)(일반적으로 클라이언트가 접속하는 CloudFront 엣지 로케이션에 가장 가까운 [AWS 리전](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/))에서 실행됩니다. 예를 들어, 비디오 또는 오디오를 스트리밍할 때 Lambda@Edge를 사용하여 적절한 세그먼트를 즉시 만들고 제공할 수 있으므로 오리진 확장성에 대한 필요성을 줄일 수 있습니다. 또 다른 일반적인 사용 사례는 Lambda@Edge 및 [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)를 사용하여 단축된 사용자 친화적인 URL을 전체 URL 방문 페이지로 변환하는 것입니다.
- 사용 사례의 두 번째 범주는 수명이 매우 짧은 함수로 실행할 수 있는 간단한 HTTP 요청/응답 조작입니다. 이러한 사용 사례에는 모든 요청에서 실행할 수 있는 성능, 확장성 및 비용 효율성을 갖춘 유연한 프로그래밍 환경이 필요합니다.

이 두 번째 범주의 사용 사례를 지원하기 위해 새로운 서버리스 스크립팅 플랫폼, [**CloudFront Functions**](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/cloudfront-functions.html)의 가용성을 발표하게 되어 정말 기쁩니다. 이를 통해 Lambda@Edge 요금의 약 1/6의 비용으로 [218개 이상의 CloudFront 엣지 로케이션](https://aws.amazon.com/cloudfront/features/#Global_Edge_Network)에서 경량 JavaScript 코드를 실행할 수 있습니다.

[![아키텍처 다이어그램.](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2021/04/01/cloudfront-functions-where-1024x532.png)](https://d2908q01vomqb2.cloudfront.net/da4b9237bacccdf19c0760cab7aec4a8359010b0/2021/04/01/cloudfront-functions-where.png)

CloudFront Functions는 웹 요청의 경량 처리에 이상적입니다. 예를 들어, 다음과 같습니다.

- **캐시 키 조작 및 정규화**: HTTP 요청 속성(예: URL, 헤더, 쿠키 및 쿼리 문자열)을 변환하여 캐시 키를 구성합니다. 캐시 키는 캐시에 있는 객체의 고유 식별자이며, 객체가 이미 캐싱되었는지 여부를 확인하는 데 사용됩니다. 예를 들어, 최종 사용자의 디바이스 유형을 포함하는 헤더를 기반으로 캐싱하여 모바일 및 데스크톱 사용자를 위한 두 가지 버전의 콘텐츠를 생성할 수 있습니다. 요청 속성을 변환하여 여러 요청을 단일 캐시 키 항목으로 정규화하고 캐시 적중률을 크게 향상시킬 수도 있습니다.
- **URL 다시 쓰기 및 리디렉션**: 요청을 다른 URL로 리디렉션하는 응답을 생성합니다. 예를 들어, 인증되지 않은 사용자를 제한된 페이지에서 로그인 양식으로 리디렉션합니다. URL 다시 쓰기는 [A/B 테스트](https://en.wikipedia.org/wiki/A/B_testing)에도 사용할 수 있습니다.
- **HTTP 헤더 조작**: 요청/응답 헤더를 보거나 추가, 수정 또는 삭제합니다. 예를 들어, [HTTP Strict Transport Security(HSTS)](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security) 헤더를 응답에 추가하거나 요청과 함께 오리진으로 전달되도록 클라이언트 IP 주소를 새 HTTP 헤더에 복사합니다.
- **액세스 권한 부여**: 요청을 허용/거부하기 위해 [HMAC](https://en.wikipedia.org/wiki/HMAC) 토큰 또는 [JSON 웹 토큰(JWT)](https://en.wikipedia.org/wiki/JSON_Web_Token)과 같은 사용자 생성 토큰을 생성 및 검증하여 CloudFront를 통해 전송되는 콘텐츠에 대한 액세스 제어 및 권한 부여를 구현합니다.



참고링크: [Amazon CloudFront Functions — 더 짧은 지연 시간으로 엣지에서 코드 실행을 위한 신규 기능 – 지락문화예술공작단 (jirak.net)](https://jirak.net/wp/amazon-cloudfront-functions-더-짧은-지연-시간으로-엣지에서-코드-실행/)



[웹개발, 서버사이드 렌더링의 미래? 😎 (필수 키워드 정리) - YouTube](https://www.youtube.com/watch?v=RLJ6tPzXB5Q&list=WL&index=44&t=1s)

