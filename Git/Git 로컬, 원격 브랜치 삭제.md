## 💫 Git 로컬, 원격 브랜치 삭제

## 👀 1. 브랜치 리스트 확인

원격 및 로컬 브랜치 목록을 확인해 봅니다.

명령어는 아래와 같습니다.

```
git branch -a
```

 <br>

결과는 아래의 **그림 1**과 같이 로컬과 원격 브랜치 목록이 모두 출력됩니다.

다시 터미널로 빠져나가고 싶다면 맥북 기준 control + z 키를 눌러주세요.



![img](https://blog.kakaocdn.net/dn/B56NR/btrOighohAJ/bVuhxpzyf12aWRFcsHUs10/img.png)그림 1. 로컬&원격 브랜치 목록 확인



 <br>

원격 저장소에도 마찬가지로 아래의 **그림 2**와 같이 브랜치가 3개 있는 것을 확인하실 수 있습니다.



![img](https://blog.kakaocdn.net/dn/bsT3JR/btrOlCc4JZg/10QL7f6gIMpovrKRy0NYsK/img.png)그림 2. 원격 저장소 내 브랜치 리스트

<br>

## 🔥 2. 로컬 브랜치 삭제

로컬 브랜치 삭제 명령어는 아래와 같습니다.

```
git branch -d 브랜치명
```

 

저는 heytech라는 브랜치를 삭제해 보겠습니다(**그림 3**).



![img](https://blog.kakaocdn.net/dn/dACu0l/btrOlf99nYm/6Jc5KU95kDERIzYsbJmZW1/img.png)그림 3. 로컬 브랜치 삭제 시도

<br>

브랜치 삭제 시 충돌이 발생했다면 아래의 명령어를 통해 강제로 브랜치를 삭제할 수도 있습니다.

```
git branch -D 브랜치명
```

해당 브랜치가 잘 삭제되었는지 확인해 봅니다(**그림 4**).

```
git branch -a
```



![img](https://blog.kakaocdn.net/dn/n8zgQ/btrOkc6SHaG/v6JY6Ge0lT0pMuGi9kKjN1/img.png)그림 4. 로컬 브랜치 삭제 결과

<br>

## 🔥 3. 원격 브랜치 삭제

원격 브랜치 삭제 명령어는 아래와 같습니다.

```
git push origin --delete 브랜치명
```

heytech라는 원격 브랜치를 삭제해 보겠습니다(**그림 5**).



![img](https://blog.kakaocdn.net/dn/mVUnI/btrOjAz2rnc/MHSZBTAr9YTnUI2Hc3RsuK/img.png)그림 5. 원격 브랜치 삭제 결과

<br>

브랜치가 잘 삭제되었는지 확인해 봅니다(**그림 6**).

```
git branch -a
```

다시 터미널로 빠져나가고 싶다면 맥북 기준 control + z 키를 눌러주세요.



![img](https://blog.kakaocdn.net/dn/pGbc9/btrOjA06cRg/E203WPpiXYgIxOB1ckkmD1/img.png)그림 6. 원격 브랜치 삭제 결과(1)

<br>

아래의 **그림 7**과 같이, Github 원격저장소에도 해당 브랜치가 삭제된 것을 확인하실 수 있습니다.



![img](https://blog.kakaocdn.net/dn/dyWxKm/btrOlKPtlvb/VOVLhgB5imxndJZjfwZ3Ck/img.png)그림 7. 원격 브랜치 삭제 결과(2)



------

포스팅 내용에 오류가 있다면 아래에 댓글 남겨주세요.

그럼 오늘도 즐거운 하루 보내시길 바랍니다 :)

고맙습니다😊

<br>

<br>

#### 참고링크: [[Git\] 로컬/원격 브랜치 삭제 방법 (tistory.com)](https://heytech.tistory.com/463)

<br>