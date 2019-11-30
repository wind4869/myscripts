#!/usr/local/bin/python3

import os
import sys
import pandas

filename = sys.argv[1]
csv = pandas.read_csv(filename, encoding='utf-8')
csv.to_excel(filename.split('.')[0] + '.xls', index=False, encoding='utf-8')

