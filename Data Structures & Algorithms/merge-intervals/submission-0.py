class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = []

        # check adjacent
        start = intervals[0][0]
        end = intervals[0][1]
        i = 1
        while i < len(intervals):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            # if touching, then merge
            if curr_start <= end:
                end = max(curr_end, end)
            # add previous to list
            else:
                result.append([start, end])
                start = curr_start
                end = curr_end
            i += 1
        result.append([start, end])
        return result