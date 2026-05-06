class Solution:
    def dutch_flag(self, nums):
        low = 0
        mid = 0
        high = len(nums) - 1

        while mid <= high:
            if nums[mid] == 0:

                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            
            elif mid == 1:
                mid += 1

            else:
                nums[high], nums[mid] = nums[mid], nums[high]
                high -= 1
        
        return nums

nums = [2,1,0,2,1,0]
print(Solution().dutch_flag(nums))