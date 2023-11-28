from bcd import *
from binary import *


def test_nums():
    for i in range(16):
        print("exp: " + dec_to_bcd(i))
        string = f"{dec_to_bin(i):0>4}"
        print(string, bin_to_bcd(string))

test_nums()