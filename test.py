nums = [1,2,3,4,5,6,7]
target = 12

l , r = 0, len(nums) - 1

while l < r:
    s = nums[l] + nums[r]
    if s == target:
        print(l,r)
        break
    elif s < target:
        l += 1
    else:
        r -= 1