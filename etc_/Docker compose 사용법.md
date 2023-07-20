## 🐳 Docker compose 사용법

## **Docker Compose 개요**

------

 Docker compose란, 여러 개의 컨테이너로부터 이루어진 서비스를 구축, 실행하는 순서를 자동으로 하여, 관리를 간단히하는 기능이다.

 Docker compose에서는 compose 파일을 준비하여 커맨드를 1회 실행하는 것으로, 그 파일로부터 설정을 읽어들여 모든 컨테이너 서비스를 실행시키는 것이 가능하다.

 

<br>

 

## **Docker Compose를 사용하기까지의 주요한 단계**

------

 Docker compose를 사용하기 위해서는, 크게 나눠 아래의 세 가지 순서로 이루어진다.

1 ) 각각의 컨테이너의 Dockerfile를 작성한다(기존에 있는 이미지를 사용하는 경우는 불필요).

2 ) docker-compose.yml를 작성하고, 각각 독립된 컨테이너의 실행 정의를 실시한다(경우에 따라는 구축 정의도 포함).

3 ) "docker-compose up" 커맨드를 실행하여 docker-compose.yml으로 정의한 컨테이너를 개시한다.

 Docker compose는 start, stop, status, 실행 중의 컨테이너의 로그 출력, 약간의 커맨드의 실행이과 같은 기능도 가지고 있다.

 

<br>

 

## **docker-compose.yml 파일이란**

------

docker-compose.yml 파일은 아래와 같이 yaml으로 Docker 컨테이너에 관한 실행 옵션(build 옵션도 포함되어 있는 경우도 있다)를 기재한 파일이 된다.

```
web:
  build: .
  ports:
   - "5000:5000"
  volumes:
   - .:/code
  links:
   - redis
redis:
  image: redis

# yaml의 기재 방법에 대해서는 아래의 링크를 참고하길 바란다.
# https://docs.docker.com/compose/compose-file/
```

 이 파일에 기재되어 있는 내용은 기본적으로 docker build, docker run 커맨드 지정하는 것이 가능한 옵션이 되지만, Docker compose의 yaml 파일로써 기술하는 것으로 여러 개의 컨테이너로부터 만들어진 서비스를 조감하여 보는 것도 가능해져, 보존성의 수고를 가볍게 한다.

 

 

<br>

<br>

## **Docker compose의 설치**

