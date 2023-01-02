class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_cpy = nums1[0:m] # create a copy of nums1 so that we could set in-place
        i, j = 0, 0 # pointers for each list

        # compare two lists, and set in non-decreasing order
        while i < m and j < n :
            if nums1_cpy[i] <= nums2[j]:
                nums1[i+j] = nums1_cpy[i]
                i += 1
            else:
                nums1[i+j] = nums2[j]
                j += 1

        # loop finished, but there exist some left elements
        if i == m:
            # rest in nums2 is greater than nums1_cpy[m-1]
            nums1[i+j::] = nums2[j::]
        if j == n:
            # rest in nums1_cpy is greater than nums2[n-1]
            nums1[i+j::] = nums1_cpy[i::]
