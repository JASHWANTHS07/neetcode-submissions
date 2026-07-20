from collections import Counter
def word_histogram(word: str) -> dict:
    return dict(Counter(word.lower()))
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        unq_s = set(s)
        unq_t = set(t)
        if len(s)==len(t) and unq_s==unq_t:
            his_s = word_histogram(s)
            his_t = word_histogram(t)
            for k in unq_s:
                if his_s[k]!=his_t[k]:
                    return False
            return True
        else:
            return False

        