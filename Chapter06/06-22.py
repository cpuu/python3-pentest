#!/usr/bin/env python3

import ftplib

ftp = ftplib.FTP("192.168.10.213")
ftp.login()

target = "backbox.txt"
copy = "windows.txt"

with open(copy, "w") as f:
        res = ftp.retrbinary("RETR " + target, f.write(copy))
        print(res)

ftp.quit()
