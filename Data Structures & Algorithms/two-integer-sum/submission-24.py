class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen_dict = {}

        for i, num in enumerate(nums):
            remainder = target - num
            if remainder in seen_dict:
                return [seen_dict[remainder], i]
            
            seen_dict[num] = i