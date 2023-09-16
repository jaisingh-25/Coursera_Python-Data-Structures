fname = input("Enter file name: ")
fh = open(fname)
b=0
c=0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    a=float(line[20:])
    c+=1
    b+=a
print("Average spam confidence:", b/c)
