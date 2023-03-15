## 광역 네트워크(WAN)란?

광역 네트워크(WAN)는 먼 거리에 있는 컴퓨터 그룹을 연결하는 대규모 컴퓨터 [네트워크](https://www.cloudflare.com/learning/network-layer/what-is-the-network-layer/)입니다.WAN은 대기업에서 사무실 네트워크를 연결하는 데 자주 사용합니다. 각 사무실에는 일반적으로 자체 근거리 통신망(LAN)이 있으며, 이러한 LAN은 [WAN](https://www.cloudflare.com/learning/network-layer/what-is-a-lan/)을 통해 연결됩니다.이러한 긴 연결은 임대 회선, [VPN](https://www.cloudflare.com/learning/access-management/what-is-a-vpn/), IP 터널 등 여러 방법으로 형성될 수 있습니다(아래 참조).

WAN의 구성 요소에 대한 정의는 상당히 광범위합니다.기술적으로는, 넓은 지리적 영역에 걸쳐 분산된 모든 대규모 네트워크가 WAN입니다.[인터넷](https://www.cloudflare.com/learning/network-layer/how-does-the-internet-work/) 자체도 WAN으로 간주됩니다.

![광역 네트워크(WAN) - 연결된 여러 LAN](https://www.cloudflare.com/resources/images/slt3lc6tev37/6ARE3uWw7nvYn4VhyNh1Z6/d92a3e1bfa0878adb6c93ac91b12b98f/what_is_WAN_wide_area_network.png)

## LAN이란 무엇인가요?

근거리 통신망(LAN)은 작고 지역화된 영역으로 제한된 네트워크입니다. 홈 WiFi 네트워크와 소규모 사업체 네트워크는 LAN의 일반적인 예입니다. 일반적으로 LAN을 관리하는 사람은 사용하는 네트워킹 장비도 관리합니다. 예를 들어 중소기업에서는 LAN 설정과 관련된 [라우터](https://www.cloudflare.com/learning/network-layer/what-is-routing/)와 [스위치](https://www.cloudflare.com/learning/network-layer/what-is-a-network-switch/)를 관리합니다.

## WAN과 LAN의 비교

LAN은 일반적으로 한정된 영역에 존재하며 일반적으로 인터넷 연결의 단일 중앙 지점을 공유합니다. WAN은 먼 거리에 걸쳐 네트워크 연결을 제공하도록 설계되었습니다. WAN은 일반적으로 여러 개의 연결된 LAN으로 구성됩니다. 자체 WAN을 설정하는 조직에서는 거의 항상 자체에서 통제할 수 없는 네트워크 인프라에 의존합니다. 예를 들어 파리에 사무실이 있고 뉴욕에 사무실이 있는 회사는 대서양을 가로지르는 해저 케이블을 통해 이들 사무실 간에 데이터를 전송해야 합니다.

일반적으로 WAN에는 여러 라우터와 스위치가 포함됩니다. LAN은 스위치를 사용할 수도 있지만, 인터넷이나 다른 LAN에 연결하기 위해 하나의 라우터만 필요합니다.

## 임대 회선이란?

조직에서 LAN을 연결하여 WAN을 형성하는 방법 중 하나는 임대 회선이라는 것을 사용하는 것입니다. 임대 회선은 ISP와 같은 대규모 네트워크 공급자로부터 임대하는 직접 네트워크 연결입니다. 수백 또는 수천 마일에 걸쳐 케이블, 라우터, 인터넷 익스체인지 포인트를 포함한 자체 물리적 네트워크 인프라를 구축하는 것은 대부분의 조직에서는 거의 불가능한 작업입니다. 따라서 대신 이미 이 인프라가 있는 회사로부터 직접 전용 연결을 임대합니다.

## 터널링이란? VPN이란?

회사에서 임대 회선에 대한 비용을 지급하지 않으려면 [터널링](https://www.cloudflare.com/learning/network-layer/what-is-gre-tunneling/)을 사용하여 LAN을 연결할 수 있습니다.네트워킹에서 터널링은 데이터 [패킷](https://www.cloudflare.com/learning/network-layer/what-is-a-packet/)*을 다른 데이터 패킷 내에 캡슐화하여 다른 방법으로는 가지 못할 곳으로 이동하도록 하는 방법입니다.두 봉투의 주소가 다른 경우에 한 봉투 안에 다른 봉투를 넣어서 내부 봉투가 외부 봉투의 대상 주소로 우편으로 발송된다고 상상해 보세요.이것이 터널링의 일반적인 개념이지만, 데이터는 봉투 대신 패킷 내에 포함됩니다.

일부 네트워크 터널은 패킷의 내용을 도중에 가로챌 수 있는 사람으로부터 보호하기 위해 [암호화](https://www.cloudflare.com/learning/ssl/what-is-encryption/)됩니다.암호화된 터널을 VPN, 즉 가상 사설망이라고 합니다.WAN 간의 VPN 연결은 암호화되지 않은 터널링 연결보다 더 안전합니다.[IPsec](https://www.cloudflare.com/learning/network-layer/what-is-ipsec/)은 일반적인 VPN 암호화 프로토콜 중 하나입니다.

터널링을 사용하여 LAN을 연결할 때의 주요 단점은 터널링 때문에 간접 비용이 늘어난다는 것입니다. 이러한 방식으로 패킷을 보내는 데는 더 많은 컴퓨팅 성능과 더 많은 시간이 필요합니다. 봉투 두 개에 를 우편물을 넣으면 우체통에 넣을 수 있는 속도가 느려지는 것처럼 각 패킷을 캡슐화하고 암호화하면 통신 속도가 느려집니다. 또한 패킷을 캡슐화하면 네트워크의 일부 라우터에서 처리할 수 있는 것보다 커져 [분편화](https://www.cloudflare.com/learning/network-layer/what-is-mtu/)가 발생하고 지연 시간이 늘어날 수 있습니다.

**네트워크를 통해 전송되는 모든 데이터는 더 작은 데이터 청크인 패킷으로 나뉩니다. 각 패킷에는 패킷의 원본, 대상, 일련의 패킷 위치에 대한 정보가 포함됩니다.*





참고링크: [WAN이란? | WAN과 LAN의 비교 | Cloudflare](https://www.cloudflare.com/ko-kr/learning/network-layer/what-is-a-wan/)