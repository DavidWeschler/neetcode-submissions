class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:      # empty matrix
            return False

        rows = len(matrix)
        cols = len(matrix[0])

        if target > matrix[rows-1][cols-1]:   # if the target is larger than the biggest element
            return False

        # finding the row:
        l, r = 0, rows-1
        rowIndex = None
        while l <= r:
            middle = (l+r)//2
            if matrix[middle][cols-1] == target:
                return True
            elif matrix[middle][cols-1] > target:
                if middle == 0 or matrix[middle-1][cols-1] < target:
                    rowIndex = middle
                    break
                else:
                    r = middle - 1
            else:
                l = middle + 1
        
        return self.search(matrix[rowIndex], target) != -1


    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)-1

        while True:
            # middle = (l + r) // 2
            middle = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                r = middle - 1
            else:
                l = middle + 1
            if l > r:
                return -1