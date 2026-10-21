class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxi=float("-inf")
        total=0
        for i in range(0,len(nums)):
            total=total+nums[i]
            maxi=max(total,maxi)
            if total<0:
                total=0
        return maxi

        