from array import *

Arr1 = array('i',[34,54,55,44,554,32,11])
Arr2 = array(Arr1.typecode, Arr1.tolist())
print(Arr1)
print(Arr2)
Arr2.append(999)
print(Arr2)
