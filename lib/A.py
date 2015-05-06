#!/usr/bin/env python3
#-*- coding: utf-8 -*-


class A():
    def __init__(self, log):
        self.logger = log.addSubLogger(__name__)
        self.logger.info('Hello from A')


