#!/bin/bash

find $2 -name ".gitmodules" | egrep -o "^/.*/" | head -n $1 | tail +$1
