#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from .log import Log
class A():
    def __init__(self):
        self.logger = Log(file=__file__, cla=type(self).__name__).logger
        self.logger.info('Hello from A')


