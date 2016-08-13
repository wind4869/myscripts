#!/usr/local/bin/python

import sys
import pandas

filename = sys.argv[1]
xls = pandas.read_excel(filename, encoding='utf-8')
xls.to_csv(filename.split('.')[0] + '.csv', index=False, encoding='utf-8')

