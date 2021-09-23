class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        '''
        不难，但是注意按给的条件来排序

        The letter-logs come before all digit-logs.
        The letter-logs are sorted lexicographically by their contents. If their contents are the same, then sort them lexicographically by their identifiers.
        The digit-logs maintain their relative ordering.

        :param logs:
        :return:
        '''
        digit_logs = []
        letter_logs = []
        for log in logs:
            log = log.split(' ')
            if log[-1].isdigit():
                digit_logs.append(' '.join(log))
            else:
                letter_logs.append(log)
        letter_logs.sort(key=lambda x: (x[1:], x[0]))
        letter_logs = [' '.join(log) for log in letter_logs]
        return [*letter_logs, *digit_logs]
