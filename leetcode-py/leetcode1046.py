class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        method 1 simulation
        :param stones:
        :return:
        '''
        while len(stones) > 1:
            stones.sort()
            y = stones.pop()
            x = stones.pop()

            if x != y:
                stones.append(y - x)

        return stones[-1] if stones else 0

        '''
        method 2 heap
        '''
        # TODO
