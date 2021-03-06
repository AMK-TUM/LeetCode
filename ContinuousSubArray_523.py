class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        s=0
        d={0:-1}
        for i in range(len(nums)):
            s=s+nums[i]
            if k!=0:
                s=s%k
            if s in d:
                if i-d[s]>=2:
                    return True
            else:
                d[s]=i
        return False
