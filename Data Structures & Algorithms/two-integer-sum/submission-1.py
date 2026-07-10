class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        #hash - map
        hash = {}

        for i,n in enumerate(nums):
            hash[n] = i
        

        for i,n in enumerate(nums):
            s_no = target - n
            
            if s_no in hash and hash[s_no] != i:
                return [i, hash[s_no]]
            
        return []

