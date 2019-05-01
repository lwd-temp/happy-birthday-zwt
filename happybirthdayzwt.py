#! /usr/bin/env python
# coding=utf-8
# HappyBirthdayZWT
# Author:LWD
# This code is used as an Easter Egg.
def main():
    # For the most adorable one.
    date=datetime.datetime.today()
    if date.month==4:
        if date.day>=20:
            print("Happy birthday ZWT!")
    if date.month==5:
        if date.day==5:
            count=0
            while count!=4:
                print("Happy birthday ZWT!")
                count=count+1
        if date.day<=15:
            print("Happy birthday ZWT!")
