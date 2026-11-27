class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
   #make an empty dict: number index
        dict = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            for j in range(len(nums)):
                if nums[j]== compliment and i!=j:
                    return [i,j]
            
        