#!/bin/bash

/usr/local/bin/ctags -R .
find . -name "*.h" -o -name "*.c" -o -name "*.cpp" > cscope.files
cscope -bkq -i cscope.files
rm cscope.files

