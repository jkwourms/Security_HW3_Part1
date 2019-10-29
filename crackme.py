#!/usr/bin/env python
import sys

def getSerial(username):
    inputSum = 0
    for i in username:
        inputSum += ord(i)
    return inputSum ^ 0x444c

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print "Name: %s <username>" % sys.argv[0]
        sys.exit(1)
    print "Serial: %s" % getSerial(sys.argv[1].upper())