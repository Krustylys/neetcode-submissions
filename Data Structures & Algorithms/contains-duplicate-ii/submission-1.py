class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        #hash table

        hash = {}

        for key,val in enumerate(nums):   
            if val in hash:
                hash[val] = abs(hash[val] - key)
                if hash[val] <= k:
                    return True
            else:
                hash[val] = key

        

        return False