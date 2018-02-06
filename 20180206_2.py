"""
제어문
"""
print("{:=^20}".format(" if문 "))
if 1 > 0:
    print('aaaa')
    print("bbbb")

    if True:
        print("cccc")
    print("dddd")

num = 10
if num % 2 == 0:
    print("짝수")
else:
    print("짝수")

if num > 0:
    print("양수")
elif num < 0:
    print("음수")
else:
    print("zero")

a = 12

if a % 3 == 0:
    print("3의 배수")
elif a % 4 == 0:
    print("4의 배수")
else:
    print("몰라몰라")

print("{:-^20}".format(" in operation "))
print("a" in ["a", "b", "c"])
print("python" in "python is good")

if 10:
    print("True야~~~~~~")

if None:
    print("False야~~~~")

print("{:=^20}".format(" while문 "))


i = 0 
while  i < 10:
    print(i)
    i += 1

x = 0    

while True:
    if 3 * x > 56:
        break
    x += 1

print(x)

x = 0

while 3 * x < 56:
    x += 1


a = 0
while a <= 20:
    a = a + 1
    if a % 2 == 1:
        continue
    print(a)
x = 0
while True:
    print(x)
    if x == 10:
        break
    x += 1

print("*", end="\n")
print("*", end="\n")
print("*", end="\n")
print("*", end="\n")

