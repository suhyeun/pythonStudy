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

# 다양한 출력포맷
# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보
print("{0: >10}".format(500))

# 양수 일때는 +로 표시, 음수일 때는 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500)) #반드시 꺾쇠 앞에 부호를 붙여야 함

# 왼쪽 정렬하고, 빈칸을 _로 채움
print("{0:_<+10}".format(500))

# 3자리마다 ,를 찍어주기
print("{0:,}".format(100000000000))

# 3자리마다 ,를 찍어주기, +- 부호도 붙이기
print("{0:+,}".format(100000000000))
print("{0:+,}".format(-100000000000))

# 3자리마다 ,를 찍어주고, 부호도 붙이고, 자릿수 확보하기
# 돈이 많으면 행복하니까 빈자리는 ^로 채우기
print("{0:^<+30,}".format(100000000000))

# 소수점 출력
print("{0:f}".format(5/3))

# 소수점을 특정 자리수까지만 표시
print("{0:.2f}".format(5/3)) #소수점 셋째 자리에서 반올림

from primetext import primelist 
primenumber=primelist() 
# primenumber는 1000000개의 소수를 포함한 리스트

# 파일입출력
w = write, a = append, r = read
score_file = open("score.txt", "w", encoding="utf8")
print("수학  : 0", file = score_file)
print("영어  : 50", file = score_file)
score_file.close()

score_file = open("score.txt", "a", encoding="utf8")
score_file.write("과학 : 80")
score_file.write("\n코딩 : 100") #write를 통해서 입력을 받을 때는 줄바꿈이 적용되지 않음
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.read()) #파일의 모든 내용을 읽어옴
score_file.close()

score_file = open("score.txt", "r", encoding="utf8")
print(score_file.readline()) #줄별로 읽기, 한 줄 읽고 커서는 다음 줄로 이동
print(score_file.readline(), end="") #줄바꿈을 하기싫으면 end사용
print(score_file.readline(), end="")
print(score_file.readline(), end="")
score_file.close()

# 몇 줄인지 모를 때
score_file = open("score.txt", "r", encoding="utf8")
while True:
    line = score_file.readline()
    if not line:
        break
    print(line, end="")
score_file.close

lines = score_file.readlines() #list형태로 저장
for line in lines:
    print(line, end="")
score_file.close()


