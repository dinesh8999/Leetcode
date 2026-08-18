class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        candidate1 = None
        candidate2 = None
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == candidate1:
                cnt1 += 1
            elif num == candidate2:
                cnt2 += 1
            elif cnt1 == 0:
                candidate1 = num
                cnt1 = 1
            elif cnt2 == 0:
                candidate2 = num
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
        cnt1 = 0
        cnt2 = 0
        for num in nums:
            if num == candidate1:

                cnt1 += 1
            elif num == candidate2:
                cnt2 += 1
        result = []
        if cnt1 > len(nums) // 3:
            result.append(candidate1)
        if cnt2 > len(nums)//3:
            result.append(candidate2)
        return result
    
            

            



        