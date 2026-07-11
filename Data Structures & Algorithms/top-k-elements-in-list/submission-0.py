class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        from collections import Counter
        c1 = Counter(nums)

        keys_only = [ key for key,count in c1.most_common(k)]

        return keys_only
        