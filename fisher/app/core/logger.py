# -*- coding: utf-8 -*- 
# @Time : 2020/10/10 9:01 上午 
# @Author : hans.li
# @File : logger.py


import logging
import os
import datetime
from logging.handlers import BaseRotatingHandler


class Mylog:
    def __init__(self, app, fmt=None, handler=None):
        self._app = app
        self._fmt = fmt
        self._handler = handler
        self._log_config = self._app.config.get('LOG')
        self._logger = None
        self.init_logger()
        self.set_logger()

    def init_logger(self):
        print('=====', self._app.debug)
        if self._log_config['FILE'] and not self._app.debug:
            fmt = logging.Formatter(
                "%(asctime)s %(levelname)s %(process)d   ---  [%(threadName)s]"
                " - %(message)s" if not self._fmt else self._fmt
            )
            logging.basicConfig(level=logging.DEBUG)
            self._handler = RotatingFileHandler(
                    log_dir=self._log_config['DIR'],
                    max_bytes=self._log_config['SIZE_LIMIT'],
                    encoding='UTF-8'
                )

            self._handler.setFormatter(fmt)
            self._handler.setLevel(level=logging.DEBUG)
            self._app.logger.addHandler(self._handler)
        else:
            return

    def set_logger(self):
        self._logger = logging.getLogger(__name__)

    def get_logger(self):
        return self._logger


class RotatingFileHandler(BaseRotatingHandler):
    def __init__(self, log_dir='logs', mode='a', max_bytes=0, encoding=None, delay=False):
        if max_bytes > 0:
            mode = 'a'
        self._log_dir = log_dir
        self._suffix = ".log"
        self._year_month = datetime.datetime.now().strftime("%Y-%m")
        self.store_dir = os.path.join(self._log_dir, self._year_month)
        self._create_new_stream_if_not_exists(self.store_dir, open_stream=False)
        self.filename = datetime.datetime.now().strftime("%Y-%m-%d")
        filename = os.path.join(self.store_dir, self.filename) + self._suffix
        BaseRotatingHandler.__init__(self, filename, mode, encoding, delay)
        self.max_bytes = max_bytes

    def doRollover(self):
        pass

    def shouldRollover(self, record):
        pass

    def _create_new_stream_if_not_exists(self, store_dir, open_stream=True):
        if not os.path.exists(store_dir):
            print('========', store_dir)
            os.makedirs(store_dir)
            if open_stream:
                self.stream = self._open()
