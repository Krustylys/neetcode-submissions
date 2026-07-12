class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #compute prefix

        prefix_arr = []
        output = [0] * len(nums)
        y = 1
        prefix_arr.append(nums[0])
        for i in range(1,len(nums)):
            y *= nums[i]
            prefix_arr.append(prefix_arr[i-1] * nums[i])
        
        output[0] = y
        x = 1
        for i in range(len(nums)-1, 0, -1):
            output[i] = prefix_arr[i-1] * x
            x *= nums[i]
        
        return output