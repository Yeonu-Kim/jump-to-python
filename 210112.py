>>> a=[1,2,3]
>>> id(a)
1523078148160

#변수 이름=값
#리스트가 메모리에 자동 저장 -> a는 메모리 주소 저장

>>> a=b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
#항상 변수 이름이 앞에 나와야 함.

#id 함수로 메모리 주소 찾기
>>> b=a
>>> id(b)
1523078148160
>>> a is b
True

#a를 변화시키면 b도 자동으로 변화됨.
>>> a
[2, 3]
>>> b
[2, 3]

#메모리 주소는 바꾸고 값만 가지고 오고 싶을 때 -> 절대 등호 사용하면 안됨.(등호는 주소까지 같다는 거니까)
  #a 처음부터 끝까지 슬라이싱
>>> b=a[:]
>>> id(a)
1523078148160
>>> id(b)
1523078147584

  #copy 함수 사용하기
>>> from copy import copy
>>> b=copy(a)
>>> id(b)
1523078547136

#변수 설정하기
  #튜플 자료형 (괄호 생략 가능)
>>> a,b=1,2
>>> a
1
>>> b
2
>>>
>>> a,b=(3,4)
>>> a
3
>>> b
4

  #등호 사용하기
>>> a=b="python"
>>> a
'python'
>>> b
'python'
>>> a is b
True

#변수 위치 바꾸기
>>> a,b=1,10
>>> a,b=b,a
>>> a
10
>>> b
1

#Q1
>>> (80+75+55)/3
70.0
  #각 영역을 변수로 지정하면 나중에 점수가 변화했을 때도 쉽게 평균을 구할 수 있다.
>>> a=80
>>> b=75
>>> c=55
>>> A=(a+b+c)/3
>>> A
70.0

#Q2
>>> a=13
>>> if a//2=1:
  File "<stdin>", line 1
    if a//2=1:
       ^^^^
SyntaxError: cannot assign to expression here. Maybe you meant '==' instead of '='?
  #'같다'는 의미를 사용하고 싶다면 ==을 사용해야 함. (=은 변수 지정과 같은 상황에서 사용)
>>> if 13 % 2==1:
...     print("odd")
... else:
...     print("even")
...
odd
  #이렇게 코드를 짜면 13 대신 다른 숫자가 들어와도 홀수, 짝수를 분간할 수 있어서 좋다.
  
#Q3
>>> pin="881120-1068234"
>>> yyyymmdd="19"+pin[:6]
>>> num=pin[7:]
>>> print(yyyymmdd)
19881120
>>> print(num)
1068234

#Q4
>>> if pin.index(7)==1:
...     print("male")
... else:
...     print('female')
...
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: must be str, not int
  #변수 이름 자리에 함수를 작성해서 에러가 발생한 듯
>>> if pin[7]==1:
...     print(pin[7])
... else:
...
  File "<stdin>", line 4

    ^
IndentationError: expected an indented block after 'else' statement on line 3
  #else 뒤에 아무것도 안 썼더니 에러발생. 뭐라도 써야 하나봄. 다음장에서 자세히 배운다고 한다.
>>> if pin[7]==1:
...     print(pin[7])
... else:
...     print("female")
...
female
  #??? 1이 맞는데 female이 출력되었다. 왜 이렇게 됐을까?-> 1이 아니라 '1'로 설정해야 하나?
>>> if pin[7]=='1':
...     print('male')
... else:
...     print('female')
...
male
  #숫자형과 문자형 혼동을 조심하자
#모범 답안 대로도 써봄
>>> print(pin[7])
1

#Q5
>>> a="a:b:c:d"
>>> b=a.replace(:,#)
  File "<stdin>", line 1
    b=a.replace(:,#)
                ^
SyntaxError: invalid syntax
  #:,#도 문자형으로 취급해야 함. (당현이 숫자형에 해당하지 않기 때문)
>>> b=a.replace(':','#')
>>> print(b)
a#b#c#d

#Q6
>>> a=[1,3,5,4,2]
>>> a.sort()
>>> a.reverse()
>>> print(a)
[5, 4, 3, 2, 1]

#Q7
>>> a=['Life', 'is', 'too', 'short']
>>> result=' '.join(a)
>>> print(result)
Life is too short

#Q8
>>> a=(1,2,3)
>>> a=a+4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "int") to tuple
  #튜플자료형끼리 더할 수 있으므로 숫자형 대신 튜플을 작성해야 한다.
>>> a=a+(4,)
>>> a
(1, 2, 3, 4)


#Q9
>>> a=dict()
>>> a
{}
>>> a[[1]]='python'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
#3번, 리스트 자료형은 key 값으로 사용될 수 없음.

#Q10
  #문제 제대로 안 읽고 그냥 결과만 출력한 것
>>> a={'A':90, 'B':80, 'C':70}
>>> result=a.get('B')
>>> print(result)
80
  #딕셔너리에서도 pop 함수를 사용할 수 있다
>>> result=a.pop('B')
>>> print(a)
{'A': 90, 'C': 70}
>>> print(result)
80

#Q11
>>> a=[1,1,1,2,2,3,3,3,4,4,5]
>>> aSet=set(a)
>>> b=list(aSet)
>>> print(b)
[1, 2, 3, 4, 5]


#Q12
>>> a=b=[1,2,3]
>>> a[1]=4
>>> print(b)
[1, 4, 3]
