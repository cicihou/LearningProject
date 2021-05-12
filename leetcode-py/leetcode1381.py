class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.item = []

    def push(self, x: int) -> None:
        if len(self.item) < self.max_size:
            self.item.append(x)

    def pop(self) -> int:
        if self.item:
            return self.item.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        length = len(self.item)
        for i in range(length):
            # attention: it should be <, cannot equals to
            # k is the volume starts from 1, while index start from 0
            if i < min(k, length):
                self.item[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)