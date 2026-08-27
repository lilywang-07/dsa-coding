class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        result = []
        counts = Counter(nums)
        for key,value in counts.items():
            heapq.heappush(heap, (-value, key))
        for i in range(k):
            freq, el = heapq.heappop(heap)
            result.append(el)
        return result