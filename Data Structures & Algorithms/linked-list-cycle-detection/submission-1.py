# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # slow fast pointer approach
        if head:
            slow = head
            fast = head
            
            while fast:
                slow = slow.next
                if fast.next is None:
                    fast = None
                else:
                    fast = fast.next.next
                if slow == fast and slow != None:
                    return True
            return False
        else:
            return False

        