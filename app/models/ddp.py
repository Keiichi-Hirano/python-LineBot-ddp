"""
author          : nsuhara <na010210dv@gmail.com>
date created    : 2019/5/1
python version  : 3.7.3
"""
import datetime
import json
import logging
#
from linebot.models.actions import PostbackAction, URIAction
from linebot.models.template import ButtonsTemplate, TemplateSendMessage, ConfirmTemplate
#from linebot.models.send_messages import messages
from linebot.models.messages import TextMessage
#from linebot.models.send_messages import TextSendMessage

#
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
        return self.PROCESS.get(kwargs.get('handle'))(
        kwargs.get('check1'),
        kwargs.get('check2'),
        kwargs.get('check3'),
        kwargs.get('check4'),
        kwargs.get('check5'))

    def story_board(self, text):
#    def story_board(self, check_T, text):
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
                ),
            ),
#  check1 
            'check1': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='利用するトランデータは CokeOne データですか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check2a',
                                'check1':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check2b',
                                'model': 'ddp',
                                'check1':'N'
                            })
                        )
                    ]
                )
            ),   
#  check2a 
            'check2a': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='データは参照のみですか？更新用件はありませんか？',
                    actions=[
                        PostbackAction(\
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check3aa',
                                'check1':'Y',
                                'check2':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check3ab',
                                'model': 'ddp',
                                'check1':'Y',
                                'check2':'N'
                            })
                        )
                    ]
                )
            ),
#  check2b 
            'check2b': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='データは参照のみですか？更新用件はありませんか？',
                    actions=[
                        PostbackAction(\
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check3ba',
                                'check1':'N',
                                'check2':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check3bb',
                                'model': 'ddp',
                                'check1':'N',
                                'check2':'N'
                            })
                        )
                    ]
                )
            ),
#  check3aa
            'check3aa': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='処理結果の表示にUIは使用しますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'scene': 'check4',
                                'model': 'ddp',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check4',
                                'model': 'ddp',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'N'
                            })
                        )
                    ]
                )
            ),
#  check3ab
            'check3ab': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='処理結果の表示にUIは使用しますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'scene': 'check4',
                                'model': 'ddp',
                                'check1':'Y',
                                'check2':'N'
                                'check3':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check4',
                                'model': 'ddp',
                                'check1':'Y',
                                'check2':'N'
                                'check3':'N'
                            })
                        )
                    ]
                )
            ),
#  check4 
            'check4': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='データの利用に即時性は求められますか？',
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
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
#                                'scene': 'result',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'check1',
                                'check2':'check2',
                                'check3':'check3',
                                'check4':'check4',
                                'check5':'Y'}
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
#                                'scene': 'result',
                                'scene': 'answer',
                                'check1':'check1',
                                'check2':'check2',
                                'check3':'check3',
                                'check4':'check4',
                                'check5':'N',
                                'process': {'handle': 'DDP_check_process'}
                            })
                        )
                    ]
                )
            ),
# answer             
            'answer': TextMessage(text=text),
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
