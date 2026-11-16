class Solution:
    def bestClosingTime(self, customers: str) -> int:
        curr, penalty = 0, 0
        hour = 0
        for i in range(len(customers)):
            if customers[i] == "Y":
                curr -= 1
            else:
                curr += 1
            if curr < penalty:
                penalty = curr
                hour = i + 1
        return hour