myList1 = [23,345,346,567,235,3457637]

size = len(myList1)
temp = myList1[0]
myList1[0] = myList1[size - 1]
myList1[size -1] = temp
print('list after swapping', myList1)


# myList1[0],myList1[-1] = myList1[-1], myList1[0]




