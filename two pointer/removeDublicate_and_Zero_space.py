#Find Unique Number With Two Way Pointer


class Solution:
    def uniNum(self, numbers):
        if not numbers:
            return 0, []
        left = 0
        right = 1
        while right < len(numbers):
            if numbers[right] != numbers[left]:
                left += 1
                numbers[left] = numbers[right]
            right += 1
        return left + 1, numbers[:left + 1]

obj = Solution()
nums = [1,1,2,2,3,3,4,4]

print(obj.uniNum(nums))