------

 기본적으로 docker compose의 릴리즈 페이지에 액세스해서 최신 정보를 확인하고, Docker compose를 설치하는 흐름이 된다.

 [Docker compose release page](https://github.com/docker/compose/releases)

 curl 커맨드를 사용하여 아래와 같이 작성면 설치가 완료된다.

```
sudo COMPOSE_VERSION=버전 bash -eu << '__EOT__'
echo ${COMPOSE_VERSION}
curl -L https://github.com/docker/compose/releases/download/${COMPOSE_VERSION}/docker-compose-`uname -s`-`uname -m` > /usr/local/bin/docker-compose
chown root:docker /usr/local/bin/docker-compose
chmod ug+x /usr/local/bin/docker-compose
update-alternatives --install /usr/bin/docker-compose docker-compose /usr/local/bin/docker-compose 10
__EOT__
```

 설치가 완료되면, docker-compose 커맨드를 실행하여 동작을 확인해보자.

```
$ docker-compose --version
docker-compose version 버전, build 7240ff3
```

 version가 출력되면 설치 성공이다.

 

 

<br>

<br>

## **이번에 동작 확인을 실행할 환경에 대해서**

------

 이번에 Docker Compose의 작성법과 관련된 파일의 구성은 다음과 같이 되어 있다.

```
(Working dir)
+- docker-compose.yml
+- app-server/
   +- Dockerfile
   +- src/
     +- app.js
```

 

 

<br>

<br>

## **Docker compose를 사용한 간단한 샘플**

------

 Docker compose를 사용한 여러 개의 컨테이너를 하나의 서비스를 작성하는 샘플을 구현해보자. 공식 사이트의 내용과 거의 동일하지만, redis를 사용하여 액세스 수를 카운트하는 간단한 어플리케이션을 만들어보자.

 

 

<br>

## **application의 작성**

------

```
FROM node:5
RUN npm -g install redis
ENV NODE_PATH /usr/local/lib/node_modules

ENTRYPOINT ["node", "app.js"]
```

 다음은 nodejs의 소스코드(app-server/src/app.js)를 작성하자. 디렉토리를 아래와 같이 작성한다.

```
var redis = require('redis');
var redis_client = redis.createClient(6379, "noderedis");
var listen_port = 10080;

require('http').createServer(function (request, response) {
    redis_client.incr('counter', function(error, reply) {
        response.writeHead(200, {'Content-Type': 'text/plain'});
        response.end("You accessed here " + reply + " times.\n");
    });
}).listen(listen_port, '0.0.0.0');
console.log("Server is running on port " + listen_port + ".");
```

 

<br>

<br>

 

## **Redis의 작성**

------

 Redis의 컨테이터의 작성을 하지만, 공식의 Redis 이미지를 사용하기 위하므로 여기서 Dockerfile은 필요로 하지 않다.

 

<br>

## **Docker compose 파일의 작성**

------

 어플쪽의 node 어플리케이션과 redis의 어플리케이션을 build, run하기 위한 정의를 build, run하기 위한 정의를 docker-compose 파일(docker-compose.yml)에 기재한다.

```
nodeapp:
  build: "./app-server"
  container_name: "nodeapp"
  working_dir: "/usr/src/app"
  ports:
   - "10080:10080"
  volumes:
   - "$PWD/app-server/src:/usr/src/app"
  links:
   - "noderedis"
noderedis:
  image: "redis:3"
  container_name: "noderedis"
```

 Dockerfile에 "ENTRYPOINT"를 쓰지 않은 경우에는 docker-compose.yml에 아래와 같이 기재하는 방법으로 대응할 수 있다.

```
nodeapp:
  ......
  command: node app.js
```

 이번에는 node의 어플리케이션을 싣을 컨테이너는 Dockerfile부터 이미지를 build해 여기서부터 nodeapp이라는 이름의 컨테이너를 실행한다. 

 redis가 있는 컨테이너에 관해서는 Dockerfile로부터 이미지를 build하지 않고 Docker hub부터 pull해 온 공식 이미지를 이용해, 여기서 부터는 noderedis이라는 이름의 컨테이너를 실행한다.

 docker-compose.yml 파일에 있는 디렉토리까지 이동해, docker-compose up 커맨드를 실행한다.

```
$ docker-compose up
...
```

 node 어플리케이션과 redis 어플리케이션의 컨테이너가 동시에 실행되어, 하나의 콘솔상에 각각의 컨터네이너 태그를 붙어 로그가 출력된다. 

<br>

 작동을 확인해보자.

```
$ curl http://localhost:10080
You accessed here 1 times.
$ curl http://localhost:10080
You accessed here 2 times.
$ curl http://localhost:10080
You accessed here 3 times.
```

 위와 같이 redis로 부터 데이터를 얻어내어 액세스 수가 카운트되면 성공이다.

 

<br>

<br>

 

## **docker-compose 커맨드로 작성된 이미지명에 대해서**

------

docker-compose up 커맨드를 사용하는 것으로 자동적으로 Docker 이미지도 작성해주지만, 그 이미지는 아래와 같은 이미지가 된다.

```
$ docker images
REPOSITORY                           TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
dockercomposeexamplesimple_nodeapp   latest              7d39370b4309        23 hours ago        643.5 MB
redis                                3                   0c4334bed751        4 days ago          151.3 MB
node                                 5                   285fd945c0b6        2 weeks ago         642.7 MB
debian                               jessie              23cb15b0fcec        4 weeks ago         125.1 MB

$ docker ps -a
CONTAINER ID        IMAGE                                COMMAND                  CREATED             STATUS              PORTS                                NAMES
e48a2014b88d        dockercomposeexamplesimple_nodeapp   "node app.js"            4 minutes ago       Up 4 minutes        0.0.0.0:10080->10080/tcp   nodeapp
b8b47ca9a285        redis:3                              "/entrypoint.sh redis"   23 hours ago        Up 4 minutes        6379/tcp                             noderedis
```

 출력된 결과를 확인하면, Redis에 대해서는 Docker Hub 공식으로 부터 pull해 온 이미지이므로 redis:3 이라는 알기 쉬운 이미지명 (+태그)이지만, nodejs에 대해서는 dockercomposeexamplesimple_nodeapp이라는 이미지명이 자동적으로 붙어있다. 

 이 이미지는 최종적으로 nodejs의 컨테이너로써 docker-compose.yml내에 지정된 이름으로 작성되어 있으므로, 동작상 문제는 없다(예를 들어 link로 이 nodejs 컨테이너와 연결할 필요성이 있는 컨테이너가 나와도 docker-compose.yml내에서 지정한 것이 되므로, 미리 연결할 곳의 컨테이너명을 추론할 수 있고, 구축의 자동화에 지장이 없다).

 그러나 어떻게 해도 보기에는 좋지 않으므로, 직접 docker 커맨드를 실행하여 구축하는 경우에 난잡한 이미지의 리스트를 보기 싫은 경우게 사전에 build한 docker 이미지를 지정하여 compose-up를 실행하는 방법이 있다.



<br> 먼저, docker-compose.yml 파일을 아래와 같이 편집한다. 먼저 사용한 파일은 image: 요소가 추가되어, build: 요소가 삭제된 형태가 된다.

```
nodeapp:                            # <- 서비스명
  image: "tsutomu/nodeapp"          # <- 사용하는Docker이미지명(이후에 빌드한다)
  container_name: "nodeapp"         # <- 컨테이너명. 지정하지 않은 경우에Docker compose로 임의로 결정된다.
  working_dir: "/usr/src/app"       # <- 컨테이너 내의 워킹 디렉토리. docker run커맨드의 -w/--workdir에 상당한다.
  ports:                            # <- Expose할 포트. docker run커맨드의 -p/--publish에 상응한다.
   - "10080:10080"
  volumes:                          # <- Bind mount하는 디렉토리. volume. docker run커맨드의 -v/--volume에 상당한다.
   - "$PWD/app-server/src:/usr/src/app"
  links:                            # <- 다른 컨테이너와 접속할 때의 컨테이너명. docker run 커맨드의 -link에 해당한다.
   - "noderedis"
noderedis:
  image: "redis:3"                  # <- 이미지ID와 tag
  container_name: "noderedis"
```



<br>

 새로 추가한 image: 의 값에 일치하도록 docker build 커맨드로 이미지를 작성하고, docker-compose up 커맨드로 컨테이너를 실행한다.

```
$ docker build -t "tsutomu/nodeapp" ./app-server
```

<br>

 여기서 이미지명과 컨테이너명을 확인해보자. 아까와 달리, docker-compose에 의해 작성된 이미지는 존재하지 않는다.

```
$ docker images
REPOSITORY          TAG                 IMAGE ID            CREATED             VIRTUAL SIZE
tsutomu/nodeapp     latest              2169cc98c4e2        2 minutes ago       643.5 MB
redis               3                   0c4334bed751        4 days ago          151.3 MB
node                5                   285fd945c0b6        2 weeks ago         642.7 MB
debian              jessie              23cb15b0fcec        4 weeks ago         125.1 MB

$ docker ps -a 
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                                NAMES
d9c9f2a70735        tsutomu/nodeapp     "node app.js"            9 seconds ago       Up 8 seconds        8888/tcp, 0.0.0.0:10080->10080/tcp   nodeapp
e295c5ff24fc        redis:3             "/entrypoint.sh redis"   9 minutes ago       Up 9 minutes        6379/tcp                             noderedis
```

------

참고자료

https://qiita.com/TsutomuNakamura/items/7e90e5efb36601c5bc8a

<br>

<br>

#### 참고자료: [[Docker\] docker compose 사용법 (tistory.com)](https://engineer-mole.tistory.com/221)

<br>