class ReversedList(object):
    def __init__(self, ls):
        self.a = list(reversed(ls))

    def __str__(self):
        return str(self.a)

    def __iter__(self):
        for el in self.a:
            yield el


rl = ReversedList([10, 20, 30])
for i in range(len(rl)):
    print(rl[i])



