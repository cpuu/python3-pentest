#!/usr/bin/env python3

import ftplib

ftp = ftplib.FTP("192.168.10.213")
ftp.login(user = "odj", passwd = "1234")

data = "windows.txt"

res = ftp.storbinary("STOR " + data, open(data, "rb"))

print(res)

ftp.quit()
