#
# @lc app=leetcode id=26 lang=python3
#
# [26] Remove Duplicates from Sorted Array
#

# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # ユニークな＝元の配列の要素の次の位置を指す
        i = 1

        for j in range(1, len(nums)):
            if nums[j] != nums[j-1]:
                # 元の配列の次の要素に、ユニークな値を入れる
                nums[i] = nums[j]
                i += 1
        
        return i

# @lc code=end

