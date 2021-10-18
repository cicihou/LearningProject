import heapq


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        '''
        simulation

        enqueueTime 表示在这个时间及之后，这个任务才可以加载进队列
        processingTime 表示这个任务需要的处理时间

        我们每次处理的是，当前排队的任务队列中耗时最短的那个任务

        若「消息队列mq」中无任务，将时间直接拨到当前对应下个任务的开始时间
        如果当前的时间 >= 下个对应任务的开始时间，则将对应的任务加进 mq，表示任务已经开始等待
        mq 中的任务格式为 (task_processing_time, task_index)
        取出当前 min_heap 中最小的任务（由于 processing_time 放在前面，也就是所有在 mq 中 processing_time 最小的任务）
        当前时间向后（产生了耗时），将 index 加入结果集

        time: O(nlogn)
        space: O(n)
        '''
        tasks = [(*task, i) for i, task in enumerate(tasks)]
        tasks.sort()
        mq = []
        time = 0
        res = []
        i = 0
        for _ in tasks:
            if not mq:
                time = max(time, tasks[i][0])
            while i < len(tasks) and tasks[i][0] <= time:
                heapq.heappush(mq, (tasks[i][1], tasks[i][2]))
                i += 1
            process_time, index = heapq.heappop(mq)
            time += process_time
            res.append(index)
        return res
