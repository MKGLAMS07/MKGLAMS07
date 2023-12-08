ls = []

while 1:
    item = input('enter the item.')
    if item == "":
        break
    ls.append(item)
    ls.sort()
    print(ls)

