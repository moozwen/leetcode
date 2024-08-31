#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        rev_x = list(reversed(str_x))
        # sum()はジェネレータを受け取れ、下のコードでは、ジェネレータを渡している。
        # `[1 for a, b in zip(str_x, rev_x) if a == b]`と[]で囲むと、listをsum()に渡す。
        numCorrect = sum(1 for a, b in zip(str_x, rev_x) if a == b)
        return True if len(str_x) == numCorrect else False

# @lc code=end
