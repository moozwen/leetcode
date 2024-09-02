#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        # stack = []
        # open_brackets = '({['
        # close_brackets = ')}]'

        # for char in s:
        #     if char in open_brackets:
        #         stack.append(char)
        #     else:
        #         # スタックが空の場合、対応する開く括弧がないので無効
        #         if not stack:
        #             return False
                
        #         top_element = stack.pop()
        #         if open_brackets.index(top_element) != close_brackets.index(char):
        #             return False
        
        # return not stack

        stack = []
        # 閉じカッコをキーにしておく。
        # 閉じカッコが現れてから、スタックを探しにいく。
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }

        for char in s:
            if char in bracket_map:
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                stack.append(char)

        return not stack
        
        
# @lc code=end

