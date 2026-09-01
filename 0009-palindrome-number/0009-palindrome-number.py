class Solution:
    def isPalindrome(self, x: int) -> bool:
        dup = x
        rev = 0
        while x > 0:
            ld = x % 10
            rev = rev*10+ld
            x//=10
        if rev == dup:
            return True
        else:
            return False

        