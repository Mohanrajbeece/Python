import datetime
import time
x=datetime.datetime.now()
print(x)
time.sleep(5)
print(x.year)
print(x.strftime("%b"))