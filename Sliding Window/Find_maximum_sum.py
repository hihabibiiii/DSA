class Solution:
    def max_sum(self, nums, k):
        n = len(nums)
        if n < k:
            return 0
        
        window_sum = sum(nums[:k])
        max_sum = window_sum
        
        for i in range(k, n):
            window_sum += nums[i] - nums[i - k]
            max_sum = max(max_sum, window_sum)
        
        return max_sum
    
nums = [1,2,3,4,5,6,2,1,3,4]
print(Solution().max_sum(nums, 2))