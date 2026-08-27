class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = defaultdict(int)
        for letter in s:
            letters[letter] += 1
        for letter in t:
            letters[letter] -= 1

        if max(letters.values()) == 0 and min(letters.values()) == 0:
            return True
        return False