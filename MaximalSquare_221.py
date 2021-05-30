class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:


        m = len(matrix)    # 3 rows in your example
        n = len(matrix[0]) # 2 columns in your example

        T = [[0 for i in range(n+1)] for j in range(m+1)]

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    T[i+1][j+1] = 1 + min(T[i][j+1], T[i+1][j], T[i][j])

        length = max(max(x) for x in T)


        return length*length
