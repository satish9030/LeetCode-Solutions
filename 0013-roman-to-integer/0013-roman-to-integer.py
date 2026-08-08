class Solution:
    def romanToInt(self, s: str) -> int:
        d = {
            'I': 1, 'V': 5, 'X': 10,
            'L': 50, 'C': 100,
            'D': 500, 'M': 1000
        }
        sum=0
        prev=0
        for i in reversed(s):
            v=d[i]
            if v<prev:
                sum-=v
            else:
                sum+=v
                prev=v
        return sum

        


