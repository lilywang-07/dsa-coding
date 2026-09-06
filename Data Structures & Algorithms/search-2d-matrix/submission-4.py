class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.findRow(0, len(matrix)-1, matrix, target)

    def findRow(self, l: int, r: int, matrix: List[List[int]], target: int):
        if l > r:
            return False
        if l == r:
            return self.binary(0, len(matrix[0])-1, matrix[l], target)
        mid = (r + l) // 2
        if matrix[mid][0] <= target:
            if matrix[mid][len(matrix[0])-1] >= target:
                return self.findRow(mid, mid, matrix, target)
            else:
                return self.findRow(mid+1, r, matrix, target)
        elif matrix[mid][0] > target:
            return self.findRow(l, mid-1, matrix, target)

    def binary(self, l: int, r: int, matrix: List[int], target: int):
        if r < l:
            return False
        mid = (r+l) // 2
        if matrix[mid] == target:
            return True
        elif matrix[mid] > target:
            return self.binary(l, mid-1, matrix, target)
        else:
            return self.binary(mid+1, r, matrix, target)