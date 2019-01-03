import sys

res = {}
for line in sys.stdin:
    kvs = line.strip().split()
    k = kvs[0]
    v = kvs[1]
    if k in res:
        res[k] += 1
    else:
        res[k] = 1
for k, v in res.items():
    print(k, v)
