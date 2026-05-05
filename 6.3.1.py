from math import gcd

class Rational:
    def __init__(self, n, d=1):
        if isinstance(n, str):
            if '/' in n:
                parts=n.split('/')
                n,d=int(parts[0]), int(parts[1])
            else:
                n,d=int(n), 1
        common=gcd(int(n), int(d))
        self._n=int(n)//common
        self._d=int(d)//common
        if self._d<0:
            self._n, self._d = -self._n, -self._d
    def __call__(self):
        return self._n/self._d
    def __getitem__(self, key):
        if key=="n" or key=="numerator": return self._n
        if key=="d" or key=="denominator": return self._d
        raise KeyError()
    def __add__(self, other):
        if not isinstance(other, Rational): other = Rational(other)
        return Rational(self._n * other._d + other._n * self._d, self._d * other._d)
    def __str__(self):
        return f"{self._n}/{self._d}"
class RationalIterator:
    def __init__(self, items):
        self._data = sorted(items, key=lambda x: (x._d, x._n), reverse=True)
        self._index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self._index < len(self._data):
            result = self._data[self._index]
            self._index += 1
            return result
        raise StopIteration
class RationalList:
    def __init__(self):
        self._items=[]
    def __len__(self):
        return len(self._items)
    def __getitem__(self, index):
        return self._items[index]
    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self._items.extend(other._items)
        else:
            if not isinstance(other, Rational): other = Rational(other)
            self._items.append(other)
        return self
    def __iter__(self):
        return RationalIterator(self._items)
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
        total_sum = r_list[0]
        for i in range(1, len(r_list)):
            total_sum = total_sum + r_list[i]
        print(f"{total_sum}, {total_sum():.4f}")
    for item in r_list:
        print(f"{item}")
except FileNotFoundError:
    print("FileNotFoundError")