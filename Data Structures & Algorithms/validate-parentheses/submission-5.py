class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) < 2:
            return False
        par = []
        valid = {")":"(", "}":"{", "]":"["}

        for char in s:
            if char not in valid:
                par.append(char)
            else:
                if not par:
                    return False
                if valid[char] != par.pop():
                    return False
        
        if not par:
            return True
        else:
            return False