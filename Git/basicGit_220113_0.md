# BasicGit
## 기본 문법

    $ cd ..  # 현재 폴더의 상위 폴더로 이동
  
    $ cd .  # 현재 폴더로 이동
    
    $ git add . 현재 폴더 스테이징

##
    $ mkdir (Directory name)  # 디렉토리 만들기

    $ rm (삭제할 파일명)  # 현재 위치의 파일 삭제
 
    $ mv (변경 전 파일명) (변경 후 파일명)  # 현재 위치의 파일명 변경

##
    $ git log  # git commit 히스토리 조회  # git log 탈출 :q

    $ git status -> git 수정된 항목 조회

    $ ls  # 현재 위치의 모든 파일 조회

    $ pwd  # 현재 작업 위치


##
    $ ctrl + l  # 터미널 입력창 상단 이동

    $ clear  # 터미널 실행 내역 삭제


* 터미널 입력창 > (not $) 탈출, cmd 루프 탈출 등 -> (ctrl + c)

## git 등록 순서
> * 편집기 ctrl + s 저장

    $ git add .  # git 스테이징

    $ git commit -m "(commit message)"  # commit을 해야 github 카운트

    $ git push origin master  # git -> github 푸시

## .gitignore 등록 순서

    $ touch .gitignore  # repo 폴더에 생성

> * .gitignore 에서 무시할 파일 목록 작성. 예) *.txt
> * git push 뒤에 생략 금지.

