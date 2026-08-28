class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        right = [0] * n
        left = [0] * n
        left[0] = nums[0]
        right[n-1] = nums[n-1]
        for i in range(1,n):
            left[i] = left[i-1] * nums[i]
            right[n-i-1] = right[n-i] * nums[n-i-1]

        output = [0] * n
        output[0] = right[1]
        for i in range(1,n-1):
            output[i] = left[i-1] * right[i+1]
        output[n-1] = left[n-2]
        return output