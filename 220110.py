#딕셔너리 요소 추가
>>> a={1:"hi"}
>>> a[2]="hello"
>>> a
{1: 'hi', 2: 'hello'}

#딕셔너리 요소 삭제
>>> del a[1]
>>> a
{2: 'hello'}

#딕셔너리 value 출력 (key-> value)
>>> grade={'연우':10, '인우':99}
>>> grade['연우']
10
>>> grade['정자']
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: '정자'
  #존재하지 않는 key를 입력하면 오류 발생
  
#key는 중복될 수 없음
>>> a={1:'a', 1:'b'}
>>> a
{1: 'b'}

#key에는 리스트 자료형이 들어갈 수 없음. (불변값 사용)
>>> a={[1,2]:'a'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'

#key 값 뽑기(keys)
>>> a={'연우':10, '인우':99, '정화':50, '용희':40}
>>> a.keys()
dict_keys(['연우', '인우', '정화', '용희'])
>>> for k in a.keys():
#a.keys의 원소 k가 참이면 반복하세요
...     print(k)
...
연우
인우
정화
용희

#a.keys로 뽑은 값을 리스트 자료형처럼 사용할 수 있다는데.. 리스트 관련 함수로는 어떻게 쓰는지 모르겠음.
>>> a.reverse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'reverse'
>>> k in a.keys()
True
>>> dict_keys.reverse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dict_keys' is not defined

#a.keys의 값을 리스트 자료형으로 뽑음 (list)
>>> list(a.keys())
['연우', '인우', '정화', '용희']
  #리스트 함수로 쓰는 법은 모르겠음. b=list(a.keys())로 해보려고 했는데 실패
>>> a.reverse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'dict' object has no attribute 'reverse'
>>> dict_keys.reverse()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'dict_keys' is not defined
>>>  b=list(a.keys())
  File "<stdin>", line 1
    b=list(a.keys())
IndentationError: unexpected indent

#a의 vlaue 값 뽑기(value)
>>> a.values()
dict_values([10, 99, 50, 40])

#a의 key-value 쌍 뽑기(items)
>>> a.items()
dict_items([('연우', 10), ('인우', 99), ('정화', 50), ('용희', 40)])

#a의 모든 key-value 쌍 삭제(clear)
>>> a.clear()
>>> a
{}

#key 입력 시 value 얻기(get)
>>> a={'연우':10, '인우':99, '정화':50, '용희':4}
>>> a.get('연우')
10
>>> a.get(10)
>>> a
{'연우': 10, '인우': 99, '정화': 50, '용희': 4}
>>> a.get('정자',0)
0
>>> a.get('정자')
>>>
  #get 함수에서는 존재하지 않는 key를 입력했을 때 none이 나오는데.. 뭔가 잘못된 것 같다.

#불 자료형 설정
>>> a={'연우':10, '인우':99, '정화':50, '용희':40}
>>> '연우' in a
True
>>> '정자' in a
False
  #True와 False는 항상 첫 문자가 대문자
  
#집합 자료형 설정
>>> a=set([1,2,3])
>>> a
{1, 2, 3}
>>> a=set([refrigerator])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'refrigerator' is not defined
>>> a=set("refrigerator")
>>> a
{'t', 'a', 'i', 'r', 'o', 'e', 'f', 'g'}

#교집합(&), 합집합(|), 차집합(-)
>>> a=set([1,2,3,4,5,6])
>>> b=set([4,5,6,7,8,9])
>>> a&b
{4, 5, 6}
>>> a|b
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> a-b
{1, 2, 3}
>>> b-a
{8, 9, 7}

#교집합 함수(intersection), 합집합 함수(union), 차집합 함수(difference)
>>> a.intersection(b)
{4, 5, 6}
>>> a.union(b)
{1, 2, 3, 4, 5, 6, 7, 8, 9}
>>> a.difference(b)
{1, 2, 3}
>>> b.difference(a)
{8, 9, 7}

#집합 원소 삭제(remove)
>>> a.remove(6)
>>> a
{1, 2, 3, 4, 5}

#집합 원소 1개 추가(add)
>>> a.add(6)
>>> a
{1, 2, 3, 4, 5, 6}

#집합 원소 여러 개 추가(update)
>>> b.update([10,11,12])
>>> b
{4, 5, 6, 7, 8, 9, 10, 11, 12}

#자료형의 유형 확인(type)
>>> a=True
>>> b=False
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>
  #불 자료형으로 잘 설정되어 있음
  
#수식의 결과도 불 자료형으로 확인 가능
>>> 1==1
True
>>> 10<100
True
>>> 10>100
False
>>> 0
0
  #0이 False 자료형이라길래 입력했는데 true로 나옴. 아마 수식으로써의 의미로 해석되어서 그런 것 같음.

#자료형의 참, 거짓
>>> a=[]
>>> while a:
...     print("true")
... else:
...     print("flase")
...
flase
  #비어있는 리스트는 거짓
  #a가 참이라면 <=> while a:
  
>>> a=['a', 'b', 'c', 'd', 'e']
>>> while a:
...     a.pop()
...
'e'
'd'
'c'
'b'
'a'
  #a가 참일 때까지 반복-> 모든 원소가 뽑히면 a가 거짓이 되므로 종료

#참 거짓 확인 함수(bool)
>>> bool(a)
False
>>> bool('a')
True
