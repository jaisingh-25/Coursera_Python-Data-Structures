fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    a=line.split()
    for i in a:
        if i not in lst:
            lst.append(i)
print(sorted(lst))
