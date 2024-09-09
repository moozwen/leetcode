#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#

# @lc code=start
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # 桁を末尾から処理していく
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:  # 9未満であればそのまま1を加えて終了
                digits[i] += 1
                return digits
            digits[i] = 0  # 9であれば0にして次の桁に繰り上がり
        
        # 全ての桁が繰り上がりで処理された場合
        return [1] + digits  # 先頭に1を追加した新しい配列を返す
        
# @lc code=end

