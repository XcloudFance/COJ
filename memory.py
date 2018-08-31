#!/usr/bin/env python
# -*- coding: utf-8 -*-
# coding:gbk
import os, re,sys
import time
import threading
import string

#统计某一个进程名所占用的内存，同一个进程名，可能有多个进程
ret=0
def getret():
    global ret
    temp=ret
    ret=0
    return temp
def countProcessMemoey(processName,name2):
    pattern = re.compile(r'([^\s]+)\s+(\d+)\s.*\s([^\s]+\sK)')
    cmd = 'tasklist /fi "imagename eq ' + processName + '"' + ' | findstr.exe ' + processName
    result = os.popen(cmd).read()
    os.system("cd " + sys.path[0])
    os.system(name2)
    resultList = result.split("\n")

    for srcLine in resultList:
        srcLine = "".join(srcLine.split('\n'))
        if len(srcLine) == 0:
            break
        m = pattern.search(srcLine)
        if m == None:
            continue
        #由于是查看python进程所占内存，因此通过pid将本程序过滤掉
        if str(os.getpid()) == m.group(2):
            continue
        ori_mem = m.group(3).replace(',','')
        ori_mem = ori_mem.replace(' K','')
        ori_mem = ori_mem.replace(r'\sK','')
        memEach = int(ori_mem)
        print ('ProcessName:'+ m.group(1) + '\tPID:' + m.group(2) + '\tmemory size:%.2f'% (memEach * 1.0 /1024), 'M')
        #print()
        global ret
        ret=memEach * 1.0 / 1024
        return(ret)


    return(0)
    #os.system(name2)

if __name__ == '__main__':
    #进程名
    ProcessName = 'unite.exe'
    ProcessName2='unite.exe'


    while ret==0:
        ta = threading.Thread(target=countProcessMemoey, args= (ProcessName,ProcessName2))
        ta.start()
        #ta.join()

        #print(countProcessMemoey (ProcessName,ProcessName2))
        time.sleep(1)
    print(getret())