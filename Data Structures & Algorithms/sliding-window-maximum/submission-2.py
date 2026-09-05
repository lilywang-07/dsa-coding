class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = [-float('inf')] * (len(nums) - k + 1)
        left = 0
        pq = []
        for i in range(k-1):
            heapq.heappush(pq, [-nums[i], i])

        for window in range(len(nums) - k + 1):
            right = window + k - 1
            heapq.heappush(pq, [-nums[right], right])
            while pq:
                curr = heapq.heappop(pq)
                if curr[1] >= left and curr[1] <= right:
                    result[window] = -curr[0]
                    if curr[1] > left:
                        heapq.heappush(pq, curr)
                    break
            left += 1
        return result
