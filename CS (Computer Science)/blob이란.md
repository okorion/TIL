## 🃏 blob이란?

### blob이란 무엇일까?

어디서 처음 blob을 보셨나요? 저는 같이 프로젝트를 하던 팀원이 사진을 저장하는데 사용한다고 해서 처음 보았습니다. 그 전까지 파일은 프로젝트의 한 폴더에 따로 저장하고 그 주소를 DB에 저장한다고만 생각하고 있었는데 하나로 저장하니 아무래도 관리할 부분이 적어지니 훨씬 편하더군요. 그 이후 저는 blob이 단순히 사진을 저장하는 자료형이라고 생각해버렸습니다. 하지만 최근 프로젝트를 하면서 훨씬 다양하게 활용될 수 있다는 것을 알게 되었습니다. 이 글에서는 제가 파악한 한도 내에서 blob를 소개하고자 합니다.

> 어떻게 읽을까?

blob은 어떻게 읽을까요? 저는 처음에는 '블롭'이라고 읽었습니다. 실제로 '블랍' 또는 '블롭'이라고 읽히는 경우도 많은 것 같습니다. 그런데 이게 blob 뿐 아니라 clob 등도 있다고 합니다. 그래서 '비랍', '시랍'처럼 읽는다고도 합니다. 아마 정확하게 읽는 법까지는 지정되지 않은 것 같으니 의미가 통하는 한도 내에서 자유롭게 쓰면 되지 않을까 합니다.

> 어디에 쓸까?

blob은 Binary Large Object의 약자입니다. 이름에서 바이너리 형태로 큰 객체를 저장할 것이라는 것을 추측할 수 있습니다. 여기서 이 큰 객체라는 것은 주로 이미지, 비디오, 사운드 등과 같은 멀티미디어 객체들을 주로 가리킵니다.

> 어떻게 저장할까?

blob의 경우 4GB의 이진 데이터를 저장할 수 있다고 합니다. 하지만 이건 DB에 직접 저장하는 것이 아니라 DB에는 Large Object의 위치 포인터만 저장하게 됩니다. 저는 DB성능이 좋아져서 대용량의 데이터도 그냥 막 넣을 수 있게 된 줄 았었더니 그건 아니군요.

> javascript에서 어떻게 사용할까?

```
var blob = new Blob([typedArray], {type: 'application/octet-binary'});

var audioBlob = new Blob([dataview], { type: type });
```



위와 같이 배열과 타입을 넣어서 객체를 생성합니다.

```
var url = URL.createObjectURL(blob);

var url = URL.createObjectURL(audioBlob);
```



위와 같은 형태로 URL을 생성할 수 있는데 이 URL을 <a></a>(앵커) 태그에 연결시키면 다운로드를 받을 수 있습니다. 다운로드라고는 하지만 서버에서 직접 다운로드를 받는 것이 아니라 브라우저 상에 저장되어 있는 blob파일을 다운로드 받게 됩니다.

```
var reader = new FileReader();

reader.readAsArrayBuffer(blob);
```



blob파일은 FileReader를 통해서 읽을 수 있습니다.

> DB에서 어떻게 사용할까?

DB에 blob 데이터 형은 이렇게 쓸 수 있습니다. (출처: [디딤돌](http://stepping.tistory.com/30))

```
String query = "UPDATE TABLE SET BLOB_DATA = EMPTY_BLOB()";
stmt.executeUpdate(query);
if(rs.next()){
    BLOB blob = null;
    BufferedOutputStream out = null;
    BufferedInputStream in = null;
    byte[] nuf = null;
    int byteRead = 0;

    blob = ((OracleResultSet)rs).getBLOB(1);
    out = new BufferedOutputStream(blob.getBinaryOutputStream());
    in = new BufferedInputStream(new StringBufferInputStream(str));
    int nFileSize = (int)str.length();
    buf = new byte[nFileSize];

    while((bytesRead = in.read(buf)) != -1){
        out.write(buf, 0, bytesRead);
    }
    
    in.close();
    out.close();
}

dbconn.commit();
dbConn.setAutocommit(true); 
```



그리고 다음처럼 DB에서 blob 데이터를 읽을 수 있습니다.

```
//SELECT
String query = "SELECT CLOB_DATA FROM TABLE WHERE~";
stmt = dbConn.createStatement();
rs = stmt.executeQuery(query);
if(rs.next()){
    BLOB blob = ((OracleResultSet)rs).getBLOB(1);
    BufferedInputStream in = new BufferedInputStream(blob.getBinaryStream());
    int nFileSize = (int)blob.length();
    byte[] buf = new byte[nFileSize];
    int nReadSize = in.read(buf, 0, nFileSize);
    in.close();
    
    //contents -> BLOB데이터가 저장될 String
    String contents = new String(buf);
```



blob 형식을 활용해서 좋은 미디어 자료를 제공하는 서비스 만들기에 도전해보면 어떨까요? :)

<br>

<br>

#### 참고링크: [blob이란 무엇일까? : 네이버 블로그 (naver.com)](https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=magnking&logNo=220950061851)

<br>