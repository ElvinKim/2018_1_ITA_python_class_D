""" 자료형 (1)
"""
print("{:-^20}".format(" 숫자형 자료형 "))
a = 10
A = 100
b = "ABC"
sangmook = "안녕"
print(a)
print(A)
print(b)
print(sangmook)

print(3.2e2)
print(3**3)

print("{:-^20}".format(" 문자형 자료형 "))
a = "12345"
print(int(a) + 10)
print(str(12345))
'a'
"python is good"

print("-" * 30)
print("I\'m SangMook")
print("Life is too short\nYou need Python")
print("-" * 30)
print("""Life is too short
you need python""")
print(1, "\n", 2)

print("{:-^20}".format(" 문자열 연산자 "))
print("abc" + "def")
print("A" * 20)

print("{:-^20}".format(" 문자열 인덱싱 "))
a = "ABCDEFG"
print(a[0])
print(a[2])
print(a[-2])
# print(a[7]) error

print("{:-^20}".format(" 문자열 슬라이싱 "))
a = "ABCDEFG"
print(a[0:2])
print(a[2:])
print(a[2:-1])

print("{:-^20}".format(" 문자열 포맷팅 "))
birth_format = "나는 %d월에 태어났습니다."
name_format = "나의 이름은 %s 입니다."
name_age_format = "나의 이름은 %s 이고 %d살 입니다."
name_age_format_ver2 = "나의 이름은 %s 이고 %s살 입니다."
print(birth_format % 12)
print(birth_format % 1)
print(name_format % "김상묵")
print(name_age_format % ("김상묵", 20))
print(name_age_format_ver2 % ("김상묵", str(20)))

print("{:-^20}".format(" 문자열 함수 "))
a = "ABCABCEEASD"

# count
print(a.count("AB"))

# index & find
print(a.find("B"))
print(a.index("B"))
print(a.find("X"))
# print(a.index("X"))

# join
print(",".join(a))

# upper & lower
print("abdaDASDea".upper())
print("abdaDASDea".lower())

# strip
print("             hi            ".lstrip())
print("             hi            ".rstrip())
print("             hi            ".strip().replace("hi", "hello"))

# replace
print("hi hi hi bye bye SangMook".replace("hi", "hello"))
print("hello hello hello bye bye SangMook".replace("bye", 'oh'))

# split
print("ABC DEF GH".split())
print("ABC,DEF,GH".split(","))
sentence = """asdf
asdf  asdf asdf asdf
asdf asdf asdf
asdfasd
asdf"""
print(sentence.split("\n"))
print("--".join("ABC DEF GH".split()))

print("{:-^20}".format(" 문자열 포맷팅 2 "))
format_a = "나이 이름은 {}입니다."
print(format_a.format("김상묵"))
print("나이 이름은 {}입니다.".format("김상묵"))
print("나이 이름은 {}이고 나이는 {}입니다..".format("김상묵", 20))
print("나이 이름은 {1}이고 나이는 {0}입니다..".format(20, "김상묵"))

print('{:<10} Sangmook'.format('hi'))
print('{:>10} Sangmook'.format('hi'))
print('{:^10} Sangmook'.format('hi'))
print('{:?^10} Sangmook'.format('hi'))
