class Solution:
    def fruitInBasket(self, fruits:list[int]) -> int:
        n = len(fruits)
        left = 0
        max_len = 0
        freq = {}
        
        for right in range(n):
            fruit = fruits[right]
            freq[fruits] = freq.get(fruit,0) + 1
            
            while len(freq) > 2:
                freq[fruits[left]] -= 1
                if freq[fruit[left]] == 0:
                    del freq[fruit[left]]
                left += 1

            max_len = max(max_len, right - left + 1)
        
        return max_len
    
nums = [1,2,3,4,5]
print(Solution().fruitInBasket(nums))