#!/usr/bin/env python3

target = "python3"
copy = "strings.txt"

with open(copy, "w") as f:
	print(f.write(target))

with open(copy, "r") as f:
	print(f.read())
