def max_subarray(array):
    max_so_far = max_now = array[0]
    print("max_so_far: " + str(max_so_far))
    print("array length: " ,len(array))
    for i in range(1, len(array)):
        max_now = max(array[i], max_now + array[i])
        max_so_far = max(max_so_far, max_now)
    return max_so_far

a = [-2,1,-3,4,-1,2,1,-5,4]
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

print(a)
print(max_subarray(a))
