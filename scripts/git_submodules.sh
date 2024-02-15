#!/bin/bash

find "$2" -name ".gitmodules" | grep -o "^/.*/" | head -n "$1" | tail +"$1"
