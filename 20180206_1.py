"""
자료형 (2)
"""

print("{:=^20}".format(" 리스트 "))
print("{:-^20}".format(" 리스트 자료형 "))
a = [1, 2, 3, 4, 5]
print(a[2])
print(a[2:3][0])

print("{:-^20}".format(" 리스트 연산자 "))
print([1, 2, 3] + [4, 5, 6])
print([1, 2, 3] * 3)

print("{:-^20}".format(" 리스트 수정하기 "))
a = [1, 2, 3, 4, 5]
a[0] = 100
a[4] = 500
a[1:4] = [200, 300, 400]

a[0:1] = [1, 2, 3]
print(a)

print("{:-^20}".format(" 리스트 삭제하기 "))
a = [1, 2, 3, 4, 5]
del a[1]
print(a)
a[1:2] = []
print(a)

print("{:-^20}".format(" 리스트 관련 함수 "))
a = [1, 2, 3, 4]
a.append(5)
print(a)

# sort
b = [3, 4, 2, 1, 6]
print(b.sort())
# print(b.sort(reverse=True))
print(b)

# reverse
print(b.reverse())
print(b)

# index
print(b)
print(b.index(4))

# remove
c = [1, 2, 3, 1, 2, 3, 5]
c.remove(2)
print(c)

# insert
c = [2, 3, 4, 5, 6, 7, 8]
c.insert(0, 1)
print(c)

# pop
print(c.pop())
print(c.pop(0))
print(c)

# count
print([1, 2, 3, 1, 2, 1, 4, 5].count(2))

# extend
a = [1, 2, 3]
b = [4, 5, 6]
a.extend(b)  # a = a + b, a += b
print(a)

print("{:=^20}".format(" 튜플 "))
t = (1, 2, 3, 4, 5)
print(t[0])
# t[0] = 100

print("{:=^20}".format(" 딕셔너리 "))
my_info = {"name": "영희", "age": 20,
           "favorite_food": ["순대", "튀김", "삼합"]}
print(my_info["name"], my_info["age"])
print(my_info["favorite_food"])

my_info["id"] = "20180202"
del my_info["age"]
print(my_info)

print("{:-^20}".format(" 딕셔너리 관련 함수"))

# keys
print(my_info.keys())

# values
print(my_info.values())

# items
print(my_info.items())

# get
print(my_info["name"])
print(my_info.get("name"))

# print(my_info["major"]) error
print(my_info.get("major"))

print("{:=^20}".format(" 집합 자료형 "))
lst = [1, 2, 3, 1, 2, 3, 4, 5, 1, 2]
new_lst = list(set(lst))
print(new_lst)
t = (1, 2, 3, 4)
t_to_lst = list(t)
print(t_to_lst)
l = [1, 2, 3, 4]
l_to_tuple = tuple(l)
print(l_to_tuple)






