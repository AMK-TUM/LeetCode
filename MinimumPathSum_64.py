class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        P = [[0 for x in range(n)] for y in range(m)]

        P[0][0] = grid[0][0]


        for i in range(m):
            for j in range(n):

                if i == 0 and j!=0:
                    P[i][j] = P[i][j-1] + grid[i][j]

                elif j==0 and i!=0:
                    P[i][j] = P[i-1][j] + grid[i][j]

                elif i!=0 and j!=0:
                    P[i][j] = min(P[i-1][j],P[i][j-1]) + grid[i][j]


        return P[-1][-1]
