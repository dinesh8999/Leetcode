class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ans = []
        i = 0
        for num in range(1, target[-1] + 1):
            if num == target[i]:
                ans.append("Push")
                i += 1
            else:
                ans.append("Push")
                ans.append("Pop")
        return ans
        