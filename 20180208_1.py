"""
클래스
"""
class Knight:
    level = 20
    name = "만년동꿀주먹"
    hp = 200

    def move(self, direction):
        print(self.name + "이 " + direction + "방향으로 이동합니다.")

    def attack(self):
        print("attack", id(self))
        print(self.name + "이 공격합니다.")

k = Knight()
print(k.name, k.level, k.hp)
k.attack()

print("{:-^20}".format(" Namespace "))
print(Knight.__dict__)
print(k.__dict__)
print(k.name)
k.name = "어은동핵폭탄"
print(k.__dict__)
print(k.name)
k.mp = 100
print(k.mp)
print(k.__dict__)
print(Knight.__dict__)

class Student:
    definition = "생전에 벼슬을 하지 아니하고 죽은 사람의 명정, 신주, 지방 따위에 쓰는 존칭"

    def __init__(self, s_id, n, m, a):
        self.student_id = s_id 
        self.name = n
        self.major = m
        self.age = a

    def eat(self, food):
        print(food + "를 먹자~~~~")

    def drink(self, soju):
        print(soju +"를(을) 마시자~~~~")

    def sleep(self):
        print("좀 자자")

    def do_homework(self, homework):
        print(self.name + "은(는) 과제 " + homework + "를 한다")

    def set_name(self, name):
        self.name = name

    def get_name(self):
        return self.name

    def set_student_id(self, s_id):
        self.student_id = s_id

    def get_student_id(self):
        return self.student_id

    def set_age(self, age):
        if age < 0:
            self.age = 0
        else:
            self.age = age



student1 = Student("20181111", "영희", "컴퓨터 공학", 20)
student2 = Student("20182222", "민수", "전기전자", 30)

student1.age + 100


class A:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def print_a(self):
        print(self.a)


class B:
    def print_a(self):
        print("몰라몰라")

    def print_b(self):
        print(self.b)

class C(B, A):
    pass

c= C("A", "B")
c.print_a()

# b = B("A", "B")
# b.print_a()
# b.print_b()

# a = A("A", "B")














