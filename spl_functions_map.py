numbers = ['7', '2', '67']
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

# map function should contain the function that is to be applied on all elements of the list
numbers_1 = list(map(int, numbers))
print(numbers_1)

def sq(a):
    return a*a

numbers_2 = list(map(sq, numbers))
print(numbers_2)

