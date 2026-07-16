class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nxt_grtr = {}
        for i in nums2:
            while stack and i > stack[-1]:
                top = stack.pop()
                nxt_grtr[top] = i
            stack.append(i)
        while stack:
            top = stack.pop()
            nxt_grtr[top] = -1
        ans = []
        for i in nums1:
            ans.append(nxt_grtr[i])
        return ans
        