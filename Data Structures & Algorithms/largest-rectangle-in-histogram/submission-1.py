class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        area = 0
        stack = deque()
        for i in range(len(heights)):
            if not stack or heights[i] > stack[-1][1]:
                stack.append([i, heights[i]])
            else:
                while stack and stack[-1][1] >= heights[i]:
                    index, height = stack.pop()
                    area = max(area, height*(i - index))
                stack.append([index, heights[i]])
        while stack:
            index, height = stack.pop()
            area = max(area, height*(len(heights) - index))
        return area