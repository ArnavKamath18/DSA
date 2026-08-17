class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxs = 0
        n = len(s)
        seen = set()
        l = 0
        
        for r in range(n):
            while s[r] in seen:
                seen.remove(s[l])
                l += 1
            
            seen.add(s[r])
            maxs = max(maxs, r-l+1)
                
        return maxs