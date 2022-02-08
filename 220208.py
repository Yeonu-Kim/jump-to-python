#클래스의 원리
result = 0
def add(num):
    global result
    result += num
    return result

print(add(6))
print(add(7))

result1 = 0
result2 = 0

def add1(num):
    global result1
    result1 += num
    return result1

def add2(num):
    global result2
    result2 += num
    return result2

print(add1(3))
#3
print(add2(5))
#5
print(add1(9))
#12
print(add2(8))
#13
#객체끼리는 서로 독립적임.

#사칙연산 맛보기
class Cal:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num
        return self.result

cal1 = Cal()
cal2 = Cal()
print(cal1.add(3))
#3
print(cal2.add(5))
#5
print(cal1.add(9))
#12
print(cal2.add(8))
#13

#사칙연산 계산기
class fourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

a = fourCal()
a.setdata(100,78)
print(a.first)
print(a.second)

b = fourCal()
b.setdata(56,99)
print(b.first)
print(b.second)

print(id(a.first))
#2477478972752
print(id(b.first))
#2477478971344

print(a.add())
#178
print(b.add())
#155
print(a.mul())
#7800
print(b.mul())
#5544

#사칙연산 계산기
class FourCal:
    def __init__(self, first, second):
      #__init__ == 생성자(Constructor), 객체가 생성될 때 자동으로 호출됨.
        self.first = first
        self.second = second

    def add(self):
        result = self.first + self.second
        return result

    def mul(self):
        result = self.first * self.second
        return result

    def div(self):
        result = self.first / self.second
        return result

a = FourCal(5,7)
#setdata 없이도 입력값 넣을 수 있음.
print(a.add())
print(a.mul())

#클래스 상속
#class 새로운 클래스 이름(상속할 클래스 이름)
class MoreFourCal(FourCal):
    def pow(self):
        result = self.first ** self.second
        return result

a = MoreFourCal(5,2)
print(a.pow())
#25
print(a.add())
#7
print(a.mul())
#10

#매서드 오버라이딩
#함수 내용 덮어 쓰기 가능
class SafeFourCal(MoreFourCal):
    def div(self):
        if self.second == 0:
            return "Error"
        else:
            return self.first / self.second

a = SafeFourCal(7,0)
print(a.div())
#Error
b=SafeFourCal(12,4)
print(b.div())
#3.0

# mod 1.py
#def add(a,b):
#    return a+b

#def mul(a,b):
#    return a*b

#if __name__ == "__main__":
#    print(add(6,7))
#    13
#    print(mul(6,7))
#    42

#자동으로 디렉터리가 이동되는 듯
import mod1
print(mod1.add(3,4))
print(mod1.mul(3,4))

from mod1 import add
print(add(3,4))

from mod1 import *
print(add(5,6))
print(mul(5,6))

#13, 42출력 없이 실행됨.
    
 

