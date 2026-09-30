class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        arr = [0]*len(seq)
        depth = 0
        for ch in range(len(seq)):
            if seq[ch] == '(':
                depth += 1
                arr[ch] = depth % 2
            elif seq[ch] == ')':
                arr[ch] = depth % 2
                depth -= 1
        return arr
        