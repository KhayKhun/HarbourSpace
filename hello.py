n = int(input())

s = set([x for x in range(1, n+ 1)])

for i in range(n- 1):
    k = int(input())
    s.remove(k)

print(next(iter(s)))