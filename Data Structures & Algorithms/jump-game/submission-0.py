class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        elif nums[0] == 0:
            return False
        
        max_reach = 0
        for i in range(len(nums)-1):
            if max_reach < i:
                break
            max_reach = max(max_reach, i+nums[i])
            if max_reach >= len(nums)-1:
                return True
        return False