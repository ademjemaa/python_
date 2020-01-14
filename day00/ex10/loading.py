import time
import sys


def ft_progress(lst):
    initial = time.time()
    first = 0
    for i in range(len(lst)):
        yield lst[i]
        if i == 0:
            first = time.time() - initial
        current = time.time() - initial
        eta = (len(lst) - 1 - i) * first
        percen = int(i / (len(lst) - 1) * 100)
        var = '>'
        for x in range(0, int(50 / len(lst) * i)):
            var = ''.join(('=', var))
        sys.stdout.write(f"ETA: {eta:.2f}s [{percen:3}%] [{var:50}]")
        sys.stdout.write(f"{i + 1}/{len(lst)} | elapsed time {current:.2f}s\r")
    sys.stdout.write("\r\n...")


listy = range(1000)
ret = 0
for elem in ft_progress(listy):
    ret += (elem + 3) % 5
    time.sleep(0.01)
print()
print(ret)
