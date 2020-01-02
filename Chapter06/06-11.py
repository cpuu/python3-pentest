#!/usr/bin/env python3

import ftplib

ftp = ftplib.FTP("192.168.10.213")
ftp.login(user = "anonymous", passwd = "")

lists = []
ftp.dir(lists.append)
for line in lists:
	print(line)

ftp.quit()
