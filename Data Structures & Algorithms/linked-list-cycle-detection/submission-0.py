# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Initially slow and fast starts from head
        slow = head
        fast = head

        # Running a loop until curr and curr.next are not none

        while fast and fast.next is not None:
            slow = slow.next    # Slow move 1 step ahead
            fast = fast.next.next # Fast moves 2 steps ahead

            # After continuous iterations if slow and fast meet at a node there is a cycle else Nome
            if slow == fast:
                return True

        return False
