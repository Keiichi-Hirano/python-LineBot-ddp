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
from app.processes.ddp import Process

# DDP_check_process

logger = logging.getLogger(__name__)

class Ddp(StoryBoard):
    def __init__(self):
        super().__init__()
        process = Process()
        self.PROCESS = {
            'DDP_check_process': process.DDP_check_process
        }

    def process_handler(self, kwargs):
        logger.info('process_handler:{}'.format(kwargs))
#        print(kwargs.get('handle'))

#        res = process.post((kwargs.get('handle')),kwargs.get('user_id'))
#        return '{}\n{}'.format(res.get('message'), res.get('timestamp'))
        print(kwargs.get('check5'))

        return self.PROCESS.get(kwargs.get('handle'))(
                            kwargs.get('check1'),
                            kwargs.get('check2'),
                            kwargs.get('check3'),
                            kwargs.get('check4'),
                            kwargs.get('check5'))
#        process = Process()
#        res = process.post((kwargs.get('handle')),
#                            kwargs.get('check1'),
#                            kwargs.get('check2'),
#                            kwargs.get('check3'),
#                            kwargs.get('check4'),
#                            kwargs.get('check5')        
#                            )
#        return '{}\n{}'.format(res.get('message'), res.get('timestamp'))

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
                                'scene': 'check4',
                                'model': 'ddp',
                                'check1':'check1','check2':'check2','check3':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check4',
                                'model': 'ddp',
                                'check1':'check1','check2':'check2','check3':'N'
                            })
                        )
                    ]
                )
            ),
#  check4 
            'check4': TemplateSendMessage(
                alt_text='ButtonsTemplate',
                template=ButtonsTemplate(
                    title='データの利用に即時性は求められますか？',
                    text=text if text else '選択して下さい',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5',
                                'check1':'check1',
                                'check2':'check2',
                                'check3':'check3',
                                'check4':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check5',
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
                    title='分析機能は実装しますか？',
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
                                'check5':'Y',
                                'process': {'handle': 'DDP_check_process'}
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
