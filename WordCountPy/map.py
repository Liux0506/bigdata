# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 14:38
# @Author  : Liunux
# @Email   : 103996977@qq.com
# @File    : map.py
# @Software: PyCharm
#!/usr/bin/env python
import sys

for line in sys.stdin:
    line.strip()
    words=line.split()
    for word in words:
        print ("%s\t%d" % (word,1))

# import sys
#
# def readLine(file):
#     for line in file:
#         line=line.strip()
#         words=line.split()
#         yield words
#
# def main():
#     file=sys.stdin
#     lines=readLine(file)
#     for words in lines:
#         for word in words:
#             print("{}  {}".format(word, 1))
#
# if __name__ == "__main__":
#   main()