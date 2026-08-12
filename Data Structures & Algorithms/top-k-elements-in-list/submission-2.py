from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        vals = []
        for key, value in c.items():
            vals.append((value, key))

        vals = sorted(vals,reverse=True)
        
        ans = []

        for i in range(k):
            ans.append(vals[i][1])
        
        return ans