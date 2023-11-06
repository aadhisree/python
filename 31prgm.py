import statistics
import math
import time

print("the value of pi is",math.pi)
second=time.time()
print("second since epoch(the point where time begins)=",second)
li=[1,2,3,3,2,2,2]
print("The average of list value is:",end="")
print(statistics.mean(li))
local_time= time.ctime(second)
print("local time:",local_time)