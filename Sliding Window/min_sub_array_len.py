class Solution:
    def minSubArrayLen(self, target:int, nums:list[int]) -> int:
        n = len(nums)
        left = 0
        window_sum = 0
        min_sum = float('inf')
        
        for right in range(n):
            window_sum += nums[right]
            
            while window_sum >= target:
                min_sum = min(min_sum, right - left + 1)
                window_sum -= nums[left]
                left += 1
        return 0 if min_sum == float('inf') else min_sum

nums = [1,2,3,4,5,6,7,8]
target = 11
print(Solution().minSubArrayLen(target, nums))