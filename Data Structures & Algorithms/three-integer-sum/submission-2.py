from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # In-place sort is slightly more efficient
        output = []
        n = len(nums)

        for x in range(n - 2):
            # If the current number is positive, we can't form a zero sum anymore
            if nums[x] > 0:
                break
            
            # Skip duplicate values for the first element to avoid duplicate triplets
            if x > 0 and nums[x] == nums[x - 1]:
                continue

            # Reset pointers for the two-sum part
            y = x + 1
            z = n - 1

            while y < z:
                current_sum = nums[x] + nums[y] + nums[z]

                if current_sum < 0:
                    y += 1
                elif current_sum > 0:
                    z -= 1
                else:
                    output.append([nums[x], nums[y], nums[z]])
                    
                    # Move pointers past any duplicate values to avoid duplicate triplets
                    while y < z and nums[y] == nums[y + 1]:
                        y += 1
                    while y < z and nums[z] == nums[z - 1]:
                        z -= 1
                    
                    # Move both pointers inward for the next potential pair
                    y += 1
                    z -= 1

        return output