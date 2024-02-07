#!/bin/bash

if [ $# -eq -0 ]
    then
        echo "No arguments supplied"
fi

# echo $1 | egrep "^b" | cut -d "'" -f2 | cut -d "\\" -f1

cd $1; git remote get-url $(git remote show)
