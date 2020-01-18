class FIFO:
    def __init__(self, *args):
        self.list = [*args]

    def __repr__(self):
        return str(self.list)

    def isEmpty(self):
        if self.list:
            return False
        else:
            return True

    def push(self, object):
        return self.list.append(object)

    def pop(self):
        return self.list.pop(0)


if __name__ == '__main__':
    example = FIFO(1, 2, 3, 4, 5)
    print(example)
    print(example.isEmpty())
    example.push(6)
    print(example)
    example.pop()
    example.pop()
    example.pop()
    example.pop()
    example.pop()
    print(example)
    print(example.isEmpty())