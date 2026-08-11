class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        
        for string in strs:
            anagram = str(sorted(string))
            if anagram in anagrams:
                anagrams[anagram].append(string)
            else:
                anagrams[anagram] = [string]
        
        return list(anagrams.values())