#! /usr/bin/env python
# coding=utf-8
# HappyBirthdayZWT
# Author:LWD
# This code is used as an Easter Egg.
# lwd-temp@Github.com 2019 版权所有 © 保留所有权利。
# ZWT 开源许可证版本0.1
# 在符合下列条件的情况下，
# 特此免费向任何得到本授权作品的副本（包括源代码、文件和/或相关内容，以下统称为“授权作
# 品”）的个人和法人实体授权：
# 被授权个人或法人实体无权以任何目的处置授权作品：
# 1.个人或法人实体只被授权了对授权作品的阅读和执行权利，禁止修改、商用或作公开用途。
# 2.个人或法人实体必须铭记项目名称和授权作品有有效输出的具体执行时间。
# 3.个人或法人实体不得传播或向他人推荐授权作品。
# 该授权作品是"按原样"提供，不做任何明示或暗示的保证，包括但不限于对适销性、特定用途适用
# 性和非侵权性的保证。在任何情况下，无论是在合同诉讼、侵权诉讼或其他诉讼中，版权持有人均
# 不承担因本软件或本软件的使用或其他交易而产生、引起或与之相关的任何索赔、损害或其他责任。
def main():
    # For the most adorable one.
    import datetime
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
