class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        s_len = len(s)
        t_len = len(t)

        T = [[0 for i in range(t_len+1)] for j in range(s_len+1)]

        for i in range(1,s_len+1):
            for j in range(1,t_len+1):

                if s[i-1] == t[j-1]:
                    T[i][j] = T[i-1][j-1] + 1

                else:
                    T[i][j] = max(T[i-1][j],T[i][j-1])

        if s_len == T[s_len][t_len]:
            return True
        else:
            return False
