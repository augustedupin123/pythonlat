def func1(value):
    return value %2 ==0
iterable = [1,2,3,4,5]
new_list = list(filter(func1, iterable))
print(new_list)

