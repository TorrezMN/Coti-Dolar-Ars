#!/bin/bash

# Get the current directory
DIR=$(pwd)

# List the directory contents every 1/2 minutes
while true; do
  # for i in {1..40}; do
    # echo '\n'
  # done
  # ls $DIR
  tree .
  # echo '========================================================'
  # echo '========================================================'
  # tree $DIR
  # echo '========================================================'
  # echo '========================================================'
  # echo '\n'
  # echo '\n'
  # echo '\n'
  # echo '##########################################################'
  # cat test1.txt
  # cat test2.txt
  echo '##########################################################'
  sleep 10
done
