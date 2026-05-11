class Solution:
    def totalfruit(self, fruits: list[int]) -> int:
        left = 0
        freq = {}
        max_len = 0

        for right in range(len(fruits)):
            fruit = fruits[right]

            freq[fruit] = freq.get(fruit, 0) + 1

            while len(freq) > 2:
                freq[fruits[left]] -= 1

                if freq[fruits[left]] == 0:
                    del freq[fruits[left]]

                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
    
nums = [1,1,2,2,3,3,4,4,5,5,6,6,7,8]
print(Solution().totalfruit(nums))