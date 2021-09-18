class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        res = 1
        counts = [0, 0, 0, 0, 0]
        cache = {'c': 0, 'r': 1, 'o': 2, 'a': 3, 'k': 4}

        for ch in croakOfFrogs:
            if ch not in cache:
                return -1
            counts[cache[ch]] += 1

            # if counts[0] >= counts[1] >= counts[2] >= counts[3] >= counts[4]:
            #     if counts[4] >= 1:
            #         counts = [c - 1 for c in counts]
            # else:
            #     return -1

            # when string is long, we prefer to use a loop instead comparing statement
            for i in range(1, len(counts)):
                if counts[i] < counts[i-1]:
                    return -1
            else:
                counts = [c-1 for c in counts]

            res = max(res, max(counts))
        if len(set(counts)) != 1:
            return -1
        return res
