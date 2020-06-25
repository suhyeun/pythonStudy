'''
사이트별로 비밀번호를 만들어 주는 프로그램을 작성하시오

ex) http://naver.com
규칙1 : http:// 부분은 제외 => naver.com
규칙2 : 처음 만나는 점(.) 이후 부분은 제외 => naver
규칙3 : 남은 글자 중 처음 세 자리 + 글자 개수 + 글자 내 'e' 갯수 + "!"로 구성
                (nav)               (5)             (1)             (!)

ex) 생성된 비밀번호 : nav51!
'''

# my
site = "http://naver.com"
pw = site[7:site.index(".")]
password = pw[:3] + str(len(pw)) + str(pw.count("e")) + "!"
print(password)

# teacher
# url = "http://naver.com
url = "http://youtube.com"
my_str = url.replace("http://", "") #규칙1
# print(my_str)
my_str = my_str[:my_str.index(".")] #규칙2
# print(my_str)
password_t = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1} 입니다.".format(url, password_t))
