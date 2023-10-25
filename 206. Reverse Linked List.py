def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None 
        cur = head
        while cur:
            next_node = cur.next
            cur.next = prev
            prev = cur
            cur = next_node
        return prev
