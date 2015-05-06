#!/usr/bin/env python3
#-*- coding: utf-8 -*-


from lib.log import log_file
from lib.A import A
from lib.B import B


if __name__ == "__main__":
    log = log_file("mytest.log", log="main")
    logger = log.getlogger()
    logger.info("from main function")
    a = A(log)
    b = B(log)
