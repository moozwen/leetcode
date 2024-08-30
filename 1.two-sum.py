#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # numをキーに、indexをバリューとする辞書
        index_map = {}
        for i, num in enumerate(nums):
            diff = target - num
            # targetとの差分をnumsから探す
            if diff in index_map:
                return [index_map[diff], i]
            index_map[num] = i

# @lc code=end
