#!/bin/bash

apt list --installed | cut -d "/" -f1
