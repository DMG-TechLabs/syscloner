#!/bin/bash

egrep -r "^deb " /etc/apt/* | egrep -o ":.*"
