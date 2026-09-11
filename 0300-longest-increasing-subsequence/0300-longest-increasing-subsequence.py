from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums):
        tails = []

        for num in nums:
            index = bisect_left(tails, num)

            if index == len(tails):
                tails.append(num)
            else:
                tails[index] = num

        return len(tails)