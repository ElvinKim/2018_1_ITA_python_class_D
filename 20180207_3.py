"""
클래스
"""

class Student:
    student_id = "201811111"
    name = "영희"
    major = "KSE"
    age = 20
    fatigue = 0.9

    def eat(self, food):
        print(food + "를 먹자~~~~")

    def drink(self, soju):
        print(soju +"를(을) 마시자~~~~")

    def sleep(self):
        print("좀 자자")

    def do_homework(self, homework):
        print(self.name + "은(는) 과제 " + homework + "를 한다")


class Song:
    genre = "힙합"
    melody = "딴따라라다라라라 쿵쿵"
    rhythm = "쿵 ..... 쿵...... 쿵...... 쿵......"
    age_limit = 12


class Singer:
    swag = "스웨에에에에엑"
    agency = "JYP"

    def sing(self, song):
        print(song + "을 부르자~~~")

    def rap(self, rap):
        print("힙합 뿜뿜")

    def dance(self):
        print("빰빰!!!")




