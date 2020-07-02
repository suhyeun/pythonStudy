# 표준 입출력
print("python", "java") #띄어서 나옴
print("python" + "java") #붙어서 나옴

print("python", "java", sep=", ") #python, java 
print("python", "java", sep=" vs ") #python vs java

print("python", "java", sep=", ", end="?") #python, java
#end = 문장의 끝부분을 ?로 바꿔라
print("무엇이 더 재미있을까요?") #윗줄과 한줄로 나옴

import sys
print("python", "java", file = sys.stdout) #표준출력
print("python", "java", file = sys.stderr) #표준에러

# 시험 성적
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    # print(subject, score)
    # print(subject.ljust(8), score) #8칸의 자리를 만들고 왼쪽으로 정렬함
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# 은행 대기순번 표
# 001, 002, 003, ...
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3)) 
    #zfill = 3개만큼의 공간을 확보하고 집어넣는데, 값이 없는 공간은 0으로 채운다

# 표준입력
answer = input("아무 값이나 입력하세요 : ")
print(type(answer))
print("입력하신 값은 " + answer + "입니다.")
#사용자 입력(input)을 통해서 입력받으면 항상 str타입으로 나온다.

