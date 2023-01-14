![image](https://user-images.githubusercontent.com/53313027/212446916-5378eea3-a6e4-4297-834f-3eb32128ae80.png)

## Approach:

Use two pointers, if there's a cycle, then it will eventually meet each other

``` python 3
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        while fast and slow:
            if not fast.next:
                break
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
```

![image](https://user-images.githubusercontent.com/53313027/212446981-6bd117de-d75c-4113-881a-8837af6c541e.png)
