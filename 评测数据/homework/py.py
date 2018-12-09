import os
import sys
for i in range(1,11):
    fs=open(str(i)+".in","r")
    fd=open(str(i)+".out","r")
    fa=open("homework"+str(i)+".in","w+")
    fb=open("homework"+str(i)+".out","w+")
    fa.write(fs.read())
    fb.write(fd.read())
    fs.close()
    fd.close()
    fa.close()
    fb.close()
