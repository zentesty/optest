import logging

logger = logging.getLogger()
handler = logging.StreamHandler()
fh = logging.FileHandler('super_log_info.log')

formatter = logging.Formatter(
        '%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
handler.setFormatter(formatter)
fh.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(fh)

logger.setLevel(logging.DEBUG)

# create file handler which logs even debug messages


logger.debug('often makes a very good meal of %s', 'visiting tourists')
