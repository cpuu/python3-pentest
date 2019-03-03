#!/usr/bin/env python3

import ftplib

ftp = ftplib.FTP("192.168.10.213")
ftp.login()

entries = ftp.nlst()
print(entries)

ftp.quit()
