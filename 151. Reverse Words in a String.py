def reverseWords(self, s: str) -> str:
        stack = s.split(' ')
        res = []
        while stack:
            res.append(stack.pop())
        for i in res:
            if i !='':
                stack.append(i)
        return " ".join(stack)
        
