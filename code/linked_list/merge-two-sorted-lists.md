# Merge Two Sorted Lists

**Difficulty** :star:

## Question Description

![image](https://user-images.githubusercontent.com/53313027/168486494-4e481e12-f8ff-42b7-a32d-ce36ba5a4769.png)

## Approach #1

Initially I started with the brute force algorithm, which may take up to **O(N) time complexity**
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # handle empty special cases
        if not list1 and not list2:
            return list1
        if not list1 or not list2:
            if not list1:
                return list2
            else:
                return list1
        
        # set small to be the smaller head of the two lists
        if list1.val < list2.val:
            small = list1
            large = list2
        else:
            small = list2
            large = list1
        
        head = small
        while small and large:
            while small.next and small.next.val < large.val:
                small = small.next
            # swap and advance
            tmp = small.next
            small.next = large
            large = tmp
            small = small.next 
        
        return head
```

Although it passed by beating 21.8% users, it seems there's space to improve
![image](https://user-images.githubusercontent.com/53313027/168486524-4d904af7-4633-4440-abb3-8abcafb57ce7.png)

## Approach #2

To improve, I considered to use a list to store all elements, and sort the list. Then create a linked list containing all elements of the list. It seems that it would take longer time, but this is indeed one of the approaches I came up.

``` python
class Solution:
    '''
        Convert a list to a linked list
        Time Complexity: O(N)
    '''
    def lst2link(self, lst):
        cur = dummy = ListNode()
        for e in lst:
            cur.next = ListNode(val=e)
            cur = cur.next
        return dummy.next
    
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        all_elem = []
        # add all element to list
        while list1:
            all_elem.append(list1.val)
            list1 = list1.next
        while list2:
            all_elem.append(list2.val)
            list2 = list2.next
        
        all_elem.sort() # O(NlogN)
        return self.lst2link(all_elem)
```

It seem to be an improvement. I think the main reason is that it avoided a large O(N) loop with multiple operations, instead it had constant behaviour on two small lists and a O(NlogN) sort.

![image](https://user-images.githubusercontent.com/53313027/168486862-bf889821-dca4-45ab-a13e-5f2e5f81f613.png)

I then changed the built-in sorting to my own code as below, and the behaviour stayed consistent.

``` python
# instead of list.sort(), i'm using self.insertion_sort(list)

'''
binary search of a list, return index of key in nums[start:end] as an integer
'''
def binary_search(self, nums:List[int], key, start, end) -> int:
    # found key
    if end - start <= 1:
        if key < nums[start]:
            return start-1
        return start
    # otherwise recursively run binary_search
    mid = (start + end) // 2
    if nums[mid] < key:
        return self.binary_search(nums, key, mid, end)
    elif nums[mid] > key:
        return self.binary_search(nums, key, start, mid)
    else:
        return mid

'''
Modify the given list nums using binary insertion sort, time comlexity O(nlogn)
'''
def insertion_sort(self, nums:List[int]) -> None:
    for i in range (1, len(nums)):
        tmp = nums[i]
        pos = self.binary_search(nums, tmp, 0, i) + 1
        for k in range(i, pos, -1):
            nums[k] = nums[k - 1]
        nums[pos] = tmp

```

![image](https://user-images.githubusercontent.com/53313027/168486992-17a25e76-8daa-43d9-a386-ad0e9699803f.png)


## Optimal solution:

``` python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        if list1 == None :
            return list2
        elif list2 == None:
            return list1
        
        head1 = list1
        head2 = list2
        
        prev = None # Most important pointer it will make all the links
        
        while head1 != None and head2 != None:
            if head1.val <= head2.val:
                if prev != None:
                    prev.next = head1
                prev = head1
                head1 = head1.next         
            else:
                if prev != None:
                    prev.next = head2
                prev = head2
                head2 = head2.next
                
        if head1 != None:
            prev.next = head1
        else:
            prev.next = head2
        
        if list1.val <= list2.val:
            return list1
        else:
            return list2
```

The idea is to use the merge sort technique

![image](https://user-images.githubusercontent.com/53313027/168487055-a324e9cf-ecef-428b-aff7-794713f767f4.png)



