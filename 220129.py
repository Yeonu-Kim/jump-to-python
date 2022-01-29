#파일 생성
>>> f=open("C:\doit\파이썬.txt", 'w')
>>> f.close()

#파일에 출력값 넣기 (쓰기 모드)
>>> f=open('C:\doit\파이썬.txt','w')
>>> for i in range(1,10):
...     s='%d번째 줄\n' %i
...     f.write(s)
... f.close()
  File "<stdin>", line 4
    f.close()
    ^
SyntaxError: invalid syntax
#for문 안에 f.close를 넣어서 오류 발생

>>> f=open('C:\doit\파이썬.txr','w')
>>> for i in range(1,11):
...     s='%d번째 줄 입니다.' %i
...     f.write(s)
...
10
10
10
10
10
10
10
10
10
11
>>> f.close
<built-in method close of _io.TextIOWrapper object at 0x000001A0D885A810>
#괄호 어디감?

>>> f=open('C:\doit\파이썬.txt','w')
>>> for i in range(1,11):
...     s='%d번째 줄입니다.' %i
...     f.write(s)
...
9
9
9
9
9
9
9
9
9
10
>>> f.close()
#s='%d번째 줄입니다.' %i -> 엔터 안 쳐서 첫번째 줄에 다 써짐.

>>> f=open('C:\doit\파이썬.txt','w')
>>> for i in range(1,11):
...     s='%d번째 줄입니다. \n' %i
...     f.write(s)
...
11
11
11
11
11
11
11
11
11
12
>>> f.close()

#외부 파일 읽기-readline
#한 줄만 읽음
>>> f=open('C:\doit\파이썬.txt','r')
>>> l=f.readline()
>>> print(l)
1번째 줄입니다.

>>> f.close()

#readline으로 전체 읽기
>>> f=open('C:\doit\파이썬.txt','r')
>>> while True:
...     l=f.readline()
...     if not l :break
...     print(l)
...
1번째 줄입니다.

2번째 줄입니다.

3번째 줄입니다.

4번째 줄입니다.

5번째 줄입니다.

6번째 줄입니다.

7번째 줄입니다.

8번째 줄입니다.

9번째 줄입니다.

10번째 줄입니다.

#readlines로 파일 읽기
>>> f.close()
>>>
>>> f=open('C:\doit\파이썬.txt','r')
>>> ls=f.readlines()
>>> print(ls)
['1번째 줄입니다. \n', '2번째 줄입니다. \n', '3번째 줄입니다. \n', '4번째 줄입니다. \n', '5번째 줄입니다. \n', '6번째 줄입니다. \n', '7번째 줄입니다. \n', '8번째 줄입니다. \n', '9번째 줄입니다. \n', '10번째 줄입니다. \n']
#모든 줄을 리스트로 변환
>>> for lin ls:
  File "<stdin>", line 1
    for lin ls:
              ^
SyntaxError: invalid syntax
#띄어쓰기 유의

>>> for l in ls:
...     print(l)
...
1번째 줄입니다.

2번째 줄입니다.

3번째 줄입니다.

4번째 줄입니다.

5번째 줄입니다.

6번째 줄입니다.

7번째 줄입니다.

8번째 줄입니다.

9번째 줄입니다.

10번째 줄입니다.

>>> f.close()

#read함수로 파일 읽기
>>> f=open('C:\doit\파이썬.txt','r')
>>> d=f.read()
>>> print(d)
1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
>>> f.close()
#가장 간편한 방법

#원해 있던 파일에 데이터 추가하기
>>> f=open('C:\doit\파이썬.txt','a')
>>> for i in range(11,21):
...     d='%d번째 줄입니다.' %i
...
#엔터 어디감?

>>> for i in range(11,21):
...     d='%d번째 줄입니다.\n' %i
...     print(d)
...
11번째 줄입니다.

12번째 줄입니다.

13번째 줄입니다.

14번째 줄입니다.

15번째 줄입니다.

16번째 줄입니다.

17번째 줄입니다.

18번째 줄입니다.

19번째 줄입니다.

20번째 줄입니다.
#print말고 write 함수를 사용해야 파일 안에 들어감. print는 내가 보는 모니터에 띄우는 것

>>> for i in range(11,21):
...     d='%d번째 줄입니다.\n' %i
...     f.write(d)
...
11
11
11
11
11
11
11
11
11
11
>>> f.close()

