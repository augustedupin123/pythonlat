# Same output for same input , every time
# Never mutates/access any variable outside the function

iterable = [1,2,3,4]
def function_iterable(iterable):
    iterable.append('mutation')

def actual_pure_function(iterable):
    new_list = iterable[:]
    new_list.append('mutation')
    return new_list

