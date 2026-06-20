#!/bin/bash

echo $0 $1 $#

if [ $# -lt 2 ]; then
  echo "dame"
  exit 0
fi

dirname=${1^^}
mkdir $dirname

for ((i=0; i<${#2}; i++)); do
  alp=${2:i:1}
  touch $dirname/${alp^^}.py
done

exit 0
