class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return "****"
        if len(strs)==0:
            return ""
        return "#/".join(strs)

    def decode(self, s: str) -> List[str]:
        if s=="****":
            return []
        if s == "":
            return [""]
        return list(s.split("#/"))
