 def reverseVowels(self, s: str) -> str:
        d = {'a':1, 'e':2, 'i':3, 'o':4, 'u':5, 
             'A':6, 'E':7, 'I':8, 'O':9, 'U':10}
        stack = [i for i in s if i in d]
        return "".join([i if i not in d else stack.pop() for i in s])
                
