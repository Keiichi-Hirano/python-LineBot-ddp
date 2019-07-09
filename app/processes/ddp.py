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

    def DDP_check_process(self):
#    def DDP_check_process(self,check1,check2,check3,check4,check5):
#        if weekday == 2 and week_number == 4:
#        else:
#            return '{}は「{}」の日です\n({})'.format(WEEKDAY[weekday], GARBAGE[weekday], DETAIL.get(GARBAGE[weekday]))
            return '{}は「{}」です\n({})'.format('テスト','良好','もうひと息！')

#    def _get_week_number(self, date_time):
#        day = date_time.day
#        week_number = 0
#        while day > 0:
#            week_number += 1
#            day -= 7
#        return week_number
