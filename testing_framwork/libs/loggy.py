import logging
import time

logger = logging.getLogger("logoutpout.log").addHandler(logging.NullHandler())

FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
logger.basicConfig(format=FORMAT)


def run_all():
    in_time = int(round(time.time() * 1000))
    logger.info("In method " + in_time)
    while 1 < 5:
        in_call_time = int(round(time.time() * 1000))
        time.sleep(1.2)
        out_call_time = int(round(time.time() * 1000))
        logger.info("Internal call")
        print(f'----------------------')
    out_time = int(round(time.time() * 1000))
    logger.info("Out method " + out_time)


if __name__ == "__main__":
    run_all()
