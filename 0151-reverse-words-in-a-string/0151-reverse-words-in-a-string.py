class Solution:
    def reverseWords(self, s: str) -> str:
        res=""
        m=[]
        for i in s:
            if i!=" ":
                res+=i
            elif res:
                m.append(res)
                res=""
        if res:
            m.append(res)
            res=""
        for j in range(len(m)-1,-1,-1):
            res+=m[j]
            if j!=0:
                res+=" "
        return res
        
        
        