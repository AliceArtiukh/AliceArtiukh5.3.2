from math import gcd
class Rational:
    def __init__(self, n, d=1):
        if isinstance(n, str):
            if '/' in n:
                parts = n.split('/')
                n, d = int(parts[0]), int(parts[1])
            else:
                n, d = int(n), 1
        if d == 0:
            raise ValueError(f"Don't know how to deal with {n}")
        common = gcd(int(n), int(d))
        self._n = int(n) // common
        self._d = int(d) // common
        if self._d < 0:
            self._n, self._d = -self._n, -self._d
    def __call__(self):
        return self._n / self._d
    def __add__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        new_n = self._n * other._d + other._n * self._d
        new_d = self._d * other._d
        return Rational(new_n, new_d)
    def __str__(self):
        return f"{self._n}/{self._d}"

class RationalList:
    def __init__(self):
        self._items = []
    def __len__(self):
        return len(self._items)
    def __getitem__(self, index):
        return self._items[index]
    def __iadd__(self, other):
        if not isinstance(other, Rational):
            other = Rational(other)
        self._items.append(other)
        return self
    def __str__(self):
        return "[" + ", ".join(str(x) for x in self._items) + "]"

file_name = input("Enter the file name: ")
r_list = RationalList()
try:
    with open(file_name, 'r') as f:
        for line in f:
            for word in line.split():
                r_list += word
    print(f"{r_list}")
    print(f"{len(r_list)}")
    if len(r_list) > 0:
        total = r_list[0]
        for i in range(1, len(r_list)):
            total = total + r_list[i]
        print(f"{total}")
        print(f"{total():.4f}")
    else:
        print("nothing")
except FileNotFoundError:
    print("File not found")