import logging, logging.config
import json


class Logger(object):

    @staticmethod
    def getLogger(name, configJson):
        conf = json.loads(configJson)
        logging.config.dictConfig(conf)
        return logging.getLogger(name)