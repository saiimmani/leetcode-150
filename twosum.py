class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        num_map = {}  # Dictionary to store number and index
        for i, num in enumerate(nums):
            complement = target - num
            if complement in num_map:
                return [num_map[complement], i]  # Return indices of the two numbers
            num_map[num] = i  # Store the index of the current number
        return []
