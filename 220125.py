#true 아니고 True임
>>> burger=true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> 'burger'=true
  File "<stdin>", line 1
    'burger'=true
    ^^^^^^^^
SyntaxError: cannot assign to literal here. Maybe you meant '==' instead of '='?
>>> money=true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
>>> money=true
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined. Did you mean: 'True'?
#if문의 구조
>>> burger=True
>>> if burger:
...     print("yummy")
... else:
...     print("I want to eat this burger.")
...
yummy

>>> money=True
>>> if money:
...     print("taxi")
... else:
...     print("walk")
...
taxi

#띄어쓰기 잘못하면 안 됨.(tab 1회 or 스페이스바 4번)
>>> if card:
...     print("bus")
... print("metro")
  File "<stdin>", line 3
    print("metro")
    ^^^^^
SyntaxError: invalid syntax

#부등호 사용
>>> money=4000
>>> if money >=3000:
...     print("taxi")
... else:
...     print("walk")
...
taxi

#or/and/not
>>> if money>=3000 or card:
...     print("taxi")
... else:
...     print('walk')
...
taxi

#리스트 in/not in
>>> pocket=['card', 'cellphone']
>>> if 'money' in pocket:
...     print('taxi')
... else:
...     print('walk')
...
walk

#elif
>>> if 'money' in pocket:
...     print('taxi')
... elif 'card' in pocket:
...     print('bus')
... else:
...     print('walk')
...
bus

#if문을 간단히 표현하는 방법
#(참일 때 output)+if+(조건문)+else+(거짓일 때 output) -> 엑셀 감성
>>> message='taxi' if 'money' in pocket else 'walk'
>>> message
'walk'

#출석부 만들기
>>> attendance = 0
>>> while attendance<=10:
...     attendance=attendance+1
...     print('Hello! %d times left until attendance is completed.' %attendance)
...
Hello! 1 times left until attendance is completed.
Hello! 2 times left until attendance is completed.
Hello! 3 times left until attendance is completed.
Hello! 4 times left until attendance is completed.
Hello! 5 times left until attendance is completed.
Hello! 6 times left until attendance is completed.
Hello! 7 times left until attendance is completed.
Hello! 8 times left until attendance is completed.
Hello! 9 times left until attendance is completed.
Hello! 10 times left until attendance is completed.
Hello! 11 times left until attendance is completed.

#왜 출석 일수가 점점 늘어나지.. 10-atd로 변경

>>> attendance = 0
>>> while attendance<=10:
...     attendance=attendance+1
...     print('Hello! %d times left until attendance is completed.' %(10-attendance) )
...     if attendance==10:
...             print('Thank you for your effort.')
...
Hello! 9 times left until attendance is completed.
Hello! 8 times left until attendance is completed.
Hello! 7 times left until attendance is completed.
Hello! 6 times left until attendance is completed.
Hello! 5 times left until attendance is completed.
Hello! 4 times left until attendance is completed.
Hello! 3 times left until attendance is completed.
Hello! 2 times left until attendance is completed.
Hello! 1 times left until attendance is completed.
Hello! 0 times left until attendance is completed.
Thank you for your effort.
Hello! -1 times left until attendance is completed.
#-1회 출석은 뭐지. 등호 빼기

#완성본
>>> atd = 0
>>> while atd<10:
...     atd=atd+1
...     print("Hello! %d times left until your attendances are completed." %(10-atd))
...     if atd==10
  File "<stdin>", line 4
    if atd==10
              ^
SyntaxError: expected ':'
>>>
>>> atd = 0
>>> while atd<10:
...     atd=atd+1
...     print('Hello! %d times left until this class is completed.' %(10-atd))
...     if atd==10:
...             print('Congratulation!')
...
Hello! 9 times left until this class is completed.
Hello! 8 times left until this class is completed.
Hello! 7 times left until this class is completed.
Hello! 6 times left until this class is completed.
Hello! 5 times left until this class is completed.
Hello! 4 times left until this class is completed.
Hello! 3 times left until this class is completed.
Hello! 2 times left until this class is completed.
Hello! 1 times left until this class is completed.
Hello! 0 times left until this class is completed.
Congratulation!

#메뉴판
>>> menu = '''
... 1. burger - 300
... 2. pizza  - 500
... 3. chicken- 700
...
... enter the number of menu: '''
>>> number = 0
>>> while number !=3:
...     print(menu)
...     number=int(input())
...

1. burger - 300
2. pizza  - 500
3. chicken- 700

enter the number of menu:
1

1. burger - 300
2. pizza  - 500
3. chicken- 700

enter the number of menu:
2

1. burger - 300
2. pizza  - 500
3. chicken- 700

enter the number of menu:
3

#커피 머신

>>> coffee=10
>>> while True:
...     money=int(input())
...     if money==500:
...             print('This coffee is here!')
...     elif money>=500:
...             print('This coffee is here! The change is %d won.' %(money-500))
...     else:
...             print('You didn't insert enough money.')
  File "<stdin>", line 8
    print('You didn't insert enough money.')
          ^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
#어퍼스트로피 잘못 찍음.

>>> coffee=10
>>> while True:
...     money=int(input())
...     if money==500:
...             print('This coffe is here!')
...     elif money>=500:
...             print('This coffee is here! The change is %d won.' %(money-500)
...     else:
  File "<stdin>", line 7
    else:
    ^^^^
SyntaxError: invalid syntax
#괄호 어디감?

>>> coffee=10
>>> while True:
...     money=int(input())
...     if money==500:
...             print('Here is your coffee!')
...     elif money>500:
...             print('Here is your coffee! The change is %d won.' %(money-500))
...     else:
...             print('There is not enough money.')
...     if coffee>0:
...             print('%d cups of coffee are left.' %(9-coffee))
...             coffee=coffee-1
...     else:
...             print('Sorry. Our Coffee is sold out.')
...             break
...
600
Here is your coffee! The change is 100 won.
-1 cups of coffee are left.
#커피 개수 이상하게 써 놓음. %(coffee-1)로 변경
