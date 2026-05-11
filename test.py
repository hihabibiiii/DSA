class Solution:
    def TwoSum(self, nums, target):
        n = len(nums)
        left, right = 0, n - 1
        
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return (f" Array Number is {nums[left]} and Index Is {left} And Second Array Number is {nums[right]} and Index Is {right}")
            elif s < target:
                left += 1
            else:
                right -= 1
        return left
    
nums = [2, 7, 11, 15]
print(Solution().TwoSum(nums, 9))