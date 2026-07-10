class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict1 = {"{": "}", "[": "]", "(": ")"}
        
        if not s:
            return True
            
        for char in s:
            if char in dict1:
                stack.append(char)
            else:
                if not stack or dict1[stack[-1]] != char:
                    return False
                stack.pop()
        
        return len(stack) == 0