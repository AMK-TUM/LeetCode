class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)    # 3 rows in your example
        n = len(obstacleGrid[0]) # 2 columns in your example

        T = [[0 for j in range(n)] for i in range(m)]


        for i in range(m):
            for j in range(n):

                if obstacleGrid[i][j] != 1:
                    if i == 0 and j == 0:
                        T[i][j] = 1

                    elif i == 0 and j>0:
                        T[i][j] = T[i][j-1]

                    elif i>0 and j==0:
                        T[i][j] = T[i-1][j]

                    else:
                        T[i][j] = T[i-1][j] + T[i][j-1]

        return T[-1][-1]
        
