#!/usr/bin/env python3
#-*- coding: utf-8 -*-


from lib import Log
from lib import A
from lib import B


if __name__ == "__main__":
    logger = Log(file=__file__, cla=__name__).logger
    logger.info("from main function")
    a = A()
    b = B()
