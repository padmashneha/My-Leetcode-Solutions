def gcdOfStrings(self, str1: str, str2: str) -> str:
        x= str1+str2
        y = str2 +str1
        if x == y:
            return str1[:gcd(len(str1), len(str2))]
        else:
            return ""
