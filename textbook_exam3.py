#gugudan_default
def gugudan_default(dan = 2):
    for i in range(1, 10):
        print("{0} X {1} = {2}".format(dan, i, dan*i))

gugudan_default()
gugudan_default(3)

#dice_return
import random

def dice(pip):
    result = random.randint(1,pip)
    return result

print("6면 주사위 값은 : ", dice(6))

