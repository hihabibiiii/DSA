class Solution:
    def reverse_array(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
        
        return nums
    
nums = [1,2,3,4,5]
print(Solution().reverse_array(nums))