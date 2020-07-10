# 클래스

# 일반 유닛
# 부모 클래스
class Unit:
    def __init__(self, name, hp, speed):
        # __init__
        # 파이썬에서 사용되는 생성자
        #self.~ 멤버변수
        self.name = name
        self.hp = hp
        self.speed = speed
    
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이돌합니다. [속도 {2}]".format(self.name, location, self.speed))


# 공격 유닛
# 자식 클래스
class AttackUnit(Unit):
    def __init__ (self, name, hp, speed, damage):
        #Unit을 상속받으므로 name과 hp를 정의해 줄 필요가 없다.
        Unit.__init__(self, name, hp, speed)
        self.damage = damage
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다. [공격력{2}]".format(self.name, location, self.damage))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다.".format(self.name, damage))
        self.hp -= damage
        print("{0} : 현재 체력은 {1} 입니다.".format(self.name, self.hp))
        if self.hp <= 0:
            print("{0} : 파괴되었습니다.".format(self.name))

# 드랍쉽 : 공중 유닛, 수송기. 마린/파이어뱃/탱크 등을 수송. 공격X
# 날 수 있는 기능을 가진 클래스
class Flyable:
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0} : {1} 방향으로 날아갑니다. [속도{2}]".format(name, location, self.flying_speed))

# 공중 공격 유닛 클래스
# 다중상속
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, 0, damage) #지상 speed 0
        Flyable.__init__(self, flying_speed)
    
    # 메소드 오버라이딩
    # move 재정의
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)


# 건물
class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        #pass #아무것도 하지 않았지만 일단 넘김
        #방법1 Unit.__init__(self, name, hp, speed)
        #방법2
        super().__init__(name, hp, 0) #super를 통해서 초기화를 할 떄는 self를 쓰지 않음
        self.location = location



# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.")

# def game_over():
#     pass

# game_start()
# game_over()

# #marine과 tank는 Unit의 인스턴스
# #객체가 생성될 때는 __init__ 함수에 정의된 갯수와 동일하게 해야함 
# marine1 = Unit("마린", 40, 5)
# marine2 = Unit("마린", 40, 5)
# tank1 = Unit("탱크", 150, 35)
# # marine3 = Unit("마린") #실행불가

# #레이스 : 공중 유닛, 비행기, 클로킹(적에게 보이지 않음)
# wraith1 = Unit("레이스", 80, 5)
# print("유닛 이름 : {0}, 공격력 : {1}".format(wraith1.name, wraith1.damage))

# # 마인드 컨트롤 : 상대방 유닛을 내 것으로 만드는 것
# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True 
# # 클로킹이라는 변수는 없지만 밖에서 추가로 할당함
# # 단 밖에서 할당한 것은 할당한 객체에만 적용된다.

# if wraith2.clocking == True:
#     print("{0}는 현재 클로킹 상태입니다.".format(wraith2.name))
