from add import *
from binary import *

def test_3(function):
    table_3 = [[0,0,0,0,1,1,1,1],[0,0,1,1,0,0,1,1],[0,1,0,1,0,1,0,1]]
    for i in range(8):
        values = (Binary(table_3[0][i]), Binary(table_3[1][i]),
                  Binary(table_3[2][i]))
        #print(*values)
        print(*function(*values))

def test_4(function):
    table_4 = [[0]*8 + [1]*8, [0]*4 + [1]*4 + [0]*4 + [1]*4,
               [0,0,1,1,0,0,1,1,0,0,1,1,0,0,1,1],[0,1]*8]
    for i in range(16):
        values = (Binary(table_4[0][i]), Binary(table_4[1][i]),
                  Binary(table_4[2][i]), Binary(table_4[3][i]))
        #values = str(table_4[0][i]) + str(table_4[1][i]) + str(table_4[2][i]) + str(table_4[3][i])
        #print(int(values[0])*2 + int(values[1]), '-', int(values[2])*2 + int(values[3]), '=')
        #print(function(values[:2], values[2:]))
        yield BinaryString(values)

a, b, c = Binary(0), Binary(1), Binary(1)
#print(fullsub("1100", "0011"))
#print(fullsub("1100", "0010"))
hither = list(test_4(fullsub))
thither = list(reversed(hither))

for i in range(16):
    diff = fullsub(str(hither[i]), str(thither[i]))
    print(int(hither[i]), '-', int(thither[i]), '=', end=' ')
    print(int(BinaryString(tuple(diff))))
