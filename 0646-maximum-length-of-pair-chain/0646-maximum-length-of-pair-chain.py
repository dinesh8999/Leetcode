class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:

        pairs.sort(key=lambda x: x[1])

        count = 1
        current_end = pairs[0][1]

        for left, right in pairs[1:]:

            if current_end < left:
                count += 1
                current_end = right

        return count
        