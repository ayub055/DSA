class TwoPointers:
    
    # 1. Valid Palindrome
    def isPalindrome(self, s):
        joined_string = "".join([ch for ch in s.lower() if ch.isalnum()])
        n = len(joined_string)
        l = 0
        r = n - 1
        
        while l <= r :
            if joined_string[l] != joined_string[r]:
                return False
            else:
                l += 1 
                r -= 1
        
        return True
    
    # 2. Two Sum : Input is sorted
    def twoSum(self, numbers, target):
        l = 0
        r = len(numbers) - 1
        
        while l <= r :
            sum = numbers[l] + numbers[r]
            if sum == target:
                return [nums[l], nums[r]]
            elif sum < target:
                l += 1
            else:
                r -= 1
        
        return None
    
    def two_sum_unsorted(self, numbers, target):
        remaining_to_index = {}
        for i in range(len(numbers)):
            remaining = target - numbers[i]
            if remaining not in remaining_to_index:
                remaining_to_index[numbers[i]] = i
            else:
                return numbers[i], numbers[remaining_to_index[remaining]]
                
    # 3. Three sum
    def threeSum(self, nums):
        result = []
        print(f'Input : ', nums)
        for i in range(len(nums)):
            curr_elem = nums[i]
            curr_nums = nums.copy()
            curr_nums.remove(curr_elem)
            print(curr_nums, curr_elem)
            if not self.two_sum_unsorted(numbers=curr_nums, target=(0 + curr_elem)):
                continue
            else:
                e1, e2 = self.two_sum_unsorted(numbers=curr_nums, target=(0 + curr_elem))
                result.append([curr_elem, e1, e2])
            # print(result)
        res = []
        for x in result:
            if x not in res:
                res.append(x)
                
        return res
        
        
            
nums = [-1,0,1,2,-1,-4]
# nums = [4, 5, 6]     
       
obj = TwoPointers()
print(obj.threeSum(nums))