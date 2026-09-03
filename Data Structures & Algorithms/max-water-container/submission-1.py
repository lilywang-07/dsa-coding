class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left = 0
        right = n - 1
        result = 0

        while left < right:
            amount = min(heights[left], heights[right]) * (right - left)
            result = max(result, amount)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return result