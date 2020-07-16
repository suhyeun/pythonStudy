# 후보2
def solution(password):
    capital_count, small_count, digit_count = 0, 0, 0
    for p in password:
        if p >= 'A' and p <= 'Z':
            capital_count += 1
        elif p >= 'a' and p <= 'z':
            small_count += 1
        elif p >= '0' and p <= '9':
            digit_count += 1
    if capital_count >= 1 and small_count >= 2 and digit_count >= 2:
        answer = True
    else:
        answer = False
    return answer

print(solution("Ajdksj872863"))

# 후보3
def mask_security_number(security_number):
   return security_number[:-4] + "****"

print(mask_security_number("0306241234567"))
print(mask_security_number("030624-1234567"))

# 후보8
def solution(sentence):
    result = []
    for sen in sentence:
        temp = ""
        for s in sen:
            if s in ",.?!":
                temp += s
        if temp  == "":
            result.append("특정한 문자가 없습니다.")
        else:
            result.append(temp)
    return result

sentence = []
n = int(input())
for i in range(n):
	sentence.append(input())
result = solution(sentence)
for r in result:
	print(r)

# ================================

# 소수
def primenum(num):
    count = 0
    for i in range(1, num+1):
        if num%i == 0:
            count += 1
    if count == 2:
        print("소수입니다")
    else:
        print("소수가 아닙니다")

primenum(5)

# 입력 숫자 뒤집어서 덧셈
# ex) 13 -> 31
# 13 + 31
def plusminus(number):
    renum = int(str(number)[::-1])
    if(number > renum):
        result = number - renum
    else:
        result = renum - number
    return number+renum, result

print(plusminus(31))

# 피보나치 수열
def fibonacci(n): 
    if n <= 1: 
        return n 
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(1,10): 
    print(fibonacci(i))

# 섭씨화씨
# 섭씨 -> 화씨
def celsius(num):
    return 9*num/5+32
print(celsius(32))

# 화씨 -> 섭씨
def fahrenheit(num):
    return (num-32)*5/9
print(fahrenheit(86))

# 중복된 문자 확인
def overlap(sen):
    answer = False
    for ch in range(0, len(sen)):
        for ch2 in range(ch + 1, len(sen)):
            if sen[ch] == sen[ch2]:
                answer = True
    return answer

print(overlap("aaaab"))
print(overlap("abdcfg"))
print(overlap("abdcfadgg"))
