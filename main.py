from logging import getLogger, config
import yaml

logger = getLogger(__name__)


class AAA(object):
    def __init__(self):
        self.logger = getLogger('AAA.BBB')
        self.logger.debug("class name is {}".format(self.__class__.__name__))

    def do_something(self):
        self.logger.info("doing something")


def main():
    aaa = AAA()
    aaa.do_something()

    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == "__main__":
    config.dictConfig(
        yaml.load(open("logging.yaml").read(), Loader=yaml.SafeLoader))
    main()
