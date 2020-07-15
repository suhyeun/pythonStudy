#5.
for i in range(1, 101):
    if i%2 != 0:
        print(i)

#6.
for i in range(100, 201):
    if i%3 == 0:
        print(i)

#7.
num = int(input("숫자를 입력하시오 : "))
count = 0
for i in range(1, num+1):
    if num%i == 0:
        count += 1

if count == 2:
    print("소수입니다")
else:
    print("소수가 아닙니다")

#8.
prime_count = 0
for num in range(1, 100):
    count = 0

    for i in range(1, num+1):
        if num%i == 0:
            count += 1
    
    if count == 2:
        prime_count += 1

print(prime_count)
