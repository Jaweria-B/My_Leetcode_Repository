class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        arr=[]
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    arr.append([i,j])
                
        for k,l in arr:
            for row in range(n):
                matrix[k][row]=0
            for col in range(m):
                matrix[col][l]=0