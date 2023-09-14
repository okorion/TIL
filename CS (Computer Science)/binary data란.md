## 🔌 binary data란?

## binary data는 무엇인가?

- 엄밀하게 따지면, 모든 data 혹은 파일은 binary data입니다.
  - 모든 텍스트파일은 binary file,
  - 그러나, 모든 binary file이 텍스트 파일인 것은 아님
- 아무튼, 그냥 binary로 읽고 쓰는 것을 간단하게 정리하였습니다.
- 텍스트의 경우는 상관없지만, 이미지와 같은 다른 파일들의 경우는 가급적 binary로 읽고 쓰는 것을 추천합니다.

## read and write binary

- 일단은 늘 하는 것처럼 그냥 텍스트를 간단하게 파일에 써보겠습니다.
- 아래처럼 보통 텍스트 파일은 편하게 읽고 쓸 수 있습니다.

```
msg = """내가 임마 느그 스장이랑 모굑탕도 가고"""

f = open('test_text.txt', 'w')
f.write(msg)
f.close()

print('-'*20)
f = open("test_text.txt", 'r')
print("read text:\n{}".format(f.read()))
f.close()
print('-'*20)
--------------------
read text:
내가 임마 느그 스장이랑 모굑탕도 가고
--------------------
```

- 이제 텍스트 파일을 binary로 읽고 써보겠습니다.
- 아래에서 보는 것처럼 binary로 읽고 쓰는데, `string`을 binary로 써야 하기 때문에 `encode`하여 저장합니다.
- file을 binary로 읽어서 출력해보면, 텍스트가 아니라 이상한 숫자들로 죽 나열되어 있는 것을 알 수 있습니다.
- binary data를 `utf-8`로 디코딩하여 출력해보면 제대로 나오는 것을 알 수 있습니다.

```
msg = """내가 임마 느그 스장이랑 모굑탕도 가고"""

f = open("test_text.bin", 'wb')
## text를 그대로 쓸 수 없기 때문에 binary로 encoding하여 저장 
f.write(msg.encode()), f.close()

print('-'*20)
f = open('test_text.bin', 'rb')
msg_bin = f.read()
print("read binary text:\n{}".format(msg_bin))
f.close()

print('-'*20)
print("decoded binary text:\n{}".format(msg_bin.decode('utf-8')))
print('-'*20)
--------------------
read binary text:
b'\xeb\x82\xb4\xea\xb0\x80 \xec\x9e\x84\xeb\xa7\x88 \xeb\x8a\x90\xea\xb7\xb8 \xec\x8a\xa4\xec\x9e\xa5\xec\x9d\xb4\xeb\x9e\x91 \xeb\xaa\xa8\xea\xb5\x91\xed\x83\x95\xeb\x8f\x84 \xea\xb0\x80\xea\xb3\xa0'
--------------------
decoded binary text:
내가 임마 느그 스장이랑 모굑탕도 가고
--------------------
```

## 그림 파일은 무조건 binary read/write

- 우리가 만약 그림 파일을 저장해야 할때는 `string`으로 저장하는 것이 아니라 `bytes`로 저장해야 합니다.
- 웹에서 이미지를 긁어와서, 해당 이미지를 로컬에 저장하려고 합니다. 이때 반드시 `binary`로 저장해야 합니다.

```
import requests
import matplotlib.pyplot as plt

url = "https://amueller.github.io/word_cloud/_images/sphx_glr_colored_003.png"
response = requests.get(url)
print("binary file sample: {}".format(response.content[:20]))

## binary file을 만들어줍니다. 
f = open("write_bin_img.png", 'wb')
f.write(response.content), f.close()

## 저장된 binary file을 다시 이미지로 읽어서, 잘 저장되어 있는지를 확인합니다. 
img_np_array = plt.imread('write_bin_img.png')
f = plt.figure()
plt.imshow(img_np_array)
plt.savefig("../../assets/images/markdown_img/180709_bin_img.svg")
binary file sample: b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x02\x80'
```

![binary_img](https://frhyme.github.io/assets/images/markdown_img/180709_bin_img.svg)

- 만약 아래처럼 그냥 string으로 저장할 경우 오류가 발생하는 것을 알 수 있습니다.

```
import requests
import matplotlib.pyplot as plt

url = "https://amueller.github.io/word_cloud/_images/sphx_glr_colored_003.png"
response = requests.get(url)
print("binary file sample: {}".format(response.content[:20]))

## binary file을 만들어줍니다. 
f = open("write_bin_img.png", 'w')
f.write(str(response.content)), f.close()

## 저장된 binary file을 다시 이미지로 읽어서, 잘 저장되어 있는지를 확인합니다. 
img_np_array = plt.imread('write_bin_img.png')
f = plt.figure()
plt.imshow(img_np_array)
plt.savefig("../../assets/images/markdown_img/180709_bin_img.svg")
binary file sample: b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x02\x80'
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-75-eda015040b05> in <module>()
     11 
     12 ## 저장된 binary file을 다시 이미지로 읽어서, 잘 저장되어 있는지를 확인합니다.
---> 13 img_np_array = plt.imread('write_bin_img.png')
     14 f = plt.figure()
     15 plt.imshow(img_np_array)

~/anaconda3/lib/python3.6/site-packages/matplotlib/pyplot.py in imread(*args, **kwargs)
   2379 @docstring.copy_dedent(_imread)
   2380 def imread(*args, **kwargs):
-> 2381     return _imread(*args, **kwargs)
   2382 
   2383 

~/anaconda3/lib/python3.6/site-packages/matplotlib/image.py in imread(fname, format)
   1374         else:
   1375             with open(fname, 'rb') as fd:
-> 1376                 return handler(fd)
   1377     else:
   1378         return handler(fname)

ValueError: invalid PNG header
```

## wrap-up

- 정리하자면, 기본적으로 컴퓨터의 모든 데이터는 binary입니다. 다만, 이를 필요에 따라서 text로 변형해서 처리하는 것이죠. 보통 파일 스트림에는 그 앞에 이 아이가 text인지, binary인지를 표시해주는 부분이 있습니다. 이를 통해 컴퓨터는 얘가 binary인지 아닌지를 파악하고 그 다음에 읽거나 출력하거나 하는 것을 진행하죠.
- 우리가 흔히 쓰는 텍스트들의 경우는 binary일 수도 있고, text일 수도 양 쪽 모두 저장 하는 것이 가능하지만, image는 기본적으로 무조건 binary입니다.
- `base64`를 이용하면 뭔가 좀 더 재밌는 것들이 가능할 것 같기도 한데, 현재로서는 그냥 넘어가는 것이 더 좋을 것 같아서 일단 무시하고 넘어갑니다.



<br>

<br>

#### 참고링크: [binary data란 무엇인가? : frhyme.code](https://frhyme.github.io/python/binary_data/)

<br>