class Solution:
    def recoverOrder(self, order: List[int], friends: List[int]) -> List[int]:
        friend_set = set(friends)
        ans = []
        for person in order:
            if person in friend_set:
                ans.append(person)
        return ans
        