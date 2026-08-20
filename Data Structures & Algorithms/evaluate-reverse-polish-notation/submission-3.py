class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numstk = []

        for token in tokens:
            if token=="+":
                a = numstk.pop()
                b = numstk.pop()
                numstk.append(a+b)
            elif token=="*":
                a = numstk.pop()
                b = numstk.pop()
                numstk.append(a*b)
            elif token=="-":
                b = numstk.pop()
                a = numstk.pop()
                numstk.append(a-b)
            elif token=="/":
                b = numstk.pop()
                a = numstk.pop()
                numstk.append(int(a/b))
            else:
                numstk.append(int(token))
        
        return numstk[-1]