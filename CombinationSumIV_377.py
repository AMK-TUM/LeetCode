class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        A = [0 for i in range(target+1)]

        A[0] = 1

        for i in range(target+1):
            for j in nums:
                if (i-j) >= 0:
                    A[i] += A[i-j]

        return A[-1]

        
