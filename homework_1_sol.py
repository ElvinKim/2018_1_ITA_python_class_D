"""
Homework 1
"""
# problem 1
a = 20180205

year = int(a / 10000)
month = int((a % 10000) / 100)
day = a % 100

print("{:04d}.{:02d}.{:02d}".format(year, month, day))

# problem 2
"실습 풀기"
a = 20180108
str_a = str(a)
year = str_a[0:4]
month = str_a[4:6]
day = str_a[6:]
print(year + "년 " + month + "월 " + day + "일")

b = "hi SangMook"
print("hello" + b[2:])
print(b.replace("hi", 'hello'))

input_str = input("input : ")
print(input_str[0].upper() + input_str[1:-1].lower() + input_str[-1].upper())

# problem 3
word = input("input word: ")
"""첫 번째 알파벳은 그대로 두고 나머지 문자들은
under bar로 바꾸기
(예)
apple -> a____
python-> p_____"""
print(word[0] + "_" * (len(word) - 1))
print(word[0] + "_" * ",".join(word).count(","))

