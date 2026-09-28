class Solution:
    def maxDepth(self, s: str) -> int:
        depth = 0
        max_dep = 0
        for ch in s:
            if ch == '(':
                depth += 1
                max_dep = max(max_dep,depth)
            elif ch == ')':
                depth -= 1

        return max_dep