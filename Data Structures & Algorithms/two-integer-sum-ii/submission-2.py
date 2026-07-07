class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        left = 0
        right = n -1 
        for i in range(n):
            m = ((right - left) // 2)
            summ = numbers[left] + numbers[right]
            if summ == target:
                return [left + 1, right + 1]
            elif summ < target:
                left +=1 
            else:
                right -=1
        