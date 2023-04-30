#we can use filter function to filter values from the given sequence based on some condition
#filter(function, sequence)
#map function - For every element given in the sequence apply some funtion and generate new element with the reqd modification
#map(function, sequence)
l = [1,2,3,4,5]
def sq(n):
    return n*n
l1 = list(map(sq,l))
print(l1)


l2 = list(map(lambda n:n%2,l))
print(l2)
