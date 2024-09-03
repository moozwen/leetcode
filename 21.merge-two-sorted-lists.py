#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # ダミーヘッドを使って新しいリストを作成
        dummy = ListNode()
        current = dummy
        
        # 両方のリストが存在する間、ノードを比較して追加
        while list1 and list2:
            if list1.val <= list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        
        # 残ったリストがある場合、それを追加
        current.next = list1 if list1 else list2
        
        # ダミーノードの次のノードが実際のマージされたリストのヘッド
        return dummy.next
# @lc code=end

