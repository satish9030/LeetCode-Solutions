class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        d={}
        for i in magazine:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        for j in ransomNote:
            if j not in d or d[j]==0:
                    return False
            else:
                    d[j]-=1
        return True
        