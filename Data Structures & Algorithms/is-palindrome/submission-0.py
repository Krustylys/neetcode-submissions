class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        extract = ""

        for i in range(len(s)):
            if s[i].isalnum():
                extract += s[i].lower()

        i = 0
        j = len(extract) - 1

        while(i < j):
            if extract[i] != extract[j]:
                return False
            i += 1
            j -= 1
        
        return True
        