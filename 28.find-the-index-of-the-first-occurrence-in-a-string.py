#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        needle_size = len(needle)
        haystack_size = len(haystack)

        if needle_size > haystack_size:
            return -1

        # ループの範囲を調整して、needleの長さを超えて範囲外にアクセスしないようにする
        for i in range(haystack_size - needle_size + 1):
            if haystack[i:i + needle_size] == needle:
                return i
        
        return -1

# @lc code=end

