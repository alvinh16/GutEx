#!/usr/bin/python3.8

infile = "objectlist.text"
outfile = "outlist.text"

readfile = open(infile, "r")
appfile = open(outfile, "a")

# [:-1] slices off the final character in the line ie \n
# rstrip("\r\n") specifically strips away the \n char
for line in readfile:
    print(line[:-1])
    appfile.write(line.rstrip("\r\n"))
appfile.close()
readfile.close()
