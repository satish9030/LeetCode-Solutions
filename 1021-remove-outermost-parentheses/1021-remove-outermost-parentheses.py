class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        stack=[]
        c=0
        for i in s:
            if i=='(':
                if c>0:
                    stack.append(i)
                c+=1
            else:
                c-=1
                if c>0:
                    stack.append(i)
        
        return "".join(stack)