class Binary:
    def __init__(self, value=0):
        self.value = False if value == 0 else True
    def __str__(self):
        return "1" if self.value is True else "0"
    def __int__(self):
        return 1 if self.value == 1 else 0
    def __add__(self, other):
        result = self.value or other.value
        return Binary(1) if result is True else Binary(0)
    def __mul__(self, other):
        result = self.value and other.value
        return Binary(1) if result is True else Binary(0)
    def __xor__(self, other):
        result = self.value ^ other.value
        return Binary(1) if result is True else Binary(0)
    def __neg__(self):
        return Binary(1) if self.value == 0 else Binary(0)

class BinaryString:
    def __init__(self, value=0):
        if type(value) == tuple: #"overloading"
            self.value = bin_to_dec(value, False)
            self.string = ''.join([str(b) for b in value])
        else:
            self.value = value
            self.string = dec_to_bin(value)

    def __str__(self):
        return str(self.string)
    def __int__(self):
        return self.value
    def __iter__(self):
        return iter(self.string)

def bin_to_dec(num: str, neg: bool) -> int:
    num = num[::-1]
    value = 0
    m = 1
    if neg:
        num = [1 if s == "0" else 0 for s in num]
    for b in num:
        value += int(b) * m
        m *= 2
    return value if not neg else -value

def dec_to_bin(num: int) -> str:
    if num == 0:
        return '0'
    string = []
    q, r = num, 999
    while q > 0:
        q, r = divmod(q, 2)
        string.append(str(r))
    return ''.join(reversed(string))
