#!/bin/bash

if [ $# -eq -0 ]
    then
        echo "No arguments supplied"
fi

find $2 -name ".git" | head -n $1 | tail +$1 | egrep -o "^/.*/"
