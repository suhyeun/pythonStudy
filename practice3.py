# 문자열
sentence = "나는 소녀입니다"
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소녀이고,
파이썬은 쉬워요
"""
print(sentence3)

# 슬라이싱
jumin = "030624-1234567"

print("성별 : " + jumin[7])
print("생년 : " + jumin[0:2]) #0부터 2 직전까지 (0~1)
print("생월 : " + jumin[2:4])
print("생일 : " + jumin[4:6]) 

print("생년월일 : " + jumin[:6]) #처음부터 6 직전까지
print("뒤 7자리 : " + jumin[7:]) #7번째부터 끝까지
print("뒤 7자리(뒤에부터) : " + jumin[-7:]) #맨 뒤에서 7번째 부터 끝까지

# 문자열 처리 함수
python = "Python is Amazing"
print(python.lower()) #모든 문자를 소문자로 출력
print(python.upper()) #모든 문자를 대문자로 출력
print(python[0].isupper()) #[]번째 문자가 대문자인지 참또는 거짓으로 반환
print(len(python)) #문자열의 길이를 반환
print(python.replace("Python", "Java")) #지정한 문자열을 입력한 문자열로 변환하여 반환

index = python.index("n") #문자열에서 지정한 문자가 어느 위치에 있는지 반환
print(index)
index = python.index("n", index + 1) #문자열에서 지정한 문자가 첫번째 위치 다음에 어느 위치에 있는지 반환
print(index)

# # index와 find의 차이
print(python.find("Java")) #원하는 값이 문자열에 없을 경우에는 -1을 반환
print(python.index("Java")) #찾는 값이 없기 때문에 오류발생

print(python.count("n")) #원하는 값이 문자열에 얼마나 있는지 개수 반환

# 문자열 포맷
print("a" + "b")
print("a", "b")

# 방법 1
print("나는 %d살입니다." %20) #정수값만 들어올 수 있음
print("나는 %s를 좋아해요." %"파이썬") #정수, 문자 뭐든 들어올 수 있음
print("Apple 은 %c로 시작해요." %"A") #문자만 들어올 수 있음
print("나는 %s살 입니다." %20)
print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

# 방법2
print("나는 {}살입니다.".format(20)) #괄호 속 값을 중괄호에 대입
print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간")) #순서 바꾸기

# 방법3
print("나는 {age}살이며, {color}색을 좋아해요.".format(age=20, color="빨간"))
print("나는 {age}살이며, {color}색을 좋아해요.".format(color="빨간", age=20))

# 방법4(version 3.6 이상)
age = 20
color = "빨간"
print(f"나는 {age}살이며, {color}색을 좋아해요.") #앞에 f먼저 선언

# 탈출문자
print("조문도\n석사가의") #줄바꾸기

#\" \' : 문장 내에서 따옴표
#저는"나도코딩"입니다
print("저는 '나도코딩'입니다.")
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 \
print("C:\\Users\사용자\Desktop\6hourpython>")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #PineApple 출력

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple") #RedApple출력

# \t : 탭
print("Red\tApple")
