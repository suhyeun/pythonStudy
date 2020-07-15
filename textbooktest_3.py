# gugudan2
# def gugudan2(start, end):
#     for dan in range(start, end+1):
#         for i in range(1, 10):
#             print("{0} X {1} = {2}".format(dan, i, start*i))
#         print("============")

# gugudan2(2, 4)hn

# gugudan3
# def gugudan3(*dans):
#     for dan in dans:
#         for i in range(1, 10):
#             print("{} X {} = {}".format(dan, i ,dan*i))
#         print("============")

# gugudan3(2, 3, 7)

# circle_area
# def circle_area(r):
#     result = 3.14 * (r/2) * (r/2)
#     return result

# print(circle_area(3))

# sum_avg
# def sum_avg(*nums):
#     #my
#     # sum = 0
#     # avg = 0
#     # for num in nums:
#     #     sum += num
#     # avg = sum/len(nums)

#     # return sum, avg
#     return(sum(nums), sum(nums)/len(nums))

# print(sum_avg(4, 4, 4))

# prime
# def prime(start, end):
#     result = []
#     for i in range(start, end):
#         flag = True
#         for j in range(2, i):
#             if i % j == 0:
#                 flag = False
#                 break
#         if flag:
#             result.append(i)
#     return result

# print(prime(1,100))

# login
# def login(id, pw):
#     if(id == 'scott' and pw == 'tiger'):
#         return True
#     else:
#         return False
# print(login('asdas', 'asdasdasd'))

# wc
# def wc(chars):
#     count = 0
#     for char in chars:
#         if(char == '' or char == '\t' or char == '\n'):
#             continue
#         count = count + 1
#     return count

# string = "하이하이  아아\t 파이썬존망\n"
# print(string)
# print(wc(string)) #글자 개수

# wc2
def wc2(chars):
    char_count = 0
    whitespace_count = 0
    word_count = 0
    word_flag = False
    
    for char in chars:
        if(char == '' or char == '\t' or char == '\n'):
            whitespace_count = whitespace_count+1
            word_flag = False
        char_count = char_count+1
        if word_flag == False:
            word_count = word_count+1
            word_flag = True
    return word_count, char_count, whitespace_count

string = "하이하이  아아\t 파이썬존망\n"
print(string)
print(wc2(string)) #단어, 글자, 공백문자


