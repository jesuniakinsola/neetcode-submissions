class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
   #make an empty dict: number index
        seen = {}  # number -> index

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in seen:
                return [seen[complement], i]

            seen[nums[i]] = i

       
       
       
       
       
       # dict = {}
       # for i in range(len(nums)):
        #    compliment = target - nums[i]
        #    for j in range(len(nums)):
         #       if nums[j]== compliment and i!=j:
          #          return [i,j]
            
        