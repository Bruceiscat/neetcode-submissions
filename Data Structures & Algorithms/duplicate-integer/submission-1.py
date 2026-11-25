class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sum = set()
        for num in nums:
            if num in sum:
                return True
            else:
                sum.add(num)
                
        return False

       

     
            
 
        