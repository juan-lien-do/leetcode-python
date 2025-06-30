class Solution(object):
    def __init__(self):
        pass

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # definimos sectores de busqueda, delimitados por li y ls.
        if len(nums) == 0:
            return 0
        if nums[0] > target:
            return 0
        if nums[len(nums)-1] < target:
            return len(nums)
        
        # print(c)
        li = 0
        ls = len(nums)-1

        while True:    
            tasa_avance = ((ls - li) // 2)
            print(li, ls, tasa_avance)
            c = (li + ls) // 2
            scoped = nums[c]
            # si lo encuentra
            if scoped == target:
                return c            
            elif scoped < target:
                li = li + tasa_avance
            else: 
                ls = ls - tasa_avance
            
            #si no existe en la lista?
            #if tasa_avance == 0:
            if tasa_avance == 0:
                return ls
            

            
        




sol = Solution()

print(sol.searchInsert([1, 2, 3, 4, 5, 6, 8], 8))