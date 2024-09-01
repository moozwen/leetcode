#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        min_length = min(len(s) for s in strs)

        for i in range(min_length):
            char = strs[0][i]
            for s in strs:
                if s[i] != char:
                    return strs[0][:i]
        
        return strs[0][:min_length]
        
# @lc code=end

