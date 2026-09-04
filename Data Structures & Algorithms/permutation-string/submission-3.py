class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counts = [0] * 26
        curr = [0] * 26
        for i in range(len(s1)):
            counts[ord(s1[i]) - ord('a')] += 1
            curr[ord(s2[i]) - ord('a')] += 1
        if curr == counts: # check first substring
            return True
            
        for i in range(len(s2) - len(s1)):
            curr[ord(s2[i]) - ord('a')] -= 1
            curr[ord(s2[i+len(s1)]) - ord('a')] += 1
            if curr == counts:
                return True

        return False