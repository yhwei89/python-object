#!/usr/bin/python
#coding:utf-8

f=open('access.log20170601')
d={}
l=[]
for  line in f:
      line=line.split(" ")
      remote_ip=line[14]
      if remote_ip in d:
	    d[remote_ip] +=1
      else:
	    d[remote_ip] =1
 
d2 = {}        
for k,v in d.items():
    d2.setdefault(v,[])
    d2[v].append(k)       

count = 0
f = open('access.html','a+')
f.write("<html><table style='border:solid 1px'>")
f.write("<th style='border:solid 1px'>访问次数</th><th style='border:solid 1px'>ip地址</th>")
while count < 10:
    key = max(d2.keys())
    for index in range(len(d2[key])):
        f.write('<tr><td style="border:solid 1px">%s</td><td style="border:solid 1px">%s</td></tr>' % (key,d2[key][index]))
    num = len(d2[key])
    d2.pop(key)
    count = count + num
f.write("</table></html>")
f.close()
