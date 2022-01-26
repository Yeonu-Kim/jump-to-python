#for문의 형식
>>> a=[1,2,3]
>>> for i in a:
...     print(i)
...
1
2
3

#for문에서 튜플 활용
>>> a=[(1,2),(5,6),(8,9)]
>>> for (b,c) in a:
...     print(b+c)
...
3
11
17

#for문으로 합불 문자 보내기
>>> scores=[90, 25, 67, 45, 80]
>>> number=0
>>> for i in scores:
...     number=number+1
...     if i>=60: print('%d번 학생 합격을 축하합니다!' %number)
...     else: print('죄송합니다. %d번 학생은 불합격하셨습니다.' %number)
...
1번 학생 합격을 축하합니다!
죄송합니다. 2번 학생은 불합격하셨습니다.
3번 학생 합격을 축하합니다!
죄송합니다. 4번 학생은 불합격하셨습니다.
5번 학생 합격을 축하합니다!

#for+continue로 합격 문자 보내기
>>> number=0
>>> for i in scores:
...     number=number+1
...     if i<60:
...             continue
...     else:
...             print('%번 학생 합격을 축하합니다!' %number)
...
Traceback (most recent call last):
  File "<stdin>", line 6, in <module>
ValueError: unsupported format character '?' (0xbc88) at index 1
#continue는 엔터치면 안 되나 봄.

>>> number=0
>>> for i in scores:
...     number=number+1
...     if i<60: continue
...     else: print('%d번 학생 합격을 축하합니다!' %number)
...
1번 학생 합격을 축하합니다!
3번 학생 합격을 축하합니다!
5번 학생 합격을 축하합니다!

#range문으로 숫자 더하기
>>> add=0
>>> for i in range(1,11):
...     add=add+i
...
>>> print(add)
55
>>> add
55
#print 찍어도 되고 걍 add 쳐봐도 됨.

#for+continue+range로 합격문자 보내기
>>> for i in range(len(scores)):
...     if scores[i]<60: continue
...     else: print('%d번 학생 합격을 축하합니다!' %(i+1))
...
1번 학생 합격을 축하합니다!
3번 학생 합격을 축하합니다!
5번 학생 합격을 축하합니다!

#구구단 기계
>>> for i in range(2,10):
...     for j in range(1,10):
...             print(i*j, end=' ')
#end=''는 엔터 치지 않고 띄어쓰기만 하겠다는 의미
...     print(' ')
#print('')는 이제 엔터를 치겠다는 의미
...
2 4 6 8 10 12 14 16 18
3 6 9 12 15 18 21 24 27
4 8 12 16 20 24 28 32 36
5 10 15 20 25 30 35 40 45
6 12 18 24 30 36 42 48 54
7 14 21 28 35 42 49 56 63
8 16 24 32 40 48 56 64 72
9 18 27 36 45 54 63 72 81

#리스트 내포로 단순화하기
>>> a=[i*j for i in range(2,10)
...     for j in range(1,10)]
>>> a
[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]
>>> print(a)
[2, 4, 6, 8, 10, 12, 14, 16, 18, 3, 6, 9, 12, 15, 18, 21, 24, 27, 4, 8, 12, 16, 20, 24, 28, 32, 36, 5, 10, 15, 20, 25, 30, 35, 40, 45, 6, 12, 18, 24, 30, 36, 42, 48, 54, 7, 14, 21, 28, 35, 42, 49, 56, 63, 8, 16, 24, 32, 40, 48, 56, 64, 72, 9, 18, 27, 36, 45, 54, 63, 72, 81]

#3장 연습문제
#연습문제 1번
#답:shirt

>>> a="Life is too short, you need python."
>>>
>>> if 'wife' in a: print('wife')
... elif 'python' in a and 'you' not in a: print('python')
... elif 'shirt' not in a: print('shirt')
... elif 'need' in a: print('need')
... else: print('none')
...
shirt

#연습문제 2번

>>> i=0
>>> while i<=1000:
...     i=i+1
...     if i % 3 !=0: continue
...     else: result=result+i
...
>>> print(result)
166833

#연습문제 3번
>>> i=0
>>> while True:
...     i=i+1
...     if i>5: break
...     print('*'*i)
...
*
**
***
****
*****

#연습문제 4번
#원래는 100까지인데 그냥 10개로 줄임.
>>> for i in range(1,11):
...     print(i)
...
1
2
3
4
5
6
7
8
9
10

#연습문제 5번
#리스트 중에서 80을 빼먹어서 답은 다르게 나오지면 코드는 맞음.
>>> A=[70,60,55,75,95,90,80,85,100]
>>> total=0
>>> for i in A:
...     total=total+i
... average=total/len(A)
  File "<stdin>", line 3
    average=total/len(A)
    ^^^^^^^
SyntaxError: invalid syntax
#...이 끝나지 않은 상태에서 average 변수를 추가해서 오류 발생

>>> A=[70,60,55,75,95,90,80,85,100]
>>> total=0
>>> for i in A:
...     total=total+i
...
>>> average=total/len(A)
>>> print(average)
78.88888888888889

#연습문제 6번
>>> numbers=[1,2,3,4,5]
>>> result=[n*2 for n in numbers if n%2==1]
>>> print(result)
[2, 6, 10]
