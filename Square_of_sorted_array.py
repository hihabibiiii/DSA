# Problem: Squares of a Sorted Array

# Statement:

# You are given an integer array nums sorted in non-decreasing (ascending) order.

# Your task:

# Return a new array containing the square of each number
# The result array must also be sorted in non-decreasing order
# 🧾 Example 1
# Input:  nums = [-4, -1, 0, 3, 10]
# Output: [0, 1, 9, 16, 100]
# 🧾 Example 2
# Input:  nums = [-7, -3, 2, 3, 11]
# Output: [4, 9, 9, 49, 121]
# ⚠️ Constraints
# 1 <= len(nums) <= 10^5
# -10^4 <= nums[i] <= 10^4
# nums is already sorted
# 🎯 Requirement
# Solve in O(n) time
# Avoid using built-in sorting (that gives O(n log n), not optimal)

from typing import List

class Solution:
    def SortedArray(self, nums: List[int]) -> List[int]:

        pos = []
        neg = []

        # Separate negative and positive

        for num in nums:
            if num < 0:
                neg.append(num)
            else:
                pos.append(num)

        #Case 1: No Negative Number 

        if len(neg) == 0:
            return [x * x for x in pos]
        
        #case 2: No Positive Number

        if len(pos) == 0:
            return [x * x for x in neg][::-1]
        
        #Case 3 Both Exist

        neg = [x * x for x in neg][::-1]
        pos = [x * x for x in pos]

        i = j = 0
        res = []

        while i < len(neg) and j < len(pos):
            if neg[i] <= pos[j]:
                res.append(neg[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1
        
        while i < len(neg):
            res.append(neg[i])
            i += 1
        
        while j < len(pos):
            res.append(pos[j])
            j += 1
        return res
    
    
nums = [-4, -1, 0, 3, 10]
obj = Solution()
result = obj.SortedArray(nums)
print(result)