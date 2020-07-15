#1.
our_pots = {"강소리":1, "강수연":2, "강은별":3, "김나은":4, "김수현":5, "김아름":6, "김연희":7, "손지우":8}

#2.
for name in our_pots:
    print(name)

#3.
for name in our_pots:
    print("{0} 집에는 {1}개의 냄비가 있다".format(name, our_pots[name]))

#4.
for name in our_pots:
    if our_pots[name] >= 3:
        print(name)

#5.
for name in our_pots:
    if our_pots[name] >= 3:
        print(name)
        break

#6.
for i in range(2,10):
    for j in range(1,10):
        print(i, "x", j , "=", i*j)
    print("=============")

#7.
dan = 2
while dan <= 9:
    i = 1
    while i <= 9:
        print(dan, "x", i, "=", dan*i)
        i += 1
    dan += 1
    print("----------------")

#8.