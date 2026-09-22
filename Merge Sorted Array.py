class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        for j in range(n):
            nums1[m+j] = nums2[j]
        
        nums1.sort()
        
