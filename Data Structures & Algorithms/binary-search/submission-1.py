class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        mid = len(nums) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return self.search(nums[0:mid], target)
        elif nums[mid] < target:
            answer = self.search(nums[mid+1:], target)
            if answer == -1:
                return -1
            else:
                return answer + mid + 1