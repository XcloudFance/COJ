'''import subprocess
import psutil

a=subprocess.Popen("cmd.exe /hello.exe",shell="true")
pids = psutil.pids()
print(a)'''
import os
import subprocess
import sys

print(os.system("g++ "+sys.path[0]+"\\hello.cpp"+" -o "+sys.path[0]+"\\hhh.exe"))
