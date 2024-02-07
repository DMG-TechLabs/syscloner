#!/bin/bash

# for i in $num_of_repos
# do
#     git_repos_path[$i]=$(find /home -name ".git" | head -n $i)
# done

# for str in ${git_repos_path[@]}
# do
#     echo $str
# done
if [ $# -eq -0 ]
    then
        echo "No arguments supplied"
fi

find /home -name ".git" | head -n $1 
