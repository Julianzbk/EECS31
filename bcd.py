from binary import *
from add import fullsub


def dec_to_bcd(num: int) -> str:
    bcd_str = ''
    for digit in str(num):
        bcd_str += f"{dec_to_bin(int(digit)):0>4} "
        """
        bcd_str = dec_to_bin(int(digit))
        while len(bcd_digit) < 4:
            bcd_digit = '0' + bcd_digit
        bcd_str += bcd_digit
        """
    return bcd_str


def bin_to_bcd(num: str) -> str:
    # 4-bit ONLY
    if num[0] == "1":
        if not(num[1] == "0" and num[2] == "0"):
            return "0001 " + fullsub(num, "1010")[1:]
    return num