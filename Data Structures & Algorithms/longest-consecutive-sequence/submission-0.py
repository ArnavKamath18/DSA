class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = sorted(list(set(nums)))
        n = len(nums)
        print(nums)

        if n==0:
            return 0

        ans = 1

        i = 0
        while i < n-1:
            j = i+1
            temp = 1
            if j < n and nums[j]==nums[i]+1:
                while j < n and nums[j]==nums[i]+1:
                    temp += 1
                    j += 1
                    i += 1
                ans = max(ans,temp)
                i = j
                continue
            i += 1
    
        return ans