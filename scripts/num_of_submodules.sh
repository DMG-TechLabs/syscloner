#!/bin/bash

find $1 -name ".gitmodules" | egrep -o "*/.*/" | wc -l
