class ListNode:
    def __init__(self, val=0, next: ListNode = None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        if not head:
            return None
        
        fast = slow = head

        while fast and fast.next:
            slow = slow.next

            fast = fast.next.next

        return slow

def main():
    node6 = ListNode(6)
    node5 = ListNode(5, node6)
    node4 = ListNode(4, node5)
    node3 = ListNode(3, node4)
    node2 = ListNode(2, node3)
    head = ListNode(1, node2)

    s = Solution()

    middle = s.middleNode(head)

    print(middle.val)

main()