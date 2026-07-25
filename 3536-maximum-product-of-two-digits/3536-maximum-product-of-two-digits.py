class Solution:
    def maxProduct(self, n: int) -> int:
        lar = 0
        sec = 0
        while n!= 0:
            digit = n%10
            if digit >= lar:
                sec = lar 
                lar = digit
            elif digit > sec:
                sec = digit
            n//=10
        return lar * sec
        
                
                 
        