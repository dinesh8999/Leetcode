
class Solution:
    def triangularSum(self, nums):
        
        while len(nums) > 1:
            
            newNums = []

            for i in range(len(nums) - 1):
                value = (nums[i] + nums[i + 1]) % 10
                newNums.append(value)

            nums = newNums

        return nums[0]
