class CountedIterator:
    def __init__(self, data):
        self.data = data
        self.index = 0
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        self.index += 1
        self.count += 1
        return self.data[self.index - 1]

    def get_count(self):
        return self.count
