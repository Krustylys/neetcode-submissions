class Solution:
    def trap(self, height: List[int]) -> int:

        # n2
        res = 0
        n = len(height)

        for i in range(n-1):
            
            p1 = height[i]

            for j in range(i):
                p1 = max(height[j],p1)
            
            p2 = height[i]

            for j in range(i+1,n):
                p2 = max(height[j],p2)

            print(p1,p2)
            res += (min(p1,p2) - height[i])

        return res
