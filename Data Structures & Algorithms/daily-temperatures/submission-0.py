class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = deque()
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                index = stack.pop()[1]
                answer[index] = i - index
            stack.append([temperatures[i], i])
        return answer
