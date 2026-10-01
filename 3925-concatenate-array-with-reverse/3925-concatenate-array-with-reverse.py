class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        n = len(nums)
        arr = [0]*2*n
        for i in range(n):
            arr[i] = nums[i]
        for i in range(n):
            arr[n+i] = nums[n-i-1]
        return arr
        