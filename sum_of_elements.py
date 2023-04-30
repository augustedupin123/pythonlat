num = int(input("How many numbers?"))
lst = []
for n in range(num):
    numbers = int(input("enter a number"))
    lst.append(numbers)
print("the sum of them is:", sum(lst))