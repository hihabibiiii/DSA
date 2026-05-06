# Find Sum Of Two Number With Two Pointer


class soluation:
    def TwoNumSum(self, number, target):
        i,j = 0, len(number) - 1

        while i < j:
            s = number[i] + number[j]
            if s == target:
                return (f" Array Number is {number[i]} and Index Is {i} And Second Array Number is {number[j]} and Index Is {j}")
            elif s < target:
                i += 1
            else:
                j -= 1

obj = soluation()
nums = [2,3,4,5,6,7,8,9]
target = 5
result = obj.TwoNumSum(nums, target)
print(result)
