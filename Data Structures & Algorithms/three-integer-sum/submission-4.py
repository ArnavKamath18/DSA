class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        if n < 3:
            return []
        if n==3:
            if sum(nums)==0:
                return [nums]
            else:
                return []
        ans = []

        i = 0
        while i < n:
            if nums[i] > 0:
                return ans
            j = i+1
            k = n-1
            while j < k:
                summ = nums[i]+nums[j]+nums[k]
                if summ == 0:
                    if sorted([nums[i], nums[j], nums[k]]) not in ans:
                        ans.append(sorted([nums[i], nums[j], nums[k]]))
                    j += 1
                elif summ > 0:
                    k -= 1
                else:
                    j += 1
                
            i += 1
            
        return ans