# 수식연산자
print(1 + 1) #2
print(3 - 2) #1
print(5 * 2) #10
print(6 / 3) #2
print(2 ** 3) #2^3=8
print(5 % 3) #나머지 구하기 2
print(10 % 3) #1
print(5 // 3) #몫 1
print(10 // 3) #3

# 대입연산자
print(10 > 3) #True
print(4 >= 7) #False
print(10 < 3) #False
print(5 <= 5) #Ture

# 비교연산자
print(3 == 3) #True
print(4 == 2) #False
print(3 + 4 == 7) #Ture
print(1 != 3) #True
print(not 1 != 3) #False

# 비트연산자
print((3 > 0) and (3 < 5)) #True
print((3 > 0) & (3 < 5)) #Ture
print((3 > 0) or (3 > 5)) #True
print((3 > 0) | (3 > 5)) #True
print((3 < 0) | (3 < 5)) #Ture

print(5 > 4 > 3) #True
print(5 > 4 > 7) #False

print(2 + 3 * 4) #14
print((2 + 3) * 4) #20

# 변수를 활용한 연산자 사용
number = 2 + 3 * 4 #14
print(number)
number = number + 2
print(number) #16
number += 2
print(number) #18
number *= 2 #36
print(number)
number /= 2 #18
print(number) 
number -= 2 #16
print(number)
number %= 2 #0
print(number)

# 숫자처리함수
print(abs(-5)) #절대값, 5반환
print(pow(4,2)) #앞숫자에 대한 뒷숫자번 제곱, 4^2 = 16
print(max(5,17)) #최대값 반환, 17
print(min(5,17)) #최소값 반환, 5
print(round(3.14)) #반올림, 3
print(round(4.99)) #반올림, 5

# math라이브러리 사용
from math import *
print(floor(4.99)) #내림, 4
print(ceil(3.14)) #올림, 4
print(sqrt(16)) #제곱근, 4

# random 함수
from random import *
print(random()) #0.0 ~ 1.0미만의 임의의 값 생성
print(random() * 10) #0.0 ~ 10.0미만의 임의의 값 생성
print(int(random() * 10)) #0 ~ 10미만의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10이하의 임의의 값 생성

# 로또
print(int(random() * 45) + 1) #1 ~ 45이하의 임의의 값 생성
print(randrange(1,45)) #1 ~ 45 미만의 임의의 값 생성
print(randrange(1,45) + 1) #1 ~ 45이하의 임의의 값 생성
print(randint(1, 45)) #1 ~ 45이하의 임의의 값 생성














