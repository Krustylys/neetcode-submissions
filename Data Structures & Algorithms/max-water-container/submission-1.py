class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0

        for i in range(len(heights)):

            for j in range(i+1,len(heights)):
                width = j - i
                curr_height = min(heights[j], heights[i])

                curr_area = curr_height * width


                max_area = max(max_area , curr_area)

        return max_area