#!/bin/bash


##install mysql
rpm -ivh /tmp/mysql.rpm
rm -rf /etc/my.cnf && cp /tmp/my.cnf /etc/my.cnf
systemctl enable mysqld && systemctl start mysqld
initpw=`grep  password /var/log/mysqld.log | awk '{print $11}'`
mysqladmin -uroot -p$(initpw) password 'newpw'
mysql -uroot -p'newpw' -e "grant all privileges  on *.* to 'xxx'@'10.0.1.%' identified by 'xxxx123456*' ;"
