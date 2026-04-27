#Find Unique Number 

class Solution:
    def uniNum(self, numbers):
        if not numbers:
            return 0, []
        officer = 0
        cm = 1
        while cm < len(numbers):
            if numbers[cm] != numbers[officer]:
                officer += 1
                numbers[officer] = numbers[cm]
            cm += 1
        return officer + 1, numbers[:officer + 1]

obj = Solution()
nums = [1,1,2,2,3,3,4,4,5,5,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,9,9,9,9,9,9]

print(obj.uniNum(nums))
