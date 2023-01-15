![1673751808604](https://user-images.githubusercontent.com/53313027/212520768-9cbaffd4-9cc1-4f09-a70e-b74352c517d5.jpg)
![image](https://user-images.githubusercontent.com/53313027/212520772-93e29f27-fd17-45fb-a2da-b3345b19b2ed.png)
![image](https://user-images.githubusercontent.com/53313027/212520774-e7f049d4-e39a-4925-96ad-49fa75c700af.png)


``` python 3
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a, b = headA, headB
        while (a != b):
            a = headB if not a else a.next
            b = headA if not b else b.next
        return a
```

![image](https://user-images.githubusercontent.com/53313027/212520782-084c3a5e-077f-4fdb-ba84-6d644e077d6a.png)
