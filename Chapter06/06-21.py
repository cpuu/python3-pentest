##!/usr/bin/env python3

import ftplib

ftp = ftplib.FTP("192.168.10.213")
ftp.login()

entries = ftp.nlst()
for entry in entries:
	f = open(entry, "w")
	res = ftp.retrbinary("RETR " + entry, f.write(entry))
	print(res)
	f.close()

ftp.quit()
