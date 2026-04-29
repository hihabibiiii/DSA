from typing import List

class Solution:
    def sortedArray(self, nums:List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n

        left, right = 0 , n-1
        index = n -1 

        while left <= right:
            if abs(nums[left]) < abs(nums[right]):
                res[index] = nums[left] ** 2
                left += 1
            else:
                res[index] = nums[right] ** 2
                right -= 1

            index -= 1
        return res

nums = [-4, -1, 0, 3, 10]
print(Solution().sortedArray(nums))