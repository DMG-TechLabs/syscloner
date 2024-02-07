#!/bin/bash

if [ $# -eq -0 ]
    then
        echo "No arguments supplied"
fi

cd $1; git remote get-url $(git remote show)
