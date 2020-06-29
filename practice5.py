# 분기(if문)
weather = input("오늘 날씨는 어때요?")

if weather == "비" or weather == "눈":
    print("우산을 챙기세요")
elif weather == "미세먼지":
    print("마스크를 챙기세요")
else:
    print("준비물이 필요없어요")

temp = int(input("기온은 어때요? "))
if 30 <= temp:
    print("너무 더워요. 나가지 마세요")
elif 10 <= temp and temp < 30:
    print("괜찮은 날씨에요")
elif 0 <= temp and temp < 10:
    print("외투를 챙기세요")
else:
    print("너무 추워요. 나가지 마세요")

# 반복문(for문)
print("대기번호  : 1")
print("대기번호  : 2")
print("대기번호  : 3")

for waiting_num in [0,1,2,3,4]:
    print("대기번호 : {0}".format(waiting_num))

for waiting_num in range(1, 5): #1부터 5미만까지
    print("대기번호 : {0}".format(waiting_num))

starbucks = ["효정", "미미", "유아"]
for customer in starbucks:
    print("{0}님, 주문하신 메뉴 나왔습니다".format(customer))

# while문
customer = "비니"
index = 5
while index >= 1:
    print("{0}님, 커피가 준비되었습니다. {1}번 남았습니다.".format(customer, index))
    index -= 1
    if index == 0:
        print("커피는 폐기처분 되었습니다.")

customer = "승희"
index = 1
while True:
    print("{0}님, 커피가 준비되었습니다. 호출 {1}회".format(customer, index))
    index += 1
    #무한루프

customer = "아린"
person = "Unknown"

while person != customer:
    print("{0}님, 커피가 준비되었습니다.".format(customer))
    person = input("이름이 어떻게 되세요?")

# continue와 break문
absent = [2,5] #결석
no_book = [7] #책을 깜빡함
for student in range(1, 11):
    if student in absent:
        continue
    elif student in no_book:
        print("오늘 수업은 여기까지. {0}은 교무실로 따라와라.".format(student))
        break
    print("{0}번, 책을 읽으세요".format(student))

# 한 줄 for문
# 출석번호가 1, 2, 3, 4 앞에 100을 붙이기로 함 -> 101, 102, 103, 104
student = [1, 2, 3, 4, 5]
print(student)
student = [i+100 for i in student] 
print(student)

# 학생 이름을 길이로 변환
students = ["승희", "효정", "유아"]
students = [len(i) for i in students]
print(students)

# 학생 이름을 대문자로 변환
students = ["Hyo", "Yu", "Mi"]
students = [i.upper() for i in students]
print(students)