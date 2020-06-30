# 함수
def open_account():
    print("새로운 계좌가 생성되었습니다.")

# open_account()

# 전달값과 반환값
def deposit(balance, money): #입금
    print("입금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance + money))
    return balance + money

def withdraw(balance, money): #출금
    if balance >= money: #잔액이 출금보다 많으면
        print("출금이 완료되었습니다. 잔액은 {0}원 입니다.".format(balance-money))
        return balance - money
    else:
        print("출금이 완료되지 않았습니다. 잔액은 {0}원 입니다.".format(balance))
        return balance

def withdraw_night(balance, money): #저녁에 출금
    commission = 100 #수수료 100원
    return commission, balance - money - commission

balance = 2000 #잔액
balance = deposit(balance, 1000)
print(balance)

# balance = withdraw(balance, 2000)
balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance, 500)
print("수수료는 {0}원이고, 잔액은 {1}원 입니다.".format(commission, balance))

# 기본값
def profile(name, age, main_lang):
    print("이름 : {0} \t 나이 : {1} \t 주 사용 언어 : {2}".format(name, age, main_lang))

profile("효정", 26, "python")
profile("미미", 24, "java")

# 같은 학교 같은 학년 같은 반 같은 수업
def profile(name, age = 17, main_lang = "python"):
    print("이름 : {0} \t 나이 : {1} \t 주 사용 언어 : {2}".format(name, age, main_lang))

profile("효정")
profile("미미")

# 키워드 값
def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name = "아린", main_lang = "파이썬", age = 21)
profile(main_lang = "java", name = "미미" , age = 23)

# 가변인자
def profile(name, age, lang1, lang2, lang3, lang4):
    print("이름 : {0} \t나이 : {1} \t".format(name, age), end = "") #end="" 줄바꿈없이 쭉 이어서 출력
    print(lang1, lang2, lang3, lang4)

def profile(name, age, *language):
    print("이름 : {0} \t나이 : {1} \t".format(name, age), end = "") #end="" 줄바꿈없이 쭉 이어서 출력
    for lang in language:
        print(lang, end=" ")
    print()

profile("유아", 23, "python", "java", "html", "C", "C#")
profile("비니", 22, "C++" , "java")

# 지역변수와 전역변수
gun = 10

def checkpoint(soldiers): #경계근무
    #gun = 20
    global gun #전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내]남은 총 : {0}".format(gun))

def checkpoint_ret(gun, soldiers):
    gun = gun - soldiers
    print("[함수 내]남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
#checkpoint(2) #2명이 경계 근무 나감
gun = checkpoint_ret(gun, 2)
print("남은 총 : {0}".format(gun))