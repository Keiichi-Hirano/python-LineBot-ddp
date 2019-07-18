"""
author          : nsuhara <na010210dv@gmail.com>
date created    : 2019/5/1
python version  : 3.7.3
"""
import datetime
import logging

logger = logging.getLogger(__name__)


class Process(object):
    def __init__(self):
        pass

    def DDP_check_process(self,check1,check2,check3,check4,check5):
            return '1は{}/2は{}/3は{}/4は{}/5は{}です\n'.format(check1,check2,check3,check4,check5)
