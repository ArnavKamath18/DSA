class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)

        for i in range(n):
            temp = 0
            for j in range(i+1,n):
                temp = max(temp,prices[j]-prices[i])
            ans = max(ans,temp)
        
        return ans