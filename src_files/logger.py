import logging

"""
logging levels:
CRITICAL
ERROR
WARNING
INFO
DEBUG
NOTSET
"""


_log_level = logging.DEBUG

logger = logging.getLogger('log_info')
logger.setLevel(_log_level)
handler = logging.FileHandler('load.txt')
handler.setLevel(_log_level)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s',
                              '%Y-%m-%d %H:%M:%S')
handler.setFormatter(formatter)
logger.addHandler(handler)

streamer = logging.StreamHandler()
streamer.setLevel(_log_level)
streamer.setFormatter(formatter)
logger.addHandler(streamer)


def get_logger():
    return logger