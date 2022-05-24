import datetime


class Date:
    def __init__(self, d1, d2):
        self.d1 = d1
        self.total = 0
        for i in range(1, self.d1 + 1):
            if i == 1 or i == 3 or i == 5 or i == 7 or i == 8 or i == 10 or i == 12:
                self.total += 31
            if i == 4 or i == 6 or i == 9 or i == 11:
                self.total += 30
            if i == 2:
                self.total += 28
        self.d2 = d2
        self.d2 += self.total

    def __sub__(self, other):
        delta = self.d2 - other.d2
        return delta


jan5 = Date(1, 5)
jan1 = Date(1, 1)

print(jan5 - jan1)
print(jan1 - jan5)
print(jan1 - jan1)
print(jan5 - jan5)
