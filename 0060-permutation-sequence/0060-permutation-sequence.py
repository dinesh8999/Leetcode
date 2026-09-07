class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = []

        for i in range(1, n + 1):
            numbers.append(i)

        fact = 1

        for i in range(1, n):
            fact *= i

        k -= 1
        ans = ""

        while len(numbers) > 0:
            index = k // fact
            ans += str(numbers[index])
            numbers.pop(index)

            if len(numbers) == 0:
                break

            k = k % fact
            fact = fact // len(numbers)

        return ans