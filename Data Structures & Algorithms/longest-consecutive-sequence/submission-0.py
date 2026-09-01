class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        start = {}
        result = 0
        for num in nums:
            if num-1 not in nums_set:
                length = 0
                while num + length in nums_set:
                    length += 1
                result = max(length, result)
        return result

            