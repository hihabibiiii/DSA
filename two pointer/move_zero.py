class Solution:
    def move_zero(self, nums):
        if not nums:
            return 0

        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
        return nums

nums = [1,2,312,0,4,0,34,]
print(Solution().move_zero(nums))