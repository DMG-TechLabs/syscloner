#!/bin/bash

egrep -r "^deb " /etc/apt/* | cut -d ':' -f 1
