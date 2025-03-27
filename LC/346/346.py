class MovingAverage(object):
    def __init__(self, size):
        self.current = [0] * size
        self.added = 0
        self.total = 0
    def next(self, val):
        position = self.added % len(self.current)
        self.total -= self.current[position]
        self.total += val
        self.current[position] = val # Add to circular buffer
        self.added += 1
        return self.total)/ min([self.added, len(self.current)])
       


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)