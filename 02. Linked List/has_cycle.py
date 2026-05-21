class ListNode:
    def __init__(self, val=0, next: ListNode = None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: ListNode = None) -> bool:
        if not head:
            return False
        
        first = head
        second = head.next

        while first and second:
            if first == second:
                return True
            
            first = first.next

            second = second.next.next

        return False
    
def main():

    node4 = ListNode(-4)
    node3 = ListNode(0)
    node2 = ListNode(2)
    head = ListNode(3)

    head.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    s = Solution()
    isCycle = s.hasCycle(head)

    print(isCycle)

main()
