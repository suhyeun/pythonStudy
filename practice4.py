# 리스트 []

# 지하철 칸별로 10명, 20명 30명
subway1 = 10
subway2 = 20
subway3 = 30

subway = [10, 20, 30]
print(subway)

subway = ["효정", "미미", "지호", "승희", "유아", "아린", "비니"]
print(subway)

# 승희가 몇 번째 칸에 타고 있는지
print(subway.index("승희")) #3

# 다음 정류장에서 진이가 다음 칸에 탑승
subway.append("진이")
print(subway)

# 배주현을 효정 / 미미 사이에 넣기
subway.insert(1, "배주현")
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway.pop())
print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇 명 있는지 확인
subway.append("배주현")
print(subway)
print(subway.count("배주현"))

# 정렬도 가능
num_list = [5, 4, 3, 2, 1]
num_list.sort()
print(num_list)

# 순서 뒤집기
num_list.reverse()
print(num_list)

# 모두 지우기
num_list.clear()
print(num_list)

# 다양한 자료형을 함께 사용
num_list = [5, 4, 3, 2, 1]
mix_list = ["효정", 24, True]
# print(mix_list)

# 리스트 확장
num_list.extend(mix_list)
print(num_list)

