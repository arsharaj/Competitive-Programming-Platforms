import collections

class Solution:
    def maxEnvelopes(self, envelopes):
        envelopes.sort(key = lambda envelope: (envelope[0], -envelope[1]))
        cache = []
        
        for width, height in envelopes:
            counter = collections.bisect_left(cache, height)
            if counter == len(cache):
                cache.append(height)
            else:
                cache[counter] = height
        return len(cache)