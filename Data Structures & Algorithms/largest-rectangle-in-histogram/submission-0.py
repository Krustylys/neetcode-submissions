class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        
        ma = 0
        heights.append(0)
        for i in range(len(heights)):

            while stack and heights[i] < heights[stack[-1]]:

                he = heights[stack.pop()]

                if not stack:
                    w = i
                else:
                    w = i - stack[-1] - 1

                
                ma = max(ma, he*w)
            stack.append(i)
        
        return ma