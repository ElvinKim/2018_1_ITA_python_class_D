"""문장을 입력받고 처음 단어랑 마지막 단어 출력하기"""
input_sentence = input("input sentence : ")
lst_sentence = input_sentence.split()

first_word = lst_sentence[0]
last_word = None

if lst_sentence[-1][-1] in ["'", '"']:
    if lst_sentence[-1][-2] in [".", "!", "?"]:
        last_word = lst_sentence[-1][:-2]
    else:
        last_word = lst_sentence[-1][:-1]
elif lst_sentence[-1][-1] in [".", "!", "?"]:
    last_word = lst_sentence[-1][:-1]

print(last_word)

"""
국어 영역 90점, 수학 영역 98점, 영어 영역 60점
이를 딕셔너리 자료형으로 표현하기
"""
my_score = {"국어영역": 90, "수학영역": 98, "영어영역": 60}

"""
국어 영역, 수학 영역, 영어 영역 점수를 입력받고
이를 딕셔너리 자료형으로 표현하기
단!!! input은 한 번만 쓰기
"""
input_score = input("input score : ")
score = input_score.split()

my_score = {"국어영역": int(score[0]), "수학영역": int(score[1]), "영어영역": int(score[2])}

"""
제어문 if 실습 부분
"""

"""
제어문 while 실습 부분
"""
i = 0

while i < 10:
    print("*", end="")
    i += 1

x = 0

while x ** 3 < 10000:
    x += 1
print(x)
