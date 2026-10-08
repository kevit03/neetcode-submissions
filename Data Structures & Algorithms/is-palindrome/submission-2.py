class Solution:
    def isPalindrome(self, s: str) -> bool:
        S = "".join(c.lower() for c in s if c.isalnum())
        mid = len(S)//2 

        for i in range(0, mid): 
            if S[i] != S[len(S)-i-1]: 
                return False  
        return True  
        