class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        T = [[0 for j in range(n)] for i in range(m)]


        for i in range(m):
            for j in range(n):

                if i == 0 and j == 0:
                    T[i][j] = 1

                elif i == 0 and j>0:
                    T[i][j] = T[i][j-1]

                elif i>0 and j==0:
                    T[i][j] = T[i-1][j]

                else:
                    T[i][j] = T[i-1][j] + T[i][j-1]

        return T[-1][-1]

        
