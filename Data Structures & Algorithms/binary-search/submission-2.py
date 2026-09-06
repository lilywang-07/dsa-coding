class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary(0, len(nums)-1, nums, target)

    def binary(self, l: int, r: int, nums: List[int], target: int) -> int:
        if l > r:
            return -1
        mid = (l+r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.binary(l, mid-1, nums, target)
        elif nums[mid] < target:
            return self.binary(mid+1, r, nums, target)