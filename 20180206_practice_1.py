lst = [21, 42, 23, 14, 5, 66]
lst.sort()
print(lst)

max_num = max(lst)
min_num = min(lst)

lst.remove(max_num)
lst.remove(min_num)

print(lst)

