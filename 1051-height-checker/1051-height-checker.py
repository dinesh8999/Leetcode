class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        ans = sorted(heights)
        count = 0
        for i in range(len(heights)):
            if heights[i] != ans[i]:
                count += 1
        return count
        