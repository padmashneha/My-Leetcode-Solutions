def mergeAlternately(self, word1: str, word2: str) -> str:
        w1 = len(word1)
        w2 = len(word2)
        x = 0
        y = 0
        res = []
        while x<w1 or y<w2:
            if x<w1:
                res.append(word1[x])
                x+=1
            if y<w2:
                res.append(word2[y])
                y+=1

        return ''.join(res)
