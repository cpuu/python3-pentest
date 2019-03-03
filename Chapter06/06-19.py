#!/usr/bin/env python3

target = "python3"
copy = "strings.txt"

f = open(copy, "w")

print(f.write(target))

f.close()

f = open(copy, "r")

print(f.read())

f.close()
