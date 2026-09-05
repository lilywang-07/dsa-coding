class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        m = len(t)
        if n < m:
            return ''
        remaining = m
        curr = defaultdict(int)
        length = float('inf')
        start = 0
        left = 0

        for char in t:
            curr[char] += 1

        for right in range(n):
            if s[right] in curr:
                if curr[s[right]] > 0:
                    remaining -= 1
                curr[s[right]] -= 1
            while remaining == 0 and left <= right:
                if right - left + 1 < length:
                    start = left
                    length = right - left + 1
                if s[left] in curr:
                    curr[s[left]] += 1
                    if curr[s[left]] > 0:
                        remaining += 1
                left += 1

        if length == float('inf'):
            return ''
        else:
            return s[start:start + length]