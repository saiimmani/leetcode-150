class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        dic = {}
        for i,num in enumerate(nums):
            if num in dic:
                distance = i - dic[num] # current - previous index 
                if distance <= k : # check the condition
                    return True
            dic[num] = i # storing into dic
        return False



            
