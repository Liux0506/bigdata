# -*- coding: utf-8 -*-
# @Time    : 2018/2/27 11:15
# @Author  : Liunux
# @Email   : 103996977@qq.com
# @File    : FtpTools.py
# @Software: PyCharm

###python FtpTools.py 'gz' '20180227' >fileLog.txt

import sys,os,ftplib,socket

Host="132.121.126.87"
Port=2121
User="*****"    #需手动输入
Password="******"   #需手动输入

city=sys.argv[1]
date=sys.argv[2]
dictory=city+'/'+date

def connect():
    try:
        ftp=ftplib.FTP()
        ftp.connect(host=Host,port=Port)
        ftp.login(user=User,passwd=Password)
        print("成功登陆", Host)
        return  ftp
    except (socket.error,socket.gaierror):
        print ("FTP登录失败")
        sys.exit(0)

def disconnect(ftp):
    ftp.quit()

def getFileList(ftp):
    ftp.cwd(dictory)
    ftp.dir()

if __name__ == '__main__':
    ftp=connect()
    getFileList(ftp)
    disconnect(ftp)
