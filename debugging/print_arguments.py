#!/usr/bin/python3
import sys

if len(sys.argv) > 1:
    for i in range(1, len(sys.argv)):  # Start from 1 to skip script name
        print(sys.argv[i])
else:
    print("No arguments provided.")

