class MinStat(object):
    def __init__(self):
        self.lst = []

    def add_number(self, x):
        self.lst.append(x)

    def result(self):
        return min(self.lst) if self.lst else None


class MaxStat(MinStat):

    def result(self):
        return max(self.lst) if self.lst else None


class AverageStat(MinStat):

    def result(self):
        return sum(self.lst) / len(self.lst) if self.lst else None


values = [1, 2, 4, 5]

mins = MinStat()
maxs = MaxStat()
average = AverageStat()
for v in values:
    mins.add_number(v)
    maxs.add_number(v)
    average.add_number(v)

print(mins.result(), maxs.result(), '{:<05.3}'.format(average.result()))
