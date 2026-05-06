class Solution:
    def remove_duplicete(self, nums):
        if not nums:
            return 0

        slow = 0

        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow += 1
                nums[slow] = nums[fast]
        
        return slow + 1
    
nums = [1,2,3,2,1,3]
nums.sort()
print(Solution().remove_duplicete(nums))