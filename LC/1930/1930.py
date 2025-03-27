class Solution(object):
    def ul3p(src):
        histo = {}
        uniques = {}
        last = {}
        for c in "abcdefghijklmnopqrstuvwxyz":
             histo[c] = 0
             last[c] = -1
        for i in range(len(src)):
                histo[src[i]] += 1
                last[src[i]] = i
        for i in range(len(src)):
            if 1 < histo[src[i]]:
                 j = i + 1
                 while j < last[src[i]]:
                      palindrome = src[i]+src[j]+src[i]
                      uniques[palindrome] = 1
                      j += 1
        return len(uniques)

