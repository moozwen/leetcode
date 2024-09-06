#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#

# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 指定した値 val に等しくない要素のみを新しいリストとして返す
        filtered_nums = [num for num in nums if num != val]
        # リストの最初の部分にフィルタリングされた要素を再代入する
        # ジャッジでは、numsの先頭要素しか確認しない。
        # そのため、関数型のアプローチを取るべく、numsの書き換えではなく、numsの先頭への再代入を行う
        nums[:len(filtered_nums)] = filtered_nums
        return len(filtered_nums)
# @lc code=end

