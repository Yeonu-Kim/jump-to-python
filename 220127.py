#함수의 구조
>>> def f(a,b):
...     return a+b
...
>>> f(3,4)
7
>>> c=f(3,4)
>>> print(c)
7

#출력값이 없는 함수
>>> def say():
...     print('hi')
...
>>> a=say()
hi
>>> print(a)
None
#a의 값이 존재하지 않음 == 출력값이 없는 거
#출력값은 return문으로 만들 수 있음. print는 걍 수행하는 거

#입력값이 없는 함수
>>> def say():
...     return 'hi'
...
>>> a=say()
>>> print(a)
hi

#def 뒤에 항상 :를 찍어야 함.
>>> def f(a,b)
  File "<stdin>", line 1
    def f(a,b)
              ^
SyntaxError: expected ':'

#매개변수 지정하여 호출
>>> def f(a,b):
...     return a+b
...
>>> f(a=4,b=7)
11
>>> f(b=7,a=6)
13
#변수 순서에 상관 없이 함수 작동

#입력값이 몇 개일지 모를 때
#*를 사용하면 함수 입력부분 처리 가능
>>> def f(*k):
...     result=0
...     for i in k:
...             result=result+i
...     return result
...
>>> f(1,2,3,4,5)
15
>>> f(range(11))
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in f
TypeError: unsupported operand type(s) for +: 'int' and 'range'
    #입력값 부분에는 range가 올 수 없나봄
    
>>> f(1,2,3,4,5,6,7,8,9,10)
55

#계산기 만들기
>>> def f(choice, *k):
...     result=0
...     if choice=='add':
...
  File "<stdin>", line 4
IndentationError: expected an indented block after 'if' statement on line 3
  #음.. 뭐가 잘못된 건지 모르겠다. result가 if 앞으로 와 있어서 오류가 났나?
  
>>> def f(choice, *k):
...     if choice=='add':
...             for i in k:
...     result=0
  File "<stdin>", line 4
    result=0
IndentationError: expected an indented block after 'for' statement on line 3
  #result가 for문 안으로 들어와야 함.
  
>>> def f(choice,*k):
...     if choice=='add':
...             result=0
...             for i in k:
...                     result=result+i
...     else:
...             result=1
...             for i in k:
...             result=result*i
  File "<stdin>", line 9
    result=result*i
    ^
IndentationError: expected an indented block after 'for' statement on line 8
  #'result=result*i'가 for문 안으로 들어와야 함.
  
>>> def f(choice,*k):
...     if choice=='add':
...             result=o
#o아니고 0임.^^
...             for i in k:
...                     result=result+i
...     else:
...             result=1
...             for i in k:
...                     result=result*i
...     return result
...
>>> f(add, 1,2,3,4,5,6,7,8,9,10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'add' is not defined
>>> f('add', 1,2,3,4,5,6,7,8,9,10)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 3, in f
NameError: name 'o' is not defined

  #완성본
>>> def f(choice,*k):
...     if choice=='add':
...             result=0
...             for i in k:
...                     result=result+i
...     else:
...             result=1
...             for i in k:
...                     result=result*i
...     return result
...
>>> f('add', 1,2,3,4,5,6,7,8,9,10)
55
>>> f('mul', 1,2,3,4,5,6,7,8,9,10)
3628800

#키워드 파라미터
>>> def f(**j):
...     print(j)
...
>>> f(a=1, b=2, c=3)
{'a': 1, 'b': 2, 'c': 3}
>>> f(name='김연우', age=21)
{'name': '김연우', 'age': 21}
#딕셔너리 자료형으로 변환해줌.

#함수 output은 항상 1개
>>> f(3,4)
(7, 12)
>>> r1, r2=f(3,4)
>>> print(r1)
7
>>> print(r2)
12

>>> def f(a,b):
...     return a+b
...     return a*b
...
>>> d=f(3,4)
>>> print(d)
7
#return이 이뤄지면 바로 함수 밖으로 나가짐.=break문
#a+b에서 return이 일어났으니까 a*b는 계산될 수 없음.

#return문의 활용
#닉네임 차단
>>> def f(i):
...     if i=='멍청이':
...             return
...     print('저는 %s입니다.' %i)
...
>>> f('귀요미')
저는 귀요미입니다.
>>> f('멍청이')
>>> d=f('ajdcjddl')
저는 ajdcjddl입니다.
>>> d=f('멍청이')
>>> print(d)
None

#매개변수 초깃값 설정
>>> def f(n,o,f=True):
...     print('저의 이름은 %s입니다.' %n)
...     print('저는 %d살 입니다.' %o)
...     if f:
...             print('여자입니다.')
...     else:
...             print('남자입니다.')
...
>>> f('김연우',21,f)
저의 이름은 김연우입니다.
저는 21살 입니다.
여자입니다.
>>> f('김연우', 21)
저의 이름은 김연우입니다.
저는 21살 입니다.
여자입니다.

#초깃값을 설정하는 매개변수는 항상 끝에 나와있어야 함.
>>> def f(n,f=True,o)
  File "<stdin>", line 1
    def f(n,f=True,o)
                   ^
SyntaxError: non-default argument follows default argument

#함수 밖 변수 vs 매개변수
#함수 안에 있는 변수는 따로 놀고 있음.-> 함수 밖 a != 함수 안 a
>>> a=1
>>> def f(a):
...     a=a*10
...
>>> f(a)
>>> print(a)
1
>>> c=f(a)
#위에서는 함수 안에 함수 밖 a를 입력함.-> 함수 안에서는 계산이 잘 되었는데, 함수 밖으로 나오지는 않은 상태
>>> print(c)
None

>>> def f(a):
...     a=a*10
...
>>> print(a)
1
>>> d=f(3)
>>> print(d)
None
#return 값이 없으니까 나오는 게 없음.

#return으로 변수 문제 해결하기
>>> def f(a):
...     a=a*10
...     return a
...
>>> a=f(a)
#함수 밖 a를 f(a)로 변경 -> 이때는 return값으로 output을 만들어서 잘 변환이 됨.
>>> print(a)
10

#global로 문제 해결하기
>>> a=1
>>> def f():
...     global a
...     a=a*10
...
>>> f()
>>> print(a)
10
#함수는 독립적일수록 유리 -> global 사용은 자제하기

#간단한 함수는 lambda로 쉽게 설정 가능
>>> add=lambda a,b: a+b
>>> r=add(3,4)
>>> print(r)
7

#사용자 입력
>>> a=input()
I love you!
>>> print(a)
I love you!

#사용자 입력창 만들기
#유저 인터페이스 같은 건가?
>>> a=input('하고 싶은 말을 적어주세요.')
하고 싶은 말을 적어주세요.I love you!
>>> print(a)
I love you!

#print의 특징 -> 출력한다.
>>> print('I''love''you''!')
Iloveyou!
>>> print('I'+'love'+'you!')
Iloveyou!
>>> print('I','love','you')
I love you
#콤마 찍으면 자동으로 띄어쓰기 해줌.

#end로 띄어쓰기 가능
>>> for i in range(10):
...     print(i, end=' ')
...
0 1 2 3 4 5 6 7 8 9 >>>
