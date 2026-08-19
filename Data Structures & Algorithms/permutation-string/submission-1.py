class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        sub = sorted(s1)

        for i in range(0,n2-n1+1):
            if sorted(s2[i:i+n1])==sub:
                return True
        
        return False