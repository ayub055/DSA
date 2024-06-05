class Solution:
    def commonChars(self, words):
        result = []
        for char in range(ord('a'), ord('z') + 1):
            char = chr(char)
            min_count = float('inf')
            for word in words:
                count = word.count(char)
                min_count = min(min_count, count)
                if min_count == 0:
                    break
            
            result.extend([char] * min_count)
    
        return result
                
            
            
                    
sol = Solution()
nums =["acabcddd","bcbdbcbd","baddbadb","cbdddcac","aacbcccd","ccccddda","cababaab","addcaccd"]
print(sol.commonChars(nums))
    
