class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i in range(len(nums)):
            diff[target - nums[i]] = i
        for j in range(len(nums)):
            if nums[j] in diff and diff[nums[j]] != j:
                return [j, diff[nums[j]]]