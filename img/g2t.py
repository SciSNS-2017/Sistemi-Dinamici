import sys

path = sys.argv[1]

# toglie le prime 7 righe e le ultime due

f = open(path,"r+")
lines = f.readlines()
f.seek(0)

for line in lines[7:-1]:
    f.write(line)    
    #print(line, end='', flush=True)

f.truncate()
f.close()
