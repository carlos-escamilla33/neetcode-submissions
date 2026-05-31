# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp_head = ListNode("temp")
        temp_head.next = head
        temp = temp_head
        curr_ = head

        length = 0
        while curr_:
            length += 1
            curr_ = curr_.next

        for _ in range(length - n):
            temp = temp.next
        temp.next = temp.next.next
        return temp_head.next



"""
Goal: remove the n variable from the end of the linked list

if the head is none then just return the head
create a temp variable so you can avoid the first node removal edge case


"""
        