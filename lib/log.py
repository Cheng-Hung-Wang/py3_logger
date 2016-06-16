import logging
import os.path
from datetime import datetime

from setting import level

class Log():
    def __init__(self, *,file=__file__, cla=None, path=None, filename="analytics", console=True, format="full"):

        if(path is None):
            path = os.path.abspath(".")+"/log/"
        path = os.path.join(path, filename)

        # create logger with 'log=name'
        #self.name = '.'.join([log, self.__class__.__name__])
        #self.id = str(id(self))
        #self.id = self.id[len(self.id)-2:]
        #self.name = "_{} - {} - {}.".format(self.id, file, cla) if cla else "{} - ".format(file)
        self.name = "{} - {}.".format(file, cla) if cla else "{} - ".format(file)

        # 創建 logger  
        self.logger = logging.getLogger(self.name)
        self.logger.propagate = False
        self.logger.setLevel(level)
        self.console = console


        # create formatter and add it to the handlers
        #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #formatter = logging.Formatter("%(levelname) -10s %(asctime)s %(module)s:%(lineno)s %(funcName)s %(message)s")
        datefmt = '%Y-%m-%d %H:%M:%S'
        if format=="full":
            formatter = logging.Formatter("%(levelname)s - %(asctime)s - %(name)s%(funcName)s:%(lineno)s - %(message)s", datefmt)
        # simple log format
        else:
            formatter = logging.Formatter("%(asctime)s - %(message)s", datefmt)

        # create file handler (log save path and name) which logs even debug messages
        self.fh = logging.FileHandler(path+"_"+datetime.now().strftime("%Y-%m-%d")+".log")
        self.fh.setLevel(logging.DEBUG)
        self.fh.setFormatter(formatter)

        # create console handler with a higher log level
        self.ch = logging.StreamHandler()
        self.ch.setLevel(logging.DEBUG)
        self.ch.setFormatter(formatter)


        if len(self.logger.handlers)==0:
            # add the handlers to the logger
            self.logger.addHandler(self.fh)

            # add the handlers to the logger
            if self.console:
                self.logger.addHandler(self.ch)

    """
    def remove_handler(self):
        self.logger.removeHandler(self.fh)
        if self.console:
            self.logger.removeHandler(self.ch)
    def debug(self, msg):
        #self.add_handler()
        self.logger.debug(msg)
        #self.remove_handler()

    def info(self, msg):
        #self.add_handler()
        self.logger.info(msg)
        #self.remove_handler()

    def error(self, msg):
        #self.add_handler()
        self.logger.error(msg)
        #self.remove_handler()
    """
