def compare(x, y):
    return (x+y) > (y+x)

def largest_number(nums):
    nums = [str(i) for i in nums]

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if not compare(nums[i], nums[j]):
                nums[i], nums[j] = nums[j], nums[i]

    result = ''.join(nums)
    return result

print(largest_number([3, 30, 34, 5, 9]))
