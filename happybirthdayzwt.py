#! /usr/bin/env python
# coding=utf-8
# HappyBirthdayZwt
# Author:LWD
# This code is used as an Easter Egg.
def main():
    from datetime import datetime
    date=datetime.today()
    if str(date.month)=="4":
        if int(date.day)>=20:
            print("Happy birthday ZWT!")
    if str(date.month)=="5":
        if str(date.day)=="5":
            count=0
            while count!=4:
                print("Happy birthday ZWT!")
                count=count+1
        if int(date.day)<=15:
            print("Happy birthday ZWT!")
