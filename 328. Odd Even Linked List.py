def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        odd = head
        evenhead = even = head.next
        while even and even.next:
            odd.next = odd.next.next
            odd = odd.next
            
            even.next = even.next.next
            even = even.next
        odd.next = evenhead
