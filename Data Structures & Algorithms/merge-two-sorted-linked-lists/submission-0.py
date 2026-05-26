# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = ListNode(0)
        temp_pt = temp
        pt1 = list1
        pt2 = list2

        while pt1 and pt2:
            if pt1.val < pt2.val:
                temp_pt.next = pt1
                temp_pt = temp_pt.next
                pt1 = pt1.next
            else:
                temp_pt.next = pt2
                temp_pt = temp_pt.next
                pt2 = pt2.next
        
        if pt1:
            temp_pt.next = pt1
        elif pt2:
            temp_pt.next = pt2
        
        return temp.next




"""
Goal: take two linked lists and create a new ordered linked list


"""
        