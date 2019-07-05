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

logger = logging.getLogger(__name__)


class Ddp(StoryBoard):
    def __init__(self):
        super().__init__()
        process = Process()
        self.PROCESS = {
            'what_day_of_garbage_is_today': process.what_day_of_garbage_is_today
        }

    def process_handler(self, kwargs):
        logger.info('process_handler:{}'.format(kwargs))
        return self.PROCESS.get(kwargs.get('handle'))()

    def story_board(self, text):
        return {
# menu            
            'menu': TemplateSendMessage(
                alt_text='ButtonsTemplate',
                template=ButtonsTemplate(
                    title='DDP利用メニュー',
                    text=text if text else '選択して下さい',
                    actions=[
                        PostbackAction(
                            label='DDP利用判定開始',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check1'
                            })
                        ),
                        PostbackAction(
                            label='戻る',
                            data=json.dumps({
                                'model': 'main_menu',
                                'scene': 'menu'
                            })
                        )
                    ]
                )
            ),
#  check1 
            'check1': TemplateSendMessage(
                alt_text='ButtonsTemplate',
                template=ButtonsTemplate(
                    title='利用するトランデータは CokeOne データですか？',
                    text=text if text else '選択して下さい',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check2',
                                'check1':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check2',
                                'model': 'ddp',
                                'check1':'N'
                            })
                        )
                    ]
                )
            ),
#  check2 
            'check2': TemplateSendMessage(
                alt_text='ButtonsTemplate',
                template=ButtonsTemplate(
                    title='データは参照のみですか？更新用件はありませんか？',
                    text=text if text else '選択して下さい',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check3',
                                'check1':'check1',
                                'check2':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check3',
                                'model': 'ddp',
                                'check1':'check1',
                                'check2':'N'
                            })
                        )
                    ]
                )
            ),
#  check3 
            'check3': TemplateSendMessage(
                alt_text='ButtonsTemplate',
                template=ButtonsTemplate(
                    title='処理結果の表示にUIは使用しますか？',
                    text=text if text else '選択して下さい',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'checK4',
                                'check1':'check1',
                                'check2':'check2',
                                'check3':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'checK4',
                                'model': 'ddp',
                                'check1':'check1',
                                'check2':'check2',
                                'check3':'N'
                            })
                        )
                    ]
                )
            ),
#  check4 
            'check4': TemplateSendMessage(
                alt_text='ButtonsTemplate',
                template=ButtonsTemplate(
                    title='処理結果の表示にUIは使用しますか？',
                    text=text if text else '選択して下さい',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'checK5',
                                'check1':'check1',
                                'check2':'check2',
                                'check3':'check3',
                                'check4':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'checK5',
                                'model': 'ddp',
                                'check1':'check1',
                                'check2':'check2',
                                'check3':'check3',
                                'check4':'N'
                            })
                        )
                    ]
                )
            ),
#  check5 
            'check5': TemplateSendMessage(
                alt_text='ButtonsTemplate',
                template=ButtonsTemplate(
                    title='処理結果の表示にUIは使用しますか？',
                    text=text if text else '選択して下さい',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'check1':'check1',
                                'check2':'check2',
                                'check3':'check3',
                                'check4':'check4',
                                'check5':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'answer',
                                'model': 'ddp',
                                'check1':'check1',
                                'check2':'check2',
                                'check3':'check3',
                                'check4':'check4',
                                'check5':'N'
                            })
                        )
                    ]
                )
            ),
# result             
            'result': TemplateSendMessage(
                alt_text='ButtonsTemplate',
                template=ButtonsTemplate(
                    title='DDP利用メニュー',
                    text=text if text else '取得できませんでした',
                    actions=[
                        PostbackAction(
                            label='戻る',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'menu'
                            })
                        )
                    ]
                )
            )

        }
