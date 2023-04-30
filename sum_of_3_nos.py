def sum_nos(x,y,z):
    sum = x + y + z
    if x==y==z:
        sum = sum * 3
        return sum
    else:
        return("The nos. are not equal")
print(sum_nos(2,3,5))


    