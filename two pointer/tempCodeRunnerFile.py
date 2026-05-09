class Solution:
    def sumOfThreeNum(self, nums , target):
        nums.sort()
        n = len(nums)
        result = []

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i+1 , n - 1

            while left < right:
                s = nums[i] + nums[left] + nums[right]

                if s == target:
                    result.append([nums[i], nums[left], nums[right]])

                    while left < right and nums[left] == nums[left + 1]:
                        left += 1

                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1

                    left += 1
                    right -= 1

                elif s < target:
                    left += 1
                else:
                    right -= 1
            return result

nums = [-3, -1, 0, 1, 2, 3,]
print(Solution().sumOfThreeNum(nums, 0)) 