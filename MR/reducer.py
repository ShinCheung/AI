import sys

result={}
for line in sys.stdin:
    kvs = line.strip().split()
    k = kvs[0]
    v = kvs[1]
    if k in result:
        result[k] += 1
    else:
        result[k] = 1
for k, v in result.items():
    print(k, v)