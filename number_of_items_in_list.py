def list_count(nums):
    count = 0
    for num in nums:
        if num == 4:
            count = count + 1
    return count
print(list_count([1,2,3,4]))
        