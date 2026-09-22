class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        a ={} # dictionary or hashmap   
        for i in nums:
            a[i] = a.get(i,0) + 1 # gets frequency 
            if a[i] > len(nums)//2:
                return i
