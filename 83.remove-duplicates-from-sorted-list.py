#
# @lc app=leetcode id=83 lang=python3
#
# [83] Remove Duplicates from Sorted List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # ベースケース: 空のリストまたは最後のノードに到達した場合
        if not head or not head.next:
            return head
        
        # 再帰的にリストを処理していく
        head.next = self.deleteDuplicates(head.next)
        
        # 重複していれば現在のノードをスキップ
        return head.next if head.val == head.next.val else head

        # # 現在のノードがNoneの場合、そのままNoneを返す
        # if not head:
        #     return head
        
        # # 現在のノードを格納する変数を用意
        # current = head
        
        # # リストを最後まで走査
        # while current and current.next:
        #     # 現在のノードの値が次のノードの値と同じならば、次のノードをスキップ
        #     if current.val == current.next.val:
        #         current.next = current.next.next
        #     else:
        #         # 異なる場合は次のノードに進む
        #         current = current.next
        
        # return head
# @lc code=end

