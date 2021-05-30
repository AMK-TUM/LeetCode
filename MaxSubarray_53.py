class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        length = len(nums)
        num = [nums[0] for i in range(length+1)]

        for i in range(1,length):
            num[i] = max(nums[i], nums[i]+num[i-1])

        return max(num)
