import math
import time
start_time = time.time()

#r = radicand
def simplify(r):
    num = int(math.sqrt(r))
    while num > 0:
        if r % num ** 2 == 0:
            break
        else:
            num -= 1

    r /= num ** 2    
    print((num, r))

simplify(4200)

print("Execution Time:" , time.time() - start_time)
