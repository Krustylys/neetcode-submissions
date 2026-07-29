class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        #brute
        longest_substring = []
        for i in range(len(s)):
            cur_substring = []
            for j in range(i,len(s)):
                if s[j] not in cur_substring:
                    cur_substring.append(s[j])
                else:
                    break
            if len(cur_substring) > len(longest_substring):
                longest_substring = cur_substring
        
        return len(longest_substring)
            

        
        