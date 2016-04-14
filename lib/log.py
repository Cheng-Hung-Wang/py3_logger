import logging
import os.path
from datetime import datetime

class Log():
    def __init__(self, *, file=__file__, cla=__name__, path=None,console=True):

        if(path is None):
            path = os.path.abspath(".")+"/log/"

        # create logger with 'log=name'
        #self.name = '.'.join([log, self.__class__.__name__])
        self.name = "{} - {}.".format(file, cla)

        # 創建 logger  
        self.logger = logging.getLogger(self.name)
        self.logger.setLevel(logging.DEBUG)

        # create formatter and add it to the handlers
        #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #formatter = logging.Formatter("%(levelname) -10s %(asctime)s %(module)s:%(lineno)s %(funcName)s %(message)s")
        formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(name)s%(funcName)s:%(lineno)s - %(message)s")

        # create file handler (log save path and name) which logs even debug messages
        fh = logging.FileHandler(path+datetime.now().strftime("%Y-%m-%d")+".log")
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(formatter)
        # add the handlers to the logger
        self.logger.addHandler(fh)

        # create console handler with a higher log level
        if console:
            ch = logging.StreamHandler()
            ch.setLevel(logging.DEBUG)
            ch.setFormatter(formatter)
            # add the handlers to the logger
            self.logger.addHandler(ch)

