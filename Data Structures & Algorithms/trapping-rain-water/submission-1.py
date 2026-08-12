class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        maxl = [0]*n
        maxr = [0]*n

        for i in range(1,n):
            j = -i-1

            maxl[i] = max(maxl[i-1], height[i-1])
            maxr[j] = max(maxr[j+1], height[j+1])
        
        total = 0
        for i in range(n):
            temp = min(maxl[i], maxr[i])-height[i]
            if temp > 0:
                total += temp
        
        return total