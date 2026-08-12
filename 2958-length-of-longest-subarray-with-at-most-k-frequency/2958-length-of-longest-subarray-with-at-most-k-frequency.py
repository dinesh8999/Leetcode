class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        freq = {}
        left = 0
        max_len = 0
        for right in range(len(nums)):
            i = nums[right]
            freq[i] = freq.get(i,0)+1
            while freq[i] > k:
                freq[nums[left]] -= 1
                left += 1
            max_len = max(max_len, right-left+1)
        return max_len
        