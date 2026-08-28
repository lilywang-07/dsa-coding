class Solution:

    def encode(self, strs: List[str]) -> str:
        code = ''
        for s in strs:
            code = code + str(len(s)) + '#' + s
        return code

    def decode(self, s: str) -> List[str]:
        i = 0
        start = 0
        result = []
        while i < len(s):
            while s[i:i+1] != '#':
                i += 1
            num = int(s[start:i])
            result.append(s[i+1:i+num+1])
            i += num + 1
            start = i
        return result