class Solution:
    def partition(self, s: str) -> List[List[str]]:
        r = []
        def backtrack(start, current):
            if start == len(s):
                r.append(current[:])
                return
            for end in range(start, len(s)):
                m = s[start:end + 1]
                if m == m[::-1]:
                    current.append(m)
                    backtrack(end + 1, current)
                    current.pop()
        backtrack(0, [])
        return r