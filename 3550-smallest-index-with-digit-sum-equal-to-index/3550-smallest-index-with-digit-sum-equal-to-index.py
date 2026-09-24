class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            j = nums[i]
            sum = 0
            while j > 0:
                ld = j % 10
                sum += ld
                j //= 10
            if sum == i:
                return i
        return -1
        