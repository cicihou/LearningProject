'''
贪心的思想就是寻找局部最优解

1. 题目要求船数最少，i.e. 每艘船尽量多装一些重量
2. 每次装人先将最大重量的装上，然后从轻到重遍历剩下的人，看剩余容量能否再装下一个人

由于每艘船限制只能载两个人，最轻的人搭配最重的人，对于我们来说是最少计算的局部最优解

如果最轻的人 a 和最重的人 b 重量和超过了 limit，那么其他人不用看了，肯定都不行。
如果最轻的人 a 可以和最重的人 b 同时载运，此时会存在另外一种方案（选择非最轻的人 c 和最重的人 b 配对）比其更优么？
答案是不能的，因为每艘船只能载两个人，即使运了 非最轻的人 c + 最重的人 b，最轻的人 a 还是需要占用一艘船的位置，需要的船数目还是一样的

最轻的人能跟最重的人配对，那就能和任何一个人配对
如果把最重的给了第二轻的，那么最轻的也只能去跟第二重的配对，事实上还是浪费了船的配重
'''


class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        Greedy + two-pointer
        消耗掉一艘船，最重的人无论如何都走了一个，最轻的人如果满足要求也能运走
        完成遍历时，一共消耗的船的数量，就是我们想要的结果

        time: O(nlogn)
        space: O(1)
        '''
        people.sort()
        i = 0
        j = len(people) - 1
        res = 0
        while i <= j:
            res += 1
            if people[i] + people[j] <= limit:
                i += 1
            j += 1
        return res
