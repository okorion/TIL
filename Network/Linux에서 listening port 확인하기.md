## 🌌 Linux에서 listening port 확인하기



네트웍이나 특정 서비스 통신이슈를 확인할떄 우선 해야할것이 사용중인 port를 확인하는것이다.

아래 `netstat`,`ss`,`lsof`등 명령을 사용하여 어떠한 서비스가 어떠한 포트를 사용중인지 확인하는 방법을 간단히 소개하고자 한다.

##### `netstat`명령어

netstat는 통신관련된 다양한 정보를 제공하는 명령이며 사용중인 포트 및 socket상태 확인이 가능하다. 사용법은 아래와 같다.

```
1
sudo netstat -tunlp
```

해당 명령에는 아래같은 옵션들이 있다.

- *-t - tcp통신포트*
- *-u -udp통신포트*
- *-n -host,서비스,유저 등을 숫자(ip,port,UID)로 표시*
- *-l -listening port만 노출*
- *-p -PID와 서비스명 노출*

output：

![Linux中查看监听中的（占用）端口（netstat,ss,lsof）](https://p9.toutiaoimg.com/origin/dfic-imagehandler/a3315063-f625-4a2c-a0d6-c7c49000c3ae?from=pc)

자주 보게될 정보는

- *Proto - 프로토콜 종류*
- *Local Address - listening인 로컬 IP와Port*
- *PID/Program name - PID와 서비스명*

grep을 이용하여 결과값에 대한 필터링이 가능하다. 아래와 같이 TCP프로토콜로 22번 포트를 사용중인 서비스를 보고싶다면 아래와 같이 명령을 이용하면 된다.

```
1
sudo netstat -tnlp | grep :22
```

출력결과에서 볼수 있다싶이 22번 포트는 SSH가 사용중이다.

![Linux中查看监听中的（占用）端口（netstat,ss,lsof）](https://p9.toutiaoimg.com/origin/pgc-image/5456c0ad13054ab9b0ab2afe8761faf2?from=pc)

출력결과가 없다면 해당포트를 tcp프로토콜로 사용중인 서비스가 없다는 의미다.

요즘은 ss,ip등 명령으로 *netstat*를 대체하는 추세이기는 하나 대부분 OS버전에서 여전히 사용가능하며 자주 이용하게되는 명령이다.

##### `ss`명령어

`ss`는 socket정보조회가 가능한 또 다른 툴이며 netstat 대체목적으로 나온 명령어이다. *netstat*보다 빠르며 상대적으로 깔끔한 포맷으로 socket정보를 제공한다. 명령어 옵션도 `netstat`랑 비슷하다.

```
1
sudo ss -tunlp
```

output은 *netstat*와 비슷하시지만 포맷차이를 확인할수 있음.

![Linux中查看监听中的（占用）端口（netstat,ss,lsof）](https://p9.toutiaoimg.com/origin/pgc-image/5a3c525a36df48e5b3f42fe86c40711d?from=pc)

##### `lsof`명령어

`lsof`를 프로세스가 열고있는 파일의 상세한 정보를 제공하는 유용한 툴이다.

“Everything is a file” Unix계열 운영체제의 특징이며 socket도 일종의 파일이므로 관련 조회가 가능하다.

`lsof`명령어로 listening port확인

```
1
sudo lsof -nP -iTCP -sTCP:LISTEN
```

사용된 옵션은 아래와 같다

- *-n -host명 대신 ip로 표현。*
- *-p -서비스명 대신 port번호로 표시*
- *-iTCP -sTCP:LISTEN - TCP프로토콜로 LISTEN중인 socket파일들만 조회*

![Linux中查看监听中的（占用）端口（netstat,ss,lsof）](https://p9.toutiaoimg.com/origin/pgc-image/93a2bb436a114244bd8c3d0411b812bb?from=pc)

특정 port만 보고싶다면

```
1
sudo lsof -nP -iTCP:3306 -sTCP:LISTEN
```

아래는 mysql서비스가 3306을 사용중인 case이다.

![Linux中查看监听中的（占用）端口（netstat,ss,lsof）](https://p9.toutiaoimg.com/origin/pgc-image/b04f4ac129884c0597b3416120af3826?from=pc)

이상 `netstat`，`ss`，`lsof` 명령어를 이용하여 listening port 확인하는 방법과 특정 port를 사용중인 프로세스(서비스)를 확인하는 방법을 소개했다.





<br>

<br>

#### 참고링크: [Linux에서 listening port확인하기（netstat,ss,lsof） - Geuni's Blog](https://www.geuni.tech/ko/linux/check_listening_port/)

<br>