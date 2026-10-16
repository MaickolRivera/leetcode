class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        result = ""
        
        for i in s:
            if not i.isalnum():
                continue
            result += i
        return result[::-1] == result