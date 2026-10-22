class Solution:
    def reverseVowels(self, s: str) -> str:
        arr = list(s)
        left = 0
        right = len(arr)-1
        vowel = "aeiouAEIOU"
        while left < right:
            if arr[left] not in vowel:
                left += 1
            elif arr[right] not in vowel:
                right -= 1
            else:
                arr[left],arr[right] = arr[right],arr[left]
                left += 1
                right -= 1
        return "".join(arr)
            
        