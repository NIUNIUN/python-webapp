#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
MUA:邮件用户代理
MTA:邮件传输代理
MDA:邮件投递代理

一封电子邮件的旅程就是：
发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人

如果编写程序来发送和接收邮件，本质上就是：
    编写MUA把邮件发到MTA；
   编写MUA从MDA上收邮件。

发邮件时，MUA和MTA使用的协议就是SMTP，后面的MTA到另一个MTA也是用SMTP协议。
        SMTP：Simple Mail Transfer Protocol

收邮件时，MUA和MDA使用的协议有两种：POP3和IMAP。
        POP：Post Office Protocol  V3
        IMAP：Internet Message Access Protocol V4


目前大多数邮件服务商都需要手动打开SMTP发信和POP收信的功能，否则只允许在网页登录：
'''