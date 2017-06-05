#!/usr/bin/python
import os,sys

f=open('/root/account.txt','a+')
d={}
for  line in f:
     line =line.split(':')
     d[line[0]]=line[1].strip('\n')
f.close()


while  True:
 	print "welcome to user system !!!"
	print ""
	print ""
	user_input=raw_input("please input action  'login or register or exit':")
	while  True:
        	if user_input == 'login':
	         	name=raw_input('name:').strip()
			if name == '' or name not in d:
				print "account input null or account not exist,please again"	
				continue
			passwd=raw_input('passswd:').strip()
			if passwd =='' :
				print "passwd input null"
				continue 
			elif passwd != d[name]:
				print "passwd wrong,please again"
				continue
		        else:
				print "welcome to %s"%(name)
				sys.exit()


		elif user_input == 'register':
			name=raw_input('name:').strip()
			if name=='':
				print "name not null,please again"
				continue
			passwd=raw_input('passwd:').strip()
			repasswd=raw_input('repasswd:').strip()
			if passwd =='' or  passwd !=repasswd :
				print " passswd not null or passwd not match,please again"
				continue
			else:
				f=open('/root/account.txt','a+')
				f.writelines(('%s:%s\n')%(name,passwd))
				print "account register successfull"
				sys.exit()
			
       		elif user_input == 'exit' or  user_input=='':
	   		 sys.exit()

