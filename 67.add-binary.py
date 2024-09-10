#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#

# @lc code=start
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # 文字列を整数に変換して足し合わせ、その結果を再び二進数に変換
        # `int(hoge, 2)`で2進数に変換する
        # bin(...)[2:]：整数の和を二進数に変換し、結果の先頭に付く ‘0b’ を取り除いて二進数の文字列を返す
        return bin(int(a, 2) + int(b, 2))[2:]
# @lc code=end

