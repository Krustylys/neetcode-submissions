class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:

        dictionary = {}
        
        for i in nums:
            if i not in dictionary:
                dictionary.update({i:1})
            else:
                dictionary[i]+=1
        
        print(dictionary)
        
        for _,val in dictionary.items():
            if val > 1:
                return True
        
        return False