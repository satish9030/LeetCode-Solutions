class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        left = 0
        right = 0
        for ch in s:
            if ch == '(':
                left += 1
            if ch == ')':
                if left > 0:
                    left -= 1
                else:
                    right += 1
            
        res = set()
        def track(i, left, right, bal, path):
            if i == len(s):
                if left == 0 and right == 0 and bal == 0:
                    res.add(''.join(path))
                return
                
            ch = s[i]
            if ch == '(':
                if left > 0:
                    track(i + 1, left - 1, right, bal, path)
                path.append(ch)
                track(i + 1, left, right, bal + 1, path)
                path.pop()

            elif ch == ')':
                if right > 0:
                    track(i + 1, left, right - 1, bal, path)
                if bal > 0:
                    path.append(ch)
                    track(i + 1, left, right, bal - 1, path)
                    path.pop()
            
            else:
                path.append(ch)
                track(i + 1, left, right, bal, path)
                path.pop()
            
        
        track(0, left, right, 0, [])
        return list(res
        )