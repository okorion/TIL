## 🛴 git commit --amend 명령어

 <br>

현업에서 git 은 필수이다. 특히 회사에서 협업할 때, 얼마나 아느냐가 작업시간을 좌지우지 하기도 한다.

오늘이 그런 날이었다. commit 을 하자마자 수정사항이 생겼다. 너무 마이너해서 다시 커밋하기도 민망하다면?

 <br>

덮어 씌워 버리자! 오늘 소개할 녀석은 amend 라는 옵션이다. 

한글 문서에는 '저장' 과 '다른이름으로 저장'이라는 기능이 있다. '저장' 기능은 그 파일 안에 새로운 내용으로 저장된다.

깃의 amend도 '저장' 기능처럼 그 커밋 위에 새로운 내용을 덮어 저장하는 기능이다.

 <br>

![img](https://blog.kakaocdn.net/dn/tUasL/btrdBp7WVmz/pIc3lJV9ztxQNtZb1cXpvK/img.png)

 <br>

 <br>

------

## Git(25) git commit --amend 커밋 수정 후 덮어쓰기

 

 <br>

amend 는 마지막 커밋에 + 추가할 사항이 있는 경우 (메시지든, 코드이든, 파일이든) 

마지막 커밋에 덮어씌우는 옵션이다. 다음 예제를 참고해보자

 

 <br>

**1. 커밋을 두번 했다. first commit 과 last commit 이다.**

```
$ git log

commit ddca6c21e365b9e714e91d5b40e39d0c87a83832
Author: saebal <saebal@gmail.com>
Date:   Sat Jan 16 23:17:56 2021 +0900

    last commit 

commit 9d130c1f91b6922ceed41e5ad5c1c6da37863ce8
Author: saebal <saebal@gmail.com>
Date:   Sat Jan 16 23:16:14 2021 +0900

    first commit
```

 

 <br>

 <br>

**2. 마지막 커밋에 Add.js 도 포함시키고 싶다면 아래와 같이 해보자.**

git add 로 스테이징 하고, amend 옵션으로 커밋한다. 이때 커밋메시지도 수정해봤다.

```
$ git add Add.js				# 파일 추가(staging)하고 
$ git commit --amend -m “last commit and Add.js” # amend 옵션을 넣어 커밋한다.
```

 <br>

 <br>

**3. 깃 로그를 보면 마지막 커밋 위에 추가된 내용과 메시지가 무사히 덮어씌워졌다.**

마지막 커밋 메시지는 last commit 이었다가 last commit and Add 로 변경되었다.

```
$ git log

commit ddca6c21e365b9e714e91d5b40e39d0c87a83832
Author: saebal <saebal@gmail.com>
Date:   Sat Jan 16 23:19:56 2021 +0900

    last commit and Add

commit 9d130c1f91b6922ceed41e5ad5c1c6da37863ce8
Author: saebal <saebal@gmail.com>
Date:   Sat Jan 16 23:16:14 2021 +0900

    first commit
```

 <br>

 <br>

 <br>

ref: https://backlog.com/git-tutorial/kr/stepup/stepup7_1.html

 <br>

### 참고링크: https://devbirdfeet.tistory.com/127