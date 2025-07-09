import random
import os
count = 1
import psutil
import gc

# =============== do NOT run this code
# it will create out of memory and may restart the computer

all = []
while True:
    count += 1
    l1 = [random.randint(1, 10_000)] * 100_000_000  # 763 MB
    all.append(l1)
    if count % 10 == 0:
        print(count)
        mem = psutil.virtual_memory()
        print(f"Total: {mem.total / (1024 ** 3):.2f} GB")
        print(f"Available: {mem.available / (1024 ** 3):.2f} GB")
        print(f"Used: {mem.used / (1024 ** 3):.2f} GB")
        print(f"Free: {mem.free / (1024 ** 3):.2f} GB")

def foo():
    long_foo = [random.randint(1, 10_000)] * 100_000_000  # 763 MB
    print('done')
    return long_foo

result = foo()
r2 = result
del r2
new_foo = [random.randint(1, 10_000)] * 100_000_000  # 763 MB
del result  # 0 ref count
#print(long_foo)
