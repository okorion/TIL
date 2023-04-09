**0.**   **PyCharm에서 디버깅을 할 필요성**

간혹 코딩을 하다가 보면 한 줄씩 차례대로 실행시키고 싶을 때가 있다. 이를 *Stepping*이라고 하는데, PyCharm에서는 디버깅 툴을 통해 단계별로 코드를 실행시킬 수 있다.

해당 코드에서 더 깊숙이 들어가고 싶을 때도 있고, 관심이 별로 없는 코드라서 빠르게 훑고 싶을 때도 있다. 이렇게 상황에 따라 다른 조작을 지원하고 있으므로 프로그래머가 필요에 따라 선택할 수 있어 매우 편리하다.

 <br>

**1.**   **버튼 및 의미**

A.[![img](https://1.bp.blogspot.com/-kxlUj5G9LmA/X_RIYNvhkYI/AAAAAAAATMM/VZ_0XaqWNNYpjrq4l73zPEpTOCqC33TkQCLcBGAsYHQ/s0/image2.png)](https://1.bp.blogspot.com/-kxlUj5G9LmA/X_RIYNvhkYI/AAAAAAAATMM/VZ_0XaqWNNYpjrq4l73zPEpTOCqC33TkQCLcBGAsYHQ/s28/image2.png) **Step Over (F8)**

Step Over는 코드의 현재 라인에서 그 다음 라인으로 이동한다. 하이라이트 표시된 라인이 메서드를 호출하고 있다 하더라도 다음 줄로 넘어가게 된다. 호출되고 있는 메서드는 내부적으로 실행된다.

다만, 내부적으로 실행되는 메서드라 하더라도 해당 메서드에 breakpoints가 존재할 경우, 디버거는 해당 위치에서 정지하게 된다. 메서드에 breakpoints가 있더라도 강제로 skip하고 싶은 경우엔 Force Step Over를 사용하면 된다.

 <br>

**B.**[![img](https://1.bp.blogspot.com/-GNHbwyPNA6o/X_RIYGREf2I/AAAAAAAATMQ/5_P4Q95E_V4lSrj1hhiAoOpJE-aQLTTqACLcBGAsYHQ/s0/image3.png)](https://1.bp.blogspot.com/-GNHbwyPNA6o/X_RIYGREf2I/AAAAAAAATMQ/5_P4Q95E_V4lSrj1hhiAoOpJE-aQLTTqACLcBGAsYHQ/s25/image3.png) **Step Into (F7)**

Step Into는 메서드 내에서 무슨 일이 일어나고 있는지를 보여준다. 호출한 메서드가 올바른 결과를 반환하고 있는지 확신할 수 없을 때에 이 기능을 사용해서 메서드 내부를 관찰할 수 있다.

만약 여러 개의 메서드가 한 번에 호출되고 있다면 PyCharm은 당신에게 어느 메서드로 들어갈 것인지를 물어보게 된다. 이 기능을 Smart Step Into라고 부른다고 한다. Smart Step Into는 메서드 다중호출 시에 기본적으로 사용하도록 되어있지만, 이 기능을 끄고 싶다면 Settings/Preferences – Build, Execution, Deployment – Debugger – Stepping에 들어가서 Always do smart step into를 체크 해제한다. 이 설정창에서는 Step Into 시에 skip할 목록들도 원하는 대로 관리할 수 있다. 또한 라이브러리 스크립트는 skip하고 싶을 땐 Do not step into library scripts에 체크하면 된다.

 <br>

**C.**[![img](https://1.bp.blogspot.com/-V6Tu0fmaNcs/X_RIZAxiAyI/AAAAAAAATMU/Ze6Q5OGUZxAGP4NLFnFibJRaC1FGYYVLgCLcBGAsYHQ/s0/image4.png)](https://1.bp.blogspot.com/-V6Tu0fmaNcs/X_RIZAxiAyI/AAAAAAAATMU/Ze6Q5OGUZxAGP4NLFnFibJRaC1FGYYVLgCLcBGAsYHQ/s26/image4.png) **Step Into My Code (Alt+Shift+F7)**

나의 코드에 집중하고 싶을 때, 라이브러리 클래스로는 stepping하지 않고 Step Into를 수행하는 기능이다.

 <br>

**D.**[![img](https://1.bp.blogspot.com/-PK-yC5Xg9SE/X_RIZX7zD8I/AAAAAAAATMY/GM0V-QN-iA4Jthp5-x66ukoSNeT6OYZRACLcBGAsYHQ/s0/image5.png)](https://1.bp.blogspot.com/-PK-yC5Xg9SE/X_RIZX7zD8I/AAAAAAAATMY/GM0V-QN-iA4Jthp5-x66ukoSNeT6OYZRACLcBGAsYHQ/s26/image5.png) **Force Step Into (Alt+Shift+F7)**

일반적인 Step Into에서는 skip되어야 했을 메서드에 강제로 진입한다.

 <br>

**E.** [![img](https://1.bp.blogspot.com/-W7E-0SMl6dM/X_RIZqhOn-I/AAAAAAAATMc/Kpw-3tTt_C04cfgkQ4KX9BVtFAptdLXggCLcBGAsYHQ/s0/image6.png)](https://1.bp.blogspot.com/-W7E-0SMl6dM/X_RIZqhOn-I/AAAAAAAATMc/Kpw-3tTt_C04cfgkQ4KX9BVtFAptdLXggCLcBGAsYHQ/s26/image6.png) **Step Out (Shift+F8)**

메서드를 호출하던 바깥 코드로 빠져나온다.

 <br>

**F.** [![img](https://1.bp.blogspot.com/-VtFW8dDKoUs/X_RIZwMNpWI/AAAAAAAATMg/awkHqVS6ktM7NLZdnN8LF5inwAWb452hACLcBGAsYHQ/s0/image7.png)](https://1.bp.blogspot.com/-VtFW8dDKoUs/X_RIZwMNpWI/AAAAAAAATMg/awkHqVS6ktM7NLZdnN8LF5inwAWb452hACLcBGAsYHQ/s26/image7.png) **Run to Cursor (Ctrl+Alt+F9)**

커서 깜빡이가 위치한 곳까지 실행을 진행시킨다. 중간에 breakpoints를 만나더라도 모두 무시된다.

<br>

<br>

#### 참고링크: [익명의 블로그: PyCharm 디버거 기능(Step Over, Step Into, Step Into My Code) (pertinency.blogspot.com)](https://pertinency.blogspot.com/2021/01/pycharm-step-over-step-into-step-into.html)

<br>

