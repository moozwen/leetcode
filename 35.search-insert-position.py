#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2  # Find the mid index
            
            if nums[mid] == target:
                return mid  # Target found, return the index
            elif nums[mid] < target:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half
                
        # If target is not found, return the position where it should be inserted
        return left
        
# @lc code=end

