from binary import *

def hadd(a, b):
    return a ^ b, a * b

def add(a, b, c=Binary()):
    return a ^ b ^ c, (a * b) + (b * c) + (a * c)

def fulladd(a, b):
    c = Binary(0)
    s = ""
    for i, j in zip(reversed(a), reversed(b)):
        a = Binary(int(i))
        b = Binary(int(j))
        s0, c = add(a, b, c)
        s = str(s0) + s
    return str(c) + s

def hsub(a, b):
    s, c = hadd(a, -b)
    if c == Binary(1):
        s = hadd(s, c)
    return hadd(s, Binary(1))
    return a ^ b, -a * b

def sub(a, b, c=Binary()):
    return (-a*-b*c)+(-a*b*-c)+(a*b*c)+(a*-b*-c), (-a*b)+(-a*c)+(b*c)

def fullsub(a, b):
    c = Binary(0)
    s = ""
    for i, j in zip(reversed(a), reversed(b)):
        a = Binary(int(i))
        b = Binary(int(j))
        s0, c = sub(a, b, c)
        s = str(s0) + s
    return str(c) + s
