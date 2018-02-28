# -*- coding: utf-8 -*-
# @Time    : 2018/2/24 10:23
# @Author  : Liunux
# @Email   : 103996977@qq.com
# @File    : reduce.py.py
# @Software: PyCharm

#!/usr/bin/env python
import sys

# hello   1
# world   1
# python  1
# world   1
words_dict={}
for line in sys.stdin:
    line=line.strip()
    word,count=line.split("\t")
    try:
        count=int(count)
        words_dict[word]=words_dict.get(word,0)+count
    except ValueError:
        pass

for word,count in words_dict.items():
    print ("%s\t%s" % (word,count))




# import sys
#
# def read_map_output(file):
#     for line in file:
#         yield line.strip().split("  ",1)
#
# def main():
#     file=read_map_output(sys.stdin)
#     cur_word=None
#     cur_count=0
#     for word,count in file:
#         try:
#             count=int(count)
#         except ValueError:
#             continue
#         if cur_word==word:
#             cur_count=cur_count+1
#         else:
#             if cur_word:
#                 print (cur_word,"\t",cur_count)
#         cur_word=word
#         cur_count=count
#
# if __name__=="__main__":
#     main()