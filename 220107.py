# %d는 정수, %s는 문자열(숫자 기입시 '2' 꼴로 기록. 이때 '2'는 숫자 기능을 하지 못함.)
>>> 'I ate %d orange.' %3
'I ate 3 orange.'
>>> 'I ate %s orange.' %'three'
'I ate three orange.'

# 변수 선언 먼저 해야함.
>>> 'I ate %d oranges.' %number
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'number' is not defined

>>> number=3
>>> 'I ate %d oranges.' %number
'I ate 3 oranges.'

# 변수 2개 이상일 때
>>> number=3
>>> day=5
>>> 'I ate %d oranges for %d days.' %(number, day)
'I ate 3 oranges for 5 days.'

#공백 및 정렬. 양수는 왼쪽 배치, 음수는 오른쪽 배치. 사실 잘 안쓰긴 함. 정렬은 보통 포맷 함수 사용.
>>> '%10s' %'Hello!'
'    Hello!'
>>> '%-10s' %'Hello!'
'Hello!    '

#소수점 표시. '.'앞은 공백, '.'은 소수점, 4는 자릿수. 반올림되어 표시됨.
>>> '%0.4f' %3.141592
'3.1416'
>>> '%.4f' %3.141592
'3.1416'
  #%.4f==%0.4f
>>> '%10.3f' %3.141592
'     3.142'

# 포맷 함수의 활용
>>> 'I ate {0} oranges.'
'I ate {0} oranges.'
>>> 'I ate {0} oranges.'.format(5)
'I ate 5 oranges.'
>>> number=5
>>> 'I ate {0} oranges.'.format(number)
'I ate 5 oranges.'
>>> 'I ate {number} oranges.'.format(number=5)
'I ate 5 oranges.'
>>> 'I ate {0} oranges for {1}.'.format('five', 'three')
'I ate five oranges for three.'

#포맷 함수로 공백 및 정렬 표현
>>> '{0:=<10}'.format()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: Replacement index 0 out of range for positional args tuple
  #.format()에서 괄호 안에는 {0}에 들어갈 내용 입력
>>> '{0:=<12}'.format('Hello!')
'Hello!======'
>>> '{0:=^12}'.format('Hello!')
'===Hello!==='
>>> '{0:=<12}'.format('Hello!')
'Hello!======'
>>> '{0:=>12}'.format('Hello!')
'======Hello!'

#포맷 함수로 소수점 표현
>>> '{0:.4f}'.format(3.141592)
'3.1416'

#f 문자열 포매팅
>>> f'{"hi":<12}'
'hi  '

>>> y=3.141592
>>> f'{y:.4f}'
'3.1416'

#문자열 함수
  # 문자 개수 세기(count)
>>> a="refrigerator"
>>> a.count('r')
4

  # 문자 위치 찾기(find, index)
>>> a="Do you want dome drink?"
>>> a.find('w')
7
>>> a.find('o')
1
    #문자가 중복해서 등장할때는 제일 앞 위치를 출력함.
>>> a.find('o')
1
>>> a.find('z')
-1
    #find 는 '-1'을 출력하여 없음을 표현. index는 ValueError발생
>>> a.index('w')
7
>>> a.index('o')
1
>>> a.index('z')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found

  #끼워넣기(join)
>>> "|".join('5678')
'5|6|7|8'
>>> "|".join(['apple', 'banana', 'grape'])
'apple|banana|grape'

  #대문자, 소문자 변환 (upper, lower)
>>> a="hello!"
>>> a.upper()
'HELLO!'
>>> a.lower()
'hello!'

  #공백 삭제(lstrip, rstrip, strip)
>>> a="I love   you.     "
>>> a.lstrip()
'I love   you.     '
    #2개 이상 등장하는 공백만 삭제하므로 가장 왼쪽에는 공백 존재하지 않음. 따라서 지워지는 공백 없음.
>>> a="    I love    you."
>>> a.strip()
'I love    you.'

  #단어 바꾸기(replace)
>>> a='Do you want some drink?'
>>> a.replace('drink', 'dishes')
'Do you want some dishes?'

  #문자열 자료형을 리스트 자료형으로 변환하기(split)
>>> a="I like pizza."
>>> a.split()
['I', 'like', 'pizza.']

#리스트 함수의 계산
>>> [a,b,c]+[d,e,f,]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'b' is not defined
  #리스트에서는 [4,] 이따구로 쓰면 안돼요.
>>> [1,2,3]+[4,5,6]
[1, 2, 3, 4, 5, 6]
>>> [1,2,3]+[3,2,1]
[1, 2, 3, 3, 2, 1]
  #중복되는 원소도 그대로 더해짐.
>>> ['a','b','c']*5
['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']

#리스트 원소 수정
>>> a=[1,2,2,4,5]
>>> a[2]=3
>>> a
[1, 2, 3, 4, 5]

#리스트 원소 삭제
>>> dela[2:]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dela' is not defined
  #del a 꼴로 작성해야함. 띄어쓰기 필수
>>> del a[2:]
>>> a
[1, 2]

#리스트 함수
  #원소 추가(append=덧붗이다)
>>> a=[1,2,3,4]
>>> a.append(5)
>>> a
[1, 2, 3, 4, 5]

  #원소 배열(sort)
>>> a=[4,2,5,1,3]
>>> a.sort()
>>> a
[1, 2, 3, 4, 5]

  #원소 뒤집기(reverse, 역순 배열 아님. 원 상태에서의 역순=transposition)
>>> a.reverse()
>>> a
[5, 4, 3, 2, 1]

  #위치 찾기(index)
>>> a.index(4)
1
>>> a.index(6)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 6 is not in list
    #없는 원소 찾으면 에러 뜸.

  #원소 삽입(insert)
>>> a.insert(5,6)
>>> a
[5, 4, 3, 2, 1, 6]

  #원소 제거(remove, del 함수는 a. 붙이지 않아도 됨.)
>>> a.remove(3)
>>> a
[5, 4, 2, 1, 6]

>>> a=[1,2,3,1,2,3]
>>> a.remove(1)
>>> a
[2, 3, 1, 2, 3]
>>> a.remove(1)
>>> a
[2, 3, 2, 3]
    #중복되는 원소 중 앞에 있는 것 하나만 제거됨.
  #원소 뽑기(pop, 뽑고 나서 삭제, pop()이면 맨 마지막 원소 추출)
>>> a.pop()
3
>>> a
[2, 3, 2]
>>> a.pop(1)
3
>>> a
[2, 2]

  #원소 개수 세기(count)
>>> a.count(2)
2

  #리스트 확장(extend, 그냥 더하기임.)
>>> a.extend([1,3,4,5,6])
>>> a
[2, 2, 1, 3, 4, 5, 6]

#튜플 자료형. ()와 ,가 특징. 원소 수정, 삭제, 생성 불가능.
>>> t1=(1,2,3,4,5)
>>> t2=(1,)
>>> t1[3]
4

#튜플 슬라이싱
>>> t1[4:]
(5,)

#튜플 계산
>>> t1+t2
(1, 2, 3, 4, 5, 1)
>>> t2*5
(1, 1, 1, 1, 1)
>>> len(t1)
5
