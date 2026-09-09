class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i in range(len(nums)): # here index i iterates through len(nums) 
            num = nums[i]           # having the num at index i
            diff = target - num      # calclating the difference
            if diff in seen:          # if diff is in seen return idx of diff in seen and idx i 
                return [seen[diff],i]  
            seen[num] = i               # if not seen remember curr num and idx
        return []                        # this returns the idx of result