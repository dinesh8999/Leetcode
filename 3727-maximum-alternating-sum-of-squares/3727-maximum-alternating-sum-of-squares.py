class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        n = len(nums)
        nums = sorted(x*x for x in nums)
        ans = 0
        for i in range(n // 2):
            ans -= nums[i]
        for i in range(n // 2, n):
            ans += nums[i] 
        return ans

        