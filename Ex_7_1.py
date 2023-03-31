fname=input("Enter file name: ")
fh = open(fname, 'r')
for lx in fh:
    lz=lx.rstrip()
    print(lz)
    print(lz.upper())




