class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        original_len = len(nums)
        new_len = len(set(nums))

        if(new_len < original_len):
            return True
        else:
            return False