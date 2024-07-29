class Solution:
    def hasCycle(self, head:Optional[ListNode]) -> bool:
        fast = head
        while fast and fast.next:
            head = head.next
            fast = fast.next.next
            if fast is head:
                return False
        return True
    
     # T - O(n) S - O(1)