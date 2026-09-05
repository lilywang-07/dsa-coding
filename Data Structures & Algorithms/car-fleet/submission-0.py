class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        array = []
        stack = deque()
        for i in range(len(position)):
            array.append([position[i], speed[i]])
        array.sort(key=lambda x: x[0], reverse=True)

        for pos, speed in array:
            time = (target - pos) / speed
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)