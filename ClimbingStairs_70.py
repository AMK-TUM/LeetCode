class Solution:
    def climbStairs(self, n: int) -> int:

        # This is a combinatoric problem.
        # It can be solved with the help of dynamic programming as it has got optimal substructure and overlapping subproblem.

        # base problem
        F = [0 for i in range(n+1)]

        F[0] = 1
        F[1] = 1

        # Recurrence relation
        for i in range(2,n+1):
            F[i] = F[i-1] + F[i-2]

        return F[n]
