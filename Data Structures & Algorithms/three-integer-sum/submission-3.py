class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        array = sorted(nums)
        result = []
        for i in range(len(array)):
            if i > 0 and array[i] == array[i-1]: # checks duplicates
                continue
            target = -array[i]
            left = 1 + i
            right = len(array) - 1
            while left < right:
                if array[left] + array[right] < target:
                    left += 1
                elif array[left] + array[right] > target:
                    right -= 1
                else:
                    result.append([array[left], array[right], array[i]])
                    left += 1 # advance to next
                    right -= 1

                    # checks duplicates
                    while left < right and array[left] == array[left - 1]:
                        left += 1
                    while left < right and array[right] == array[right + 1]:
                        right -= 1
        return result