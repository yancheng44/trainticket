#!/usr/bin/env python
# -*- coding=utf-8 -*-

import logging
import logging.config

log_file = "tst.log"

logging.config.fileConfig('logging.conf')

# instance of logging

logger = logging.getLogger('tst')
logger.debug('debug msg')
logger.info('info msg')
logger.warn('warn msg')
logger.error('error msg')
logger.critical('critical msg')

