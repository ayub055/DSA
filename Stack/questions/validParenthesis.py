class Solution:
    def isInvalid(self, s):
        # 1. ( ), { },  [ ]
        # 2. )(  Not allowed
        # 3. [}] not allowed
        
        # solution 1:
        # process the string ---> Maintain a stack --> check some condtion to see if current should push or pop
        match = {
                 ')' : '(', 
                 ']' : '[',
                 '}' : '{'
                 }
        
        stack = []
        open = '([{'
        close = '}])'
        for ch in s:
            if ch in open:
                stack.append(ch)
            elif ch in close:
                if len(stack) == 0:
                    return False
                elif stack[-1] == match(ch):
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
        