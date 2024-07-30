class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        LEFT_BOUND, RIGHT_BOUND = len(s), len(t)

        left, right = 0, 0
        while left < LEFT_BOUND and right < RIGHT_BOUND:
            if s[left] == t[right]:
                left += 1
            right += 1
        return left == LEFT_BOUND

        #T = O(|t|) S = O(1)