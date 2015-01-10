class Solution:
    # @param matrix, a list of lists of integers
    # @param target, an integer
    # @return a boolean
    def searchMatrix(self, matrix, target):
        if len(matrix) ==0:
            return False
        nrow = len(matrix)
        if len(matrix[0])==0:
            return False
        ncol = len(matrix[0])
        row,col = 0,ncol-1
        while row<nrow and col>=0:
            current = matrix[row][col]
            if  current== target:
                return True
            elif current < target:
                row +=1
            else:
                col -= 1
        return False