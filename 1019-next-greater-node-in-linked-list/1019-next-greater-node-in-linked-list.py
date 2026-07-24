# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        n = len(nums)
        ans = [0]*n
        stack = []
        for i in range(n):
            while stack and nums[i]>nums[stack[-1]]:
                ans[stack.pop()]= nums[i]
            stack.append(i)
        return ans
            