class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]
        begin = True
        # finds intersection of fast & slow
        while begin or slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]
            begin = False

        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return slow