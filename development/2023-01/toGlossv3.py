#!/usr/bin/python3

import re, sys, subprocess,os

def main():
    # check_pass=False
    check_pass=check_command_args()
    if (check_pass!=True):
        print("Hello")
    else:
        print("goodbye")

def check_command_args():
    num_args=len(sys.argv)-1
    if(num_args!=0):
        return False
    else:
        return True

# def 

main()