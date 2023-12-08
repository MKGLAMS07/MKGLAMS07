ls = [int(i)for i in input().split()]
ls1=[]
for i in ls:
    if i not in ls1:
        ls1.append(i)
    
out= max(ls1)
print(out)
n = ls1.remove(out)
o = max(ls1)
print(o)
