**이번 포스팅에서는 json대신에 db 데이터를 불러올건데용**

****

**원리는 사실 크게 달라지지 않습니다.**

![img](https://postfiles.pstatic.net/MjAyMDExMDlfMTc0/MDAxNjA0OTAxNjcxNDM5.qfkPQnrux4XQQEslPuK--vE_PxXaLr2T9_8OnljlCsQg.-vh_D-1fo_Zti1bh1aVHzHi2nJutxo46Hxmgp8iXiZIg.PNG.ks2414e/20201109145956.png?type=w773)

**백엔드 뒤에 숨어있는 단계라고 생각하시면 되는데요**

****

**쉽게 생각하면**

**프론트엔드 : 사용자에게 보이는 화면**

**백엔드 : 사용자에게 보이지 않는 화면**

**데이터베이스 : 화면에 필요한 정보를 담는 곳**

****

**이렇게 생각하시면 됩니다. 대부분 백엔드를 db와 같이 생각하시는 분들이 많은데**

**백엔드도 결국엔 화면입니다.** 

**더 정확하게 말하면 백엔드가 db와 연결해주는 다리라고 생각하시면 됩니다.**

****

**자 이제 보시면**

![img](https://postfiles.pstatic.net/MjAyMDExMDlfMTM2/MDAxNjA0OTAxNjcxMjcw.upL8eqYMXeAhXyOkPJVjW55iMVUO1UgpPILKtt0-iGQg.eUjFPsf_49_uA74T3dd_CONC9GD9kk2mTN8o4tCQIw0g.PNG.ks2414e/20201109143625.png?type=w773)

**저번에 했던 백엔드 서버 파일인데, 처음보시는 분들은 이것만 봐도 뭔가 복잡해서 더이상 알고 싶지 않죠?**

**이럴 때는 파일을 분리하는게 좋습니다.**

**저도 막 처음하는 프로그래밍인데, 별거아닌데도 모여있으면 앞이깜깜해지고 답답해집니다 ㅋㅋ**

**그래서 저는 db를 여기다가 다 부르지 않고**

![img](https://postfiles.pstatic.net/MjAyMDExMDlfMjY0/MDAxNjA0OTAxNjcxMjcw.oMqSJdwDqSoRGCU7Rep-nu5KKNgkdDH6-nUtzSL-wScg.nOHRRs3tb16hktr8jD4ug5rDcztUQ5D0kJKv4TTsibMg.PNG.ks2414e/20201109144229.png?type=w773)

**이렇게 나눠서 할건데요.**

**그러면 하시는 분들이** 

**"이거 초보만 이렇게하는건가? 나중엔 결국합쳐야하는거아닌가?"라고 생각하실 수 있는데**

**절대 아닙니다. 이게 오히려 더 좋습니다. 유지보수나 가독성 면에서요.**

**회사에서도 합쳐서 쓰는 곳도 물론 존재하지만 나눠서 쓰는곳있고 나눠서 쓴다고해서 뭐라하는 곳 없습니다.**

**(mysql.js는 query문 쓰느라 잠깐 만들어놨습니다. 하실 필요없어용)**

![img](https://postfiles.pstatic.net/MjAyMDExMDlfMjU1/MDAxNjA0OTAxNjcxMjc1.7sKzJmD2-O1eJ6KcObPeZtogum4cTHfFoj3PIRsXLO0g.BVykIlAAkY_a2k7aKg-b61zO5yDora_P2uBpCBpYudcg.PNG.ks2414e/20201109144346.png?type=w773)

**일단 db라는 파일에서 이렇게 db접속 처리를 할겁니다.**

![img](https://postfiles.pstatic.net/MjAyMDExMDlfMjk5/MDAxNjA0OTAxNjcxMjc3.MchhLL74usumjpGJhaIrj_EH7R86UusWzIaX-vtuO9Ag.NF3n75-8o1jJWWrQIc6s1SA2YJ2-mlSs2mv1SVHoJyYg.PNG.ks2414e/20201109144533.png?type=w773)

**그리고 이렇게 일단 db를 불러주세용**

**이건 그냥 파일 가져오는거니까 설명할 필요없죠?**

![img](https://postfiles.pstatic.net/MjAyMDExMDlfODgg/MDAxNjA0OTAxNjcxMzYz.IJOLR0lZ-qJLglmWcDe1Nv-AZGlxtYz3uHFh9T1-4A8g.oukeGcWyzZkC--Hqfb9nAMPtkxj-XfkMG3IybN5jzz0g.PNG.ks2414e/20201109144746.png?type=w773)

**그리고 기존에 json보내던 곳에서** 

![img](https://postfiles.pstatic.net/MjAyMDExMDlfNDIg/MDAxNjA0OTAxNjcxMzkw.Ne3nzAaQF40z4ee2MDagbIvmETLDN5azRV2CaX2z2Ecg.sAhKb_Ltynd_2qw_cEzJ8xvwdgexZSFC-D_9xu0LWrsg.PNG.ks2414e/20201109144836.png?type=w773)

**이제 member라는 테이블을 호출해서 rows라는 값에 저장해서 보내면 되는데용,**

**그러면 대부분 여기서 쓸데없는 고민을 하면서 점점 고민에 빠집니다.**

**db값을 어떻게 불러오지?**

**db값이 어떻게 불러와지는지 한 번 출력을 해보세요.**

![img](https://postfiles.pstatic.net/MjAyMDExMDlfNjAg/MDAxNjA0OTAyMjU1MzM3.D6ZPOx2ofqSquiC6VrAGX-6K9ql6Qx3LYkDUy3yQ3s8g.xzyR1jPl5gqMxE15-ahKORc-P8dk6QCo2ZbuNLcoO9Mg.PNG.ks2414e/20201109150944.png?type=w773)

**이런식으로 와집니다. 즉 json이랑 같은 형태입니다.**

****

**그러면 쉽게 생각하면 json을 보내는 건데, 이미 프론트엔드에서는**

**json을 받는 형식으로 코드를 짰죠?**

****

**그러면 이제 프론트엔드로 가면**

![img](https://postfiles.pstatic.net/MjAyMDExMDlfODYg/MDAxNjA0OTAxNjcxNDM3.cppajCbTNf7H6Lsa2Mx974wQ0B0PtGnRXKxu3lJm3YUg.ZMVc7t8UtiwUI0RQoTdk2MlxZsxFk1Q38rMCPhm9Imgg.PNG.ks2414e/20201109145530.png?type=w773)

**이제 이렇게 테이블에 저장된 값이 출력되는 걸 확인할 수 있습니다.**

****

![img](https://postfiles.pstatic.net/MjAyMDExMDlfMjgz/MDAxNjA0OTAyMzgzMTI5.sg8OA8DYO5liN17VPD4bQzDYtHGZWmsDeqx63ctdCn0g.nm2HkBnZ_UIg9pTCrosmOUTZP2m3qYZBy7lNJpGif50g.PNG.ks2414e/20201109151253.png?type=w773)

**그리고 당연히 db값을 추가하면**

**프론트엔드에도 값이 추가되는 걸 확인할 수 있습니다.**



***\*[출처]\** [[알고리즘\] 백엔드에 db불러오기 및 프론트 전송원리](https://blog.naver.com/ks2414e/222139609146) | \**작성자\** [배고프면개발하는사람](https://blog.naver.com/ks2414e)**