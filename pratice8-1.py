class Unit:
    def __init__(self):
        print("Unit 생성자")

class Flyable:
    def __init__(self):
        print("Flyable 생성자")

class FlyableUnit(Unit, Flyable):
    def __init__(self):
        #super().__init__()
        Unit.__init__(self)
        Flyable.__init__(self)

# super()는 다중 상속을 하지 못한다.
# super()는 처음 상속받은 class만 상속된다.
dropship = FlyableUnit()