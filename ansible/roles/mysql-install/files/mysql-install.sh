#!/bin/bash

rpm -ivh mysql.rpm
systemctl enable mysqld
systemctl start mysqld

