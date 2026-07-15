class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0

        l = 0
        r = len(heights) - 1
        for i in range(len(heights)):
            curr_area = (r-l) * min(heights[l], heights[r])
            if heights[l] >= heights[r]:
                r -= 1
            else:
                l += 1

            max_area = max(max_area, curr_area)


        return max_area