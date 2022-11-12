import sys  
from sys import version
import random
import time as t  

date=t.localtime()

print(date)
print(sys.version)

time_now=t.localtime()
print("transaction effectué à:",str(time_now.tm_hour) + "h" )

liste=[1,3,5,8,9,5]
print(random.choice(liste))

print(version)