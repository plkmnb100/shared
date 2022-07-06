import pymysql
import logging

class DBLogHandler(logging.Handler):
    def __init__(self, table_name):
        logging.Handler.__init__(self)
        self.table_name = table_name
        #self.connect = pymysql.connect(host='localhost', user='root', passwd='', db='dblogger')
        #self.cursor = self.connect.cursor()

    def emit(self, record):
        print(record.__dict__)


logger = logging.getLogger('bh')
logger.addHandler(DBLogHandler('log'))
logger.warning("Oh Fuck {}".format("You"))