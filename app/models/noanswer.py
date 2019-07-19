"""
author          : nsuhara <na010210dv@gmail.com>
date created    : 2019/5/1
python version  : 3.7.3
"""
import datetime
import json
import logging

from linebot.models.actions import PostbackAction, URIAction
from linebot.models.template import ButtonsTemplate, TemplateSendMessage

from app.framework.nslinebot.models.story_board import StoryBoard
from app.processes.trash import Process
from linebot.models.messages import TextMessage

logger = logging.getLogger(__name__)


class noanswer(StoryBoard):
    def __init__(self):
        super().__init__()
        process = Process()
        self.PROCESS = {
            'noanswer_pro': process.what_day_of_garbage_is_today
        }

    def process_handler(self, kwargs):
        logger.info('process_handler:{}'.format(kwargs))
        return self.PROCESS.get(kwargs.get('handle'))()

    def story_board(self, text):
        return {
# answer             
            'answer': TextMessage(text='すみません。会話を理解できませんでした。' + '\n' + '[メニュー]と頂ければメインメニューを表示しますよ。')
        }
