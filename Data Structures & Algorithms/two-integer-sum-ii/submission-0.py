class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        n = len(numbers)
        right = n - 1
        sol = [0, 0]
        while left <= right:
            suma = numbers[left] + numbers[right]
            if suma > target:
                right -= 1
            elif suma < target:
                left += 1
            else:
                sol[0] = left + 1
                sol[1] = right + 1 
                return sol