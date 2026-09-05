class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.mins or val < self.mins[-1]:
            self.mins.append(val)
        else:
            self.mins.append(self.mins[-1])

    def pop(self) -> None:
        self.stack.pop()
        self.mins.pop()

    def top(self) -> int:
        temp = self.stack.pop()
        self.stack.append(temp)
        return temp

    def getMin(self) -> int:
        temp = self.mins.pop()
        self.mins.append(temp)
        return temp