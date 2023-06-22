## 🥣 git stash 명령어 사용하기

> 하던 작업을 임시로 저장 해두고 싶을 때 사용하는 명령어 git stash

Goal

> - stash 개념과 과정을 이해한다.
> - stash를 적용할 수 있다.
> - stash와 관련된 git 명령어를 확인한다.

**들어가기 전**

자신이 어떤 작업을 하던 중에 다른 요청이 들어와 하던 작업을 멈추고 잠시 브랜치를 변경해야 할 일이 있다고 하자. 이때, 아직 완료하지 않은 일을 commit하는 것은 껄끄럽다. 어떻게 해야 될까?

![img](https://gmlwjd9405.github.io/images/git-stash/git-stash-stashing-changes.png)



#### git stash 란?
아직 마무리하지 않은 작업을 스택에 잠시 저장할 수 있도록 하는 명령어이다. 이를 통해 아직 완료하지 않은 일을 commit하지 않고 나중에 다시 꺼내와 마무리할 수 있다.

- git stash 명령을 사용하면 워킹 디렉토리에서 수정한 파일들만 저장한다.
- stash란 아래에 해당하는 파일들을 보관해두는 장소이다.
  - Modified이면서 Tracked 상태인 파일
    - Tracked 상태인 파일을 수정한 경우
    - Tracked: 과거에 이미 commit하여 스냅샷에 넣어진 관리 대상 상태의 파일
  - Staging Area에 있는 파일(Staged 상태의 파일)
    - git add 명령을 실행한 경우
    - Staged 상태로 만들려면 git add 명령을 실행해야 한다.
    - git add는 파일을 새로 추적할 때도 사용하고 수정한 파일을 Staged 상태로 만들 때도 사용한다.

<br>

#### 1. 하던 작업 임시로 저장하기
**git stash**
위의 명령어를 통해 새로운 stash를 스택에 만들어 하던 작업을 임시로 저장한다.

- 예를 들어, 파일 2개를 수정하고 그 중 하나는 Staging Area에 추가한다. 아직 작업 중인 2개의 파일은 commit할 게 아니기 때문에 모두 stash에 넣는다.
  - index.html: Staging Area에 있는 파일(Staged 상태의 파일)
  - lib/simplegit.rb: Modified이면서 Tracked 상태인 파일

```bash
// working directory에 있는 파일의 상태 확인
$ git status
Changes to be committed:
(use "git reset HEAD <file>..." to unstage)
modified:   index.html
Changes not staged for commit:
(use "git add <file>..." to update what will be committed)
(use "git checkout -- <file>..." to discard changes in working directory)
modified:   lib/simplegit.rb
```



- git stash 나 git stash save 를 실행하면 스택에 새로운 stash가 만들어진다. 이 과정을 통해 working directory는 깨끗해진다.

```$ git stash
$ git stash
$ git stash save
이제 새로운 작업을 위한 다른 브랜치로 변경할 수 있다.
```

<br>



#### 2. stash 목록 확인하기
**git stash list**
여러 번 stash를 했다면 위의 명령어를 통해 저장한 stash 목록을 확인할 수 있다.

```
$ git stash list
stash@{0}: WIP on master: 049d078 added the index file
stash@{1}: WIP on master: c264051 Revert "added file_size"
stash@{2}: WIP on master: 21d80a5 added number to log
```

<br>



#### 3. stash 적용하기(했던 작업을 다시 가져오기)
git stash apply
위의 명령어를 통해 했던 작업을 다시 가져온다.

```
// 가장 최근의 stash를 가져와 적용한다.
$ git stash apply
// stash 이름(ex. stash@{2})에 해당하는 stash를 적용한다.
$ git stash apply [stash 이름]
```

- 위의 명령어로는 Staged 상태였던 파일을 자동으로 다시 Staged 상태로 만들어 주지 않는다. –index 옵션을 주어야 Staged 상태까지 복원한다. 이를 통해 원래 작업하던 파일의 상태로 돌아올 수 있다.

```
// Staged 상태까지 저장
$ git stash apply --index
```



- –index옵션 유무의 차이
  - git stash apply
  - ![img](https://gmlwjd9405.github.io/images/git-stash/apply-option-notinclude.png)
  - git stash apply –index
  - ![img](https://gmlwjd9405.github.io/images/git-stash/apply-option-include.png)

- 수정했던 파일들을 복원할 때 반드시 stash했을 때와 같은 브랜치일 필요는 없다. 만약 다른 작업 중이던 브랜치에 이전의 작업들을 추가했을 때 충돌이 있으면 알려준다.



#### 4. stash 제거하기
**git stash drop**
apply 옵션은 단순히 stash를 적용하는 것으로, 해당 stash는 스택에 여전히 남아있다. 스택에 남아 있는 stash는 위의 명령어을 사용하여 제거할 수 있다.

```
// 가장 최근의 stash를 제거한다.
$ git stash drop
// stash 이름(ex. stash@{2})에 해당하는 stash를 제거한다.
$ git stash drop [stash 이름]
```



- 만약 적용과 동시에 스택에서 해당 stash를 제거하고 싶으면 git stash pop 명령을 사용하면 된다.

```
// apply + drop의 형태
$ git stash pop
```



#### 5. stash 되돌리기
**git stash show -p | git apply -R**
실수로 잘못 stash 적용한 것을 되돌리고 싶으면 위의 명령어를 이용한다.

```
// 가장 최근의 stash를 사용하여 패치를 만들고 그것을 거꾸로 적용한다.
$ git stash show -p | git apply -R
// stash 이름(ex. stash@{2})에 해당하는 stash를 이용하여 거꾸로 적용한다.
$ git stash show -p [stash 이름] | git apply -R
```


**TIP alias로 편리하게 사용하자.**

- stash-unapply라는 명령어를 등록하여 간단하게 사용할 수 있다.

- ```
  $ git config --global alias.stash-unapply '!git stash show -p | git apply -R'
  $ git stash apply
  $ #... work work work
  // alias로 등록한 stash 되돌리기 명령어
  $ git stash-unapply
  ```

<br>

<br>

References
https://git-scm.com/book/ko/v2/Git-%EB%8F%84%EA%B5%AC-Stashing%EA%B3%BC-Cleaning
https://wayhome25.github.io/git/2017/05/16/git-07-stashing-cleaning/
https://code.tutsplus.com/tutorials/quick-tip-leveraging-the-power-of-git-stash–cms-22988
https://gmlwjd9405.github.io/2018/05/18/git-stash.html

<br>

<br>

#### 참고링크: [[Git\] git stash 명령어 사용하기 - Heee's Development Blog (gmlwjd9405.github.io)](https://gmlwjd9405.github.io/2018/05/18/git-stash.html)

<br>