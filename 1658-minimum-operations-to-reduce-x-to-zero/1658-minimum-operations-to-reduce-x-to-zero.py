class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
    
        target = total - x

        if target < 0:
            return -1

        if target == 0:
            return n

        left = 0
        win_sum = 0
        max_length = -1

        for j in range(n):
            win_sum += nums[j]
            while win_sum > target:
                win_sum -= nums[left] 
                left += 1
            if win_sum == target:
                max_length = max(max_length, j-left+1)
        if max_length == -1:
            return -1
        else:
            return n-max_length


        