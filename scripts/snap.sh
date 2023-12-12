#!/bin/bash

snap list | tr -s " " | cut -d " " -f1 | tail -n +2
