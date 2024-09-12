#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # メモ化用の辞書
        memo = {}
        
        # 再帰関数を定義
        def climb(k: int) -> int:
            # すでに計算した値がある場合、メモから取得
            if k in memo:
                return memo[k]
            
            # ベースケース
            if k == 0 or k == 1:
                return 1
            
            # 再帰ステップ
            memo[k] = climb(k - 1) + climb(k - 2)
            return memo[k]
        
        return climb(n)
# @lc code=end

