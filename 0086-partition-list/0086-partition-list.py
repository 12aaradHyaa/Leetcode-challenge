class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        less = ListNode(0)
        greater = ListNode(0)

        p1 = less
        p2 = greater

        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next

            head = head.next

        p2.next = None
        p1.next = greater.next

        return less.next
