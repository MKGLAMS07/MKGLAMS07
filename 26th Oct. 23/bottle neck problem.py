ls = [int(i)for i in input().split()]
ls2 = []
for i in ls:
    t = ls.count(i)
    ls2.append(t)
o = max(ls2)
print(o)
