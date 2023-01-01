![image](https://user-images.githubusercontent.com/53313027/210187324-22ca3714-cde3-42e3-b111-4c178595f12f.png)

## Approach 1

Of course we could solve it by brute force, traversing from 0 to x, and check each number's square, but that would be O(N)

## Approach 2

Considering the integers are naturally a sorted array, we could use binary search, and verify each iteration. This only takes O(log(N)) time and turned out to work really well in practice (beats 80+%)
