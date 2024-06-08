class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_new = {None: None}
        curr = head
        while curr:
            copy = Node(curr.val)
            old_to_new[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = old_to_new[curr]
            copy.next = old_to_new[curr.next]
            copy.random = old_to_new[curr.random]
            curr = curr.next
        return old_to_new[head]