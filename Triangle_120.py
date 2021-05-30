class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        rows = len(triangle)

        P = [0 for i in range(rows)]

       # P[0] = triangle[0]
        for i in range(0,rows):
           #
                if i == 0:
                    P[i] = min(triangle[i])
                else:
                    for j in range(0,len(triangle[i])):
                        P[i] = min(triangle[i]) + P[i-1]

        return P[-1]


   
