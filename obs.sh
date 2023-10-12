#!/bin/bash

#shell script to print numbers 1 to 100

i=1
while [ $i -le 100 ]
do
    # echo $i
    touch file_$i.txt
    i=$(($i+1))
  done
