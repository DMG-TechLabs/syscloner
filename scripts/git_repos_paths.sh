#!/bin/bash

if [ $# -eq -0 ]
    then
        echo "No arguments supplied"
fi

find /home -name ".git" | head -n $1 | tail +$1
