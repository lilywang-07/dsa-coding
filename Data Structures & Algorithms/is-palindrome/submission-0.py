class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ''.join(filter(str.isalnum, s))
        string = string.lower()
        for i in range(len(string)):
            if string[i] != string[len(string)-i-1]:
                return False
        return True