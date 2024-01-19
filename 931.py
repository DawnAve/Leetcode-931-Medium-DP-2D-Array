class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        # Length of the list
        n = len(matrix)
        if n == 1:
            return matrix[0][0]

        # Remember to set up the matrix in this way!!!!!!!!!!
        num = [[0 for _ in range(n)] for _ in range(n)]
        num[0] = matrix[0].copy()
        for i in range(1,n):
            for j in range(0,n):
                if j > 0 and j < n-1 :
                    num[i][j] = matrix[i][j] + min(num[i-1][j-1], num[i-1][j], num[i-1][j+1])
                elif j == 0:
                    num[i][j] = matrix[i][j] + min(num[i-1][j], num[i-1][j+1])
                elif j == n-1:
                    num[i][j] = matrix[i][j] + min(num[i-1][j-1], num[i-1][j])
        return min(num[n-1])
