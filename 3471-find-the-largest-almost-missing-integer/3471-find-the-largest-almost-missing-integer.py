class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1
        if k == n:
            return max(nums)
        if k == 1:
            ans = -1
            for x in nums:
                if count[x] == 1:
                    ans = max(ans, x)
            return ans
        last = n - 1
        a = nums[0]
        b = nums[last]
        if a == b:
            return -1

        if count[a] == 1 and count[b] == 1:
            return max(a, b)

        if count[a] == 1:
            return a

        if count[b] == 1:
            return b

        return -1