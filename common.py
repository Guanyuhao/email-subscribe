# !/usr/bin/env python
# coding=utf-8

import os
import datetime

FALL_IN_LOVE = (2015, 7, 2)

# 隐私数据存放在环境变量中
MAIL_HOST = os.environ.get("MAIL_HOST")
MAIL_USER = os.environ.get("MAIL_USER")
MAIL_PASS = os.environ.get("MAIL_PASS")
MAIL_SENDER = os.environ.get("MAIL_SENDER")
MAIL_RECEIVER = os.environ.get("MAIL_RECEIVER")

MAIL_ENCODING = "utf8"


def get_loving_days():
    """
    获取恋爱天数
    """
    today = datetime.datetime.today()
    anniversary = datetime.datetime(*FALL_IN_LOVE)
    return (today - anniversary).days
