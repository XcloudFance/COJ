#未经允许不得给其他人使用
#此作品为石光中学初三七班蔡弘毅独立制作完成
#Cloud OpenJudge具体环境在根目录的"运行代码的必要条件"
import os
import sys
import time
from cmpcplus import *
from cmpclanguage import *
from task import *
from defender import *

class Getini:
    def getlink(self):
        fs=open("link.ini","r",encoding="gbk")
        String32=fs.read()
        f=String32.split("|")
        fs.close()
        return f
    def getrun(self,filename):
        fs=open("./评测数据/"+filename+"/run.ini","r",encoding="gbk")
        String32=fs.read()
        f=String32.split("|")
        fs.close()
        return f
os.system("del "+sys.path[0]+"\\demo.exe")
print("============================欢迎来到Cloud OpenJudge评测===================================")
print("请确定根目录有测试数据后开始执行")
'''
p=input("请输入文件名：")
t=input("请设置运行时间(秒单位)：")
maa=input("请设置内存限制大小(单位M)：")
exm=input("请输入数据个数:")
lang=input("请输入语言类型(c,cpp):")
'''
getini=Getini()
use=getini.getlink()
used=getini.getrun(use[0])
p=use[0]
lang=use[1]
t=used[0]
maa=used[1]
exm=used[2]
resultout=""
fs=open(p+".cpp","r")
sdsd=fs.read()
sdd=Defender()
fs.close()
if(not sdd.findsof(sdsd)):
    endres="DefenderError"
    print("result:"+endres)
    resultout+="result:"+endres
    fs=open("./result.txt","w+")
    fs.write(resultout)
    fs.close()
    exit()
    
if(lang!=" "):
    total=0
    endres="Accepted"
    if(lang=="cpp"):
        compiles=cplus()
        compiles.filename=p+".cpp"
    else:
        if(lang=="c"):
            compiles=cl()
            compiles.filename=p+".c"
        else:
            print("输入错误!请输入正确的语言")
    if(not compiles.compiletest()):
         endres="CompileError"
         print("您的总分为:"+str(total))
         resultout+="您的总分为:"+str(total)
         print("result:"+endres)
         resultout+="result:"+endres
         fs=open("./result.txt","w+")
         fs.write(resultout)
         fs.close()
         exit()
    compiles.run()
    if(not compiles.fileerrortest(p)):
                    endres="File Error"
                    print("您的总分为:"+str(total))
                    print("result:"+endres)
                    resultout+="您的总分为:"+str(total)
                    resultout+="result:"+endres
                    fs=open("./result.txt","w+")
                    fs.write(resultout)
                    fs.close()
                    exit()#.out都没有就直接break
    for i in range(0,int(exm)):
        fd=open("./评测数据/"+p+"/"+p+str(i)+".in","r+",encoding='gbk')
        ins=fd.read()
        fd.close()
        fd=open("./评测数据/"+p+"/"+p+str(i)+'.out',"r",encoding='gbk')
        outs=fd.read()
        fd.close()
        fd=open(p+".in","w+",encoding='gbk')
        fd.write(ins)
        fd.close()

        os.system("cd "+sys.path[0])
        ts=Task()
        fine=ts.read()
        tm=fine[0]
        print("time:"+str(tm)+"s")
        resultout+="time:"+str(tm)+"s\n"
        link=0
        g=0
        #这里插入task的检测内存赋值给G
        g=fine[1]
        print("memory:"+str(g)+"mb")
        resultout+="memory:"+str(g)+"mb"+"\n"
        if(g>int(maa)):
            print("Test "+str(i)+".out Memory Limit Exceeded")
            resultout+="Test "+str(i)+".out Memory Limit Exceeded"+"\n"
            endres = "Memory Limit Exceeded"
            continue
        if((tm)>float(t)):
            print("Test "+str(i)+".out Time Limit Exceeded")
            resultout+="Test "+str(i)+".out Time Limit Exceeded"+"\n"
            endres = "Time Limit Exceeded"
            continue
        fds = open(p + ".out", 'r', encoding='gbk')
        result = fds.read()
        fds.close()
        if(float(g)>float(maa)):
            print("Test " + str(i) + ".out Memory Limit Exceeded")
            resultout+="Test " + str(i) + ".out Memory Limit Exceeded"+"\n"
            endres = "Memory Limit Exceeded"
            continue
        '''if(not compiles.runtimetest(p)):
            endres="Runtime Error"
            print("Test " + str(i) + ".out Runtime Error")
            continue'''
        rte=fine[2]
        if(rte!=0):
            endres="Runtime Error"
            print("Test " + str(i) + ".out Runtime Error")
            resultout+="Test " + str(i) + ".out Runtime Error"+"\n"
            continue
        if( outs not in result and result not in outs):
            print(outs,result)
            print("Test "+str(i)+".out Wrong Answer")
            resultout+="Test "+str(i)+".out Wrong Answer"+"\n"
            endres="Wrong Answer"
        else:
            print("Test "+str(i)+".out Accepted")
            resultout+="Test "+str(i)+".out Accepted"+"\n"
            total+=20
        
        
print("您的总分为:"+str(total))
print("result:"+endres)
resultout+="您的总分为:"+str(total)
resultout+="result:"+endres
fs=open("./result.txt","w+")
fs.write(resultout)
fs.close()
#打印出res进行模拟结果
