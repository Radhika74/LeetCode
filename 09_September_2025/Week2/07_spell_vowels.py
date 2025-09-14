class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        res =[]
        s=set()
        lowers={}
        devowels={}
        vowels="aeiou"
        for w in wordlist:
            s.add(w)
            lowers.setdefault(w.lower(),w)
            devowels.setdefault("".join(['*' if c in vowels else c for c in w.lower()]), w)

        for q in queries:
            if q in s:
                res.append(q)
            elif (lower := q.lower()) in lowers:
                res.append(lowers[lower])
            elif (devowel := "".join(["*" if c in vowels else c for c in lower])) in devowels:
                res.append(devowels[devowel])
            else:
                res.append("")
        return res

