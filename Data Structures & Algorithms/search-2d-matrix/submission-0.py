class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        r = len(matrix)
        c = len(matrix[0])

        left,right = 0, r*c-1

        while(left<=right):
            mid = left + (right-left)//2
            row = mid // c
            col = mid % c
            val = matrix[row][col]

            if val>target:
                right = mid - 1
            elif val<target:
                left = mid + 1
            else:
                return True
        return False