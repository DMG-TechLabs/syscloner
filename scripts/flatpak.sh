#!/bin/bash

flatpak list | tr -s '\t' | cut -d$'\t' -f1
