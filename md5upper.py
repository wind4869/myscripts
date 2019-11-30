#!/usr/local/bin/python2

import sys
import hashlib

print(hashlib.md5(sys.argv[1]).hexdigest().upper())

