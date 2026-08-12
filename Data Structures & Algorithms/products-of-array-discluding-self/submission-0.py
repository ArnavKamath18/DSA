class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pl = [1]*n
        pr = [1]*n

        for i in range(1,n):
            j = -i-1
            pl[i] = pl[i-1]*nums[i-1]
            pr[j] = pr[j+1]*nums[j+1]
        
        ans = [0]*n
        for i in range(n):
            ans[i] = pl[i]*pr[i]
        
        return ans