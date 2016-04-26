#!/bin/bash
set -e

AUTHOR="wind4869"
LEETCODE_URL=https://leetcode.com/problems/

function usage()
{
    echo -e "Usage: ${0} [url] [source_file]"
    echo -e ""
    echo -e "Example:"
    echo -e ""
    echo -e "   1) Create a file named largestNumber.cpp, and add Copyright & Problem description"
    echo -e "   ${0} https://leetcode.com/problems/largest-number/"
    echo -e ""
    echo -e "   2) Add Copyright & Problem description into existed file"
    echo -e "   ${0} https://leetcode.com/problems/largest-number/ largestNumber.cpp"
    echo -e ""
}

if [ $# -lt 1 ] || [[ "${1}" != ${LEETCODE_URL}* ]]; then
    usage
    exit 255
fi


leetcode_url=$1
current_time=`date +%Y-%m-%d`

if [ $# -gt 1 ] && [ -f $2 ]; then
    source_file=$2
    current_time=`gstat -c %x ${source_file} | gawk '{print \$1}'`
else
    source_file=${1#${LEETCODE_URL}}
    source_file=${source_file::${#source_file}-1}
    source_file=`echo $source_file | gawk -F '-' '{for (i=1; i<=NF; i++) printf("%s", toupper(substr($i,1,1)) substr($i,2)) }'`.cpp

    if [ ! -f ${source_file} ]; then
        echo "Create a new file - ${source_file}."
        echo -e "\n" > ${source_file}
        current_time=`date +%Y-%m-%d`
    else
        rm ${source_file}
        echo -e "\n" > ${source_file}
        current_time=`gstat -c %x ${source_file} | gawk '{print \$1}'`
    fi
fi

# adding the Copyright Comments
if  ! grep -Fq "// Author :" $source_file ; then
    gsed -i '1i\'"// Source : ${leetcode_url}" $source_file
    gsed -i '2i\'"// Author : ${AUTHOR}" $source_file
    gsed -i '3i\'"// Date   : ${current_time}\n" $source_file
fi

xidel ${leetcode_url} -q -e "css('div.question-content')"  | \
    grep -v '                ' |gsed '/^$/N;/^\n$/D'  | \
    gsed 's/^/ * /' | gsed "1i/*$(printf '%.0s*' {0..80}) \n * " | \
    gsed "\$a \ $(printf '%.0s*' {0..80})*/\n" > /tmp/tmp.txt

gsed -i '4 r /tmp/tmp.txt' ${source_file}

rm -f /tmp/tmp.txt

echo "${source_file} updated !"
