class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        ans = 1
        counts = [0]*26
        l, r = 0,0

        for r in range(n):
            counts[ord(s[r])-65] += 1
            while (r-l+1)-max(counts) > k:
                counts[ord(s[l])-65] -= 1
                l +=1
            ans = max(ans,r-l+1)
        
        return ans