class Solution:
    def smallestPalindrome(self, s: str) -> str:
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-ord('a')]+=1
        first = ""
        middle = ""
        for i in range(26):
            if freq[i]%2==1:
                middle = chr(i + ord('a'))
            for j in range(freq[i] // 2):
                first += chr(i + ord('a'))
        return first + middle + first[:: -1]
        