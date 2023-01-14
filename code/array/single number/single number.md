## Approach 1:

Brute Force
Intuition:
Iterate through every element in the nums and check if any of the element does not appear twice, in that case return the element.
Time: O(n^2)
Space: O(1)

## Approach 2:

Use Sorting
Intuition:
If the elements of the nums array are sorted/when we sort it, we can compare the neighbours to find the single element. It is already mentioned that all other elements appear twice except one.
Time: O(nlogn) for sorting then O(n) to check neighbouring elements
Space: O(1)

## Approach 3:

Use Hashing/Set
Intuition:
i) As we iterate through the nums array we store the elements encountered and check if we find them again while iteration continues. While checking if we find them again, we maintain a single_element object/variable which stores that single element, eventually returning the single_element.
ii) The other way is to maintain a num_frequency hashmap/dictionary and iterate over it to find which has exactly 1 frequency and return that key/num.
Time: O(n) for iterating over the nums array
Space: O(n) for hashing

## Approach 4:

Use Xor/Bit Manipulation
Intuition:
Xor of any two num gives the difference of bit as 1 and same bit as 0.
Thus, using this we get 1 ^ 1 == 0 because the same numbers have same bits.
So, we will always get the single element because all the same ones will evaluate to 0 and 0^single_number = single_number.
Time: O(n)
Space: O(1)

``` python 3
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        xor = 0
        for num in nums:
            xor ^= num
        
        return xor
```
