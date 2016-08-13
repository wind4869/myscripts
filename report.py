#!/usr/local/bin/python

import os
import datetime

yesterday = datetime.datetime.strftime(datetime.date.today() - datetime.timedelta(days=1), '%Y%m%d')
os.popen('scp d67:/home/supertool/haoyouqiang/output/report_%s.csv .' % yesterday)
os.popen('csv2xls.py report_%s.csv' % yesterday)

