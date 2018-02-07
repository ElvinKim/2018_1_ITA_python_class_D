"""
제어문
"""

print("{:=^20}".format(" for 문 "))

for num in [1, 2, 3, 4, 5, 6]:
    print(num)

for c in "ABCDEFG":
    print(c)

print("-" * 20)
for num in range(1, 10):
    print(num)


for _ in range(10):
    print("*", end="")


for x in range(1, 21):
    if x % 2 == 0:
        continue
    print(x)


print("-" * 20)

for i in range(2, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i , j , i * j))
    print("-" * 10)

print("{:-^20}".format(" Level Up! "))

lst = []
for num in range(10):
    lst.append((num + 1) ** 3)

lst = [(num + 1) ** 3 for num in range(10)]
print(lst)

# input_numbers = input("input numbers : ")
#
# number_lst = [int(str_num) for str_num in input_numbers.split()]
# print(number_lst)

# enumerate
idx = 0
for c in "ABCBBDCEFG":
    print(idx, c)
    idx += 1

print("-" * 20)
for i, c in enumerate("ABCBBDCEFG"):
    print(i, c)

# 
print("-" * 20)
a = ["A", "B", "C", "D"]
b = ["a", 'b', 'c']

for x in range(min([len(a), len(b)])):
    print(a[x], b[x])

print("-" * 20)
for x, y in zip(a, b):
    print(x, y)