#f.close 쓰지 않고 자동으로 닫기 -> with문 활용
#f를 빠져나가는 순간 자동으로 닫힘.
>>> with open('파이썬.txt','w') as f:
...     f.write('안녕하세요.')
...
6
>>> with open('C:\doit\파이썬.txt','w') as f:
...     f.write('Hello World')
...
11

#4장 연습문제
>>> #연습문제 1번
>>> def odd(number):
...     if number%2==1:
...             return(True)
...     else:
...             return(False)
...
>>> odd(7)
True
>>> odd(4)
False

>>> #연습문제 2번
>>> def avg(*data):
...     result=o
#o뭐임? 0으로 바꿔야 함.
...     for i in data:
...             result=result+i
...     reutrn (result/len(data))
...
>>> avg(1,2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 2, in avg
NameError: name 'o' is not defined

>>> def avg(*data):
...     result=0
...     for i in data:
...             result +=i
#result=result+i와 동일한 뜻
...     return (result/len(data))
...
>>> avg(1,2)
1.5
>>> avg(1,2,3,4,5)
3.0

>>> #연습문제 3번
>>> i1= input('첫번째 숫자를 입력하세요.:')
첫번째 숫자를 입력하세요.:
>>> i2= input('두번째 숫자를 입력하세요.:')
두번째 숫자를 입력하세요.:
>>> total=i1+i2
>>> print('두 수의 합은 %d입니다.' %total)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: %d format: a real number is required, not str
#input은 문자열을 돌려줌. -> 정수로 변환
#int('문자열')를 치면 모든 문자열이 정수로 변환

>>> i1=input('첫번째 숫자를 입력하세요.:')
첫번째 숫자를 입력하세요.:3
>>> i2=input('두번째 숫자를 입력하세요.:')
두번째 숫자를 입력하세요.:6
>>> int()
0
#int()는 걍 임. 아무 의미 없음. 문자열도 그냥 그대로 남아있음.
#당시에 int()만 치면 모든 문자열이 자동으로 바뀌는 줄로 알고 있었음.
>>> total=i1+i2
>>> print('두 수의 합은 %d입니다.' %total)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: %d format: a real number is required, not str

#최종본
>>> i1=int(input('첫번째 숫자를 입력하세요.:'))
첫번째 숫자를 입력하세요.:3
>>> i2=int(input('두번째 숫자를 입력하세요.:'))
두번째 숫자를 입력하세요.:6
>>> total=i1+i2
>>> print('두 수의 합은 %d입니다.' %total)
두 수의 합은 9입니다.

>>> #연습문제 4
>>> #3번만 띄어쓰기가 되어서 나옴.
>>> print('you''need''python')
youneedpython
>>> print('you'+'need'+'python')
youneedpython
>>> print('you,', 'need', 'python')
you, need python
>>> print(''.join(['you','need','python']))
youneedpython

>>> #연습문제 5
>>> f1=open("C:\doit\테스트.txt", 'w')
>>> f1.write('Life is too short')
17
>>> f1.close()
>>> f2=open("C:\doit\테스트.txt", 'r')
>>> print(f2.read())
Life is too short
>>>
>>> f2.close()

>>> #연습문제6
>>> user=input('저장할 내용을 입력하세요.')
저장할 내용을 입력하세요.
>>> user=input('저장할 내용을 입력하세요:')
저장할 내용을 입력하세요:안녕하세요!
>>> f=open('C:\doit\파이썬.txt', 'a')
>>> f.write(user)
6
>>> f.write(\n)
  File "<stdin>", line 1
    f.write(\n)
             ^
SyntaxError: unexpected character after line continuation character
#\n도 문자열처럼 따옴표로 묶어야 함.

>>> f.write('\n')
1
>>> f.close()


>>> #연습문제 7번
>>> f=open('test.txt', 'r')
>>> body=read()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'read' is not defined
#read 앞에 무엇을 읽을 것인지는 꼭 적어야 함. ex)f.read()
>>> body=f.read()
>>> f,close()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'close' is not defined
>>> f.close
<built-in method close of _io.TextIOWrapper object at 0x0000022AE189AB50>
>>> f.close()
#f.close인데 f,close(), f.close등 별의 별 짓을 하느라 오류 발생.
>>> body=body.replace('java', 'python')
>>> f.write(body)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
#먼저 f함수를 열어줘야 함.
>>> f=open('test.txt', 'w')
>>> f.write(body)
0
>>> f.close()
