#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import logging.handlers

def main():
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    handler = logging.handlers.TimedRotatingFileHandler("test.log", 'D')
    fmt = logging.Formatter("%(asctime)s - %(parameter)s - %(filename)s - %(function)s - %(lineno)s - %(levelname)s - %(message)s")
    handler.setFormatter(fmt)
    logger.addHandler(handler)

    logger.debug("debuf msg")
    logger.info("info msg")
    logger.warn("warn msg")
    logger.warning("warning msg")
    logger.error("error msg")
    logger.fatal("fatal msg")
    logger.critical("critical msg")

if __name__ == "__main__":
    main()