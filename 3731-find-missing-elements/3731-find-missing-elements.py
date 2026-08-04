class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        s = set(nums)
        ans = []
        mini = min(nums)
        maxi = max(nums)
        for i in range(mini + 1, maxi):
            if i not in s:
                ans.append(i)
        return ans
        