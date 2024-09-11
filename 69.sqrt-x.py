#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        # 内部関数で再帰を実装
        def binary_search(left: int, right: int) -> int:
            if left > right:
                return right
            
            mid = (left + right) // 2
            mid_squared = mid * mid
            
            if mid_squared == x:
                return mid
            elif mid_squared < x:
                return binary_search(mid + 1, right)
            else:
                return binary_search(left, mid - 1)

        # 特別ケースとして0の平方根は0
        if x == 0:
            return 0
        
        # 1からxまでの範囲で二分探索
        return binary_search(1, x)
        
        # if x == 0:
        #     return 0
        
        # left, right = 1, x
        
        # while left <= right:
        #     mid = (left + right) // 2
        #     if mid * mid == x:
        #         return mid
        #     elif mid * mid < x:
        #         left = mid + 1
        #     else:
        #         right = mid - 1
        
        # return right
# @lc code=end

