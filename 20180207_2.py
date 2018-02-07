"""
함수
"""

def add(a, b):
    return a + b

print(add(10, 20))
print(add("A", "B")[0])

def odd_even(num):
    if num % 2 == 0:
        return "짝수"
    else:
        return "홀수"


print(odd_even(10))
print("-" * 20)


def average(a, b):
    return (a + b) / 2

print(average(10 , 20))


# def list_average(lst):
#     total = 0
#     cnt = 0
#
#     for num in lst:
#         total += num
#         cnt += 1
#
#     return total / cnt

def list_average(lst):
    return sum(lst) / len(lst)


def say_my_name():
    return "영희"

print(say_my_name())


def print_my_name(name):
    print(name)

print_my_name("수지")

def say_hi():
    print('hi') 

print(say_hi())

a = [1, 2, 3]
print(a.sort())

print("{:-^20}".format(" 매개변수 "))

def my_sum(*args):
    return sum(args)

def sample(a, b, *args):
    print(a)
    print(b)
    print(args)

sample(1, 2, 3, 4)

print("{:-^20}".format(" 실습 "))
def my_average(*args):
    return sum(args) / len(args)


def my_concat(c, *args):
    return c.join(args)

print(my_concat('-', 'abc', 'def', 'ghi', 'jkl'))

print("{:-^20}".format(" 반환값 "))

def sum_sub(a, b):
    return a + b, a - b
print(sum_sub(1, 2))
x, y = sum_sub(2, 1)
print(x)
print(y)


def print_my_name(name):
    if name == "":
        return
    print(name)

print_my_name("영희")


print("{:-^20}".format(" 실습 "))

def get_max_min(lst):
    if len(lst) < 2:
        return

    return max(lst), min(lst)

print(get_max_min([1]))


print("{:-^20}".format(" 초깃값 "))
def my_power(num, p=2):
    return num ** p

print(my_power(2, 3))

print("{:-^20}".format(" 효력범위 "))

n = 1
def make_n_10():
    global n

    n = 10
    print(n)

make_n_10()

print(n)





