# Higher order function:
# Can take function as input
# Can return function
# A function extender

def squared(value):
    return value ** 2
iterable = [1,2,3,4,5]
new_list = list(map(squared, iterable))
print(new_list)

