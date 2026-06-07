class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = set()

        for i in range(len(words)):
            for j in range(len(words)):
                word1 = words[i]
                word2 = words[j]
                if i != j and word1 in word2:
                    res.add(word1)

        return list(res)
        