class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        array = sorted(nums)
        result = []
        print(array)
        for i in range(len(nums)):
            target = -array[i]
            left = 0
            right = len(nums) - 1
            while left < right:
                if left == i or array[left] + array[right] < target:
                    left += 1
                elif right == i or array[left] + array[right] > target:
                    right -= 1
                else:
                    curr = sorted([array[left], array[right], array[i]])
                    if curr not in result:
                        result.append(curr)
                    left += 1
        return result