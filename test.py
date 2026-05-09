nums = [1,2,3,4,5,6,2,1,3,4]
k = 2

window_sum = sum(nums[:k])
max_sum = window_sum

for i in range(k, len(nums)):
    window_sum += nums[i] - nums[i - k]
    max_sum = max(max_sum, window_sum)
print(max_sum)