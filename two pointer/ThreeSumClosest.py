class Solution:
    def ThreeSumClosest(self, nums, target):
        nums.sort()
        if not nums:
            return []
        n = len(nums)
        closest = nums[0] + nums[1] + nums[2]
        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
        
            
            left , right = i + 1, n - 1
            
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if abs(target - s) < abs(target - closest):
                    closest = s
                if s == target:
                    return s
                
                elif s < target:
                    left += 1
                     
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                
                else:
                    right -=1
                    while right > left and nums[right] == nums[right + 1]:
                        right -= 1
                        
        return closest
    
nums = [1, 1, 1, 2, 2, 3, -1]

print(Solution().ThreeSumClosest(nums, 5))