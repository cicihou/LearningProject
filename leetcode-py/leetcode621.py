'''
Task Scheduler
code: https://leetcode.com/problems/task-scheduler/discuss/1468369/Python-solution
code: https://leetcode-cn.com/problems/task-scheduler/solution/tong-zi-by-popopop/
'''

from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks).most_common()
        max_task_count = counter[0][1]

        idle = (max_task_count - 1) * n  # the most idle bucket

        for k, v in counter[1:]:  # we dont need to calculate the most frequent task
            if v == max_task_count:
                idle = idle - v + 1  # add an extra bucket
            else:
                idle -= v  # the idle bucket can be occupied
        return len(tasks) + max(0, idle)
