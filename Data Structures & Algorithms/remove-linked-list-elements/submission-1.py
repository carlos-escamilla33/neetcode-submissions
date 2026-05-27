# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp_head = ListNode(0)
        temp_head.next = head
        temp = temp_head
        curr = head

        while curr:
            if curr.val == val:
                temp.next = curr.next 
                curr = curr.next
            else:
                temp = temp.next
                curr = curr.next
        
        return temp_head.next
        