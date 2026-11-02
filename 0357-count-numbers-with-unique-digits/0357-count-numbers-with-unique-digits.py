class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n == 0:
            return 1

        count = 10
        uniq = 9
        avail = 9
        for i in range(2, n + 1):
            uniq *= avail
            count += uniq
            avail -= 1
        return count

        