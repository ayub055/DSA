class Solution:
    def subsets(self, nums):
        res = []
        subset = []
        
        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            
            subset.append(nums[i])
            dfs(i+1)
            
            subset.pop()
            dfs(i+1)
            
        dfs(0)
        return res

    
    
def check_duplicates_DC(elements):
    if len(elements) <= 1:
        return False
    else:
        mid = len(elements) // 2
        left = elements[ : mid]
        right = elements[mid : ]
        
        # Check in individual halves
        
        if check_duplicates_DC(left):
            return True
        
        if check_duplicates_DC(right):
            return True
        
        i = 0
        l , r = 0, 0 
        
        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                elements[i] = left[l]
                l += 1
            elif left[l] > right[r]:
                elements[i] = right[r]
                r += 1
            else:
                return True
            i += 1
            
        while l < len(left):
            elements[i] = left[l]
            i += 1
            l += 1
            
        while r < len(right):
            elements[i] = right[r]
            i += 1
            r += 1
        
print(check_duplicates_DC([1, 2, 3, 4, 5, 5, 5]))