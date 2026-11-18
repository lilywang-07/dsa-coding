class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # right to left, find decrease
        i = n - 2
        while i >= 0:
            if nums[i] >= nums[i+1]:
                i -= 1
            else:
                break

        # swap with farthest right
        if i >= 0:
            j = n - 1
            while j >= 0:
                if nums[j] <= nums[i]:
                    j -= 1
                else:
                    break
            nums[j], nums[i] = nums[i], nums[j]

        # reverse right side
        nums[i+1:] = reversed(nums[i+1:])