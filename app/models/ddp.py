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
                                'scene': 'check01'
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
#  check01 
            'check01': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='利用するトランデータは CokeOne データですか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check02Y',
                                'check1':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check02N',
                                'model': 'ddp',
                                'check1':'N'
                            })
                        )
                    ]
                )
            ),   
#  check02Y 
            'check02Y': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='データは参照のみですか？更新用件はありませんか？',
                    actions=[
                        PostbackAction(\
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check3YY',
                                'check1':'Y',
                                'check2':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check3YN',
                                'model': 'ddp',
                                'check1':'Y',
                                'check2':'N'
                            })
                        )
                    ]
                )
            ),
#  check02N 
            'check02N': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='データは参照のみですか？更新用件はありませんか？',
                    actions=[
                        PostbackAction(\
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check3NY',
                                'check1':'N',
                                'check2':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check3NN',
                                'model': 'ddp',
                                'check1':'N',
                                'check2':'N'
                            })
                        )
                    ]
                )
            ),
#  check3YY
            'check3YY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='処理結果の表示にUIは使用しますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'scene': 'check4YYY',
                                'model': 'ddp',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check4YYN',
                                'model': 'ddp',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'N'
                            })
                        )
                    ]
                )
            ),
#  check3YN
            'check3YN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='処理結果の表示にUIは使用しますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'scene': 'check4YNY',
                                'model': 'ddp',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check4YNN',
                                'model': 'ddp',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'N'
                            })
                        )
                    ]
                )
            ),
#  check3NY
            'check3NY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='処理結果の表示にUIは使用しますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'scene': 'check4NYY',
                                'model': 'ddp',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check4NYN',
                                'model': 'ddp',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'N'
                            })
                        )
                    ]
                )
            ),
#  check3NN
            'check3NN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='処理結果の表示にUIは使用しますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'scene': 'check4NNY',
                                'model': 'ddp',
                                'check1':'N',
                                'check2':'N',
                                'check3':'Y'
                            })
                        ),
                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'scene': 'check4NNN',
                                'model': 'ddp',
                                'check1':'N',
                                'check2':'N',
                                'check3':'N'
                            })
                        )
                    ]
                )
            ),
#---------#---------#---------#---------#---------
#  check4 
#---------#---------#---------#---------#---------
#            'check4': TemplateSendMessage(
#                alt_text='ConfirmTemplate',
#                template=ConfirmTemplate(
#                    text='データの利用に即時性は求められますか？',
#                    actions=[
#                        PostbackAction(
#                            label='Yes',
#                            data=json.dumps({
#                                'model': 'ddp',
#                                'scene': 'check5',
#                                'check1':'check1',
#                                'check2':'check2',
#                                'check3':'check3',
#                                'check4':'Y'
#                            })
#                        ),
#                        PostbackAction(
#                            label='No',
#                            data=json.dumps({
#                                'scene': 'check5',
#                                'model': 'ddp',
#                                'check1':'check1',
#                                'check2':'check2',
#                                'check3':'check3',
#                                'check4':'N'
#                            })
#                        )
#                    ]
#                )
#            ),
#  check4YYY
            'check4YYY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='データの利用に即時性は求められますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5YYYY',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'Y',
                                'check4':'Y'
                            })
                        ),

                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5YYYN',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'Y',
                                'check4':'N'
                            })
                        )
                    ]
                )
            ),
#  check4YYN
            'check4YYN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='データの利用に即時性は求められますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5YYNY',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'N',
                                'check4':'Y'
                            })
                        ),

                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5YYNN',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'N',
                                'check4':'N'
                            })
                        )
                    ]
                )
            ),
#  check4YNY
            'check4YNY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='データの利用に即時性は求められますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5YNYY',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'Y',
                                'check4':'Y'
                            })
                        ),

                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5YNYN',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'Y',
                                'check4':'N'
                            })
                        )
                    ]
                )
            ),
#  check4YNN
            'check4YNN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='データの利用に即時性は求められますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5YNNY',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'N',
                                'check4':'Y'
                            })
                        ),

                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5YNNN',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'N',
                                'check4':'N'
                            })
                        )
                    ]
                )
            ),
#  check4NYY
            'check4NYY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='データの利用に即時性は求められますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5NYYY',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'Y',
                                'check4':'Y'
                            })
                        ),

                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5NYYN',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'Y',
                                'check4':'N'
                            })
                        )
                    ]
                )
            ),
#  check4NYN
            'check4NYN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='データの利用に即時性は求められますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5NYNY',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'N',
                                'check4':'Y'
                            })
                        ),

                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5NYNN',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'N',
                                'check4':'N'
                            })
                        )
                    ]
                )
            ),
#  check4NNY
            'check4NNY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='データの利用に即時性は求められますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5NNYY',
                                'check1':'N',
                                'check2':'N',
                                'check3':'Y',
                                'check4':'Y'
                            })
                        ),

                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5NNYN',
                                'check1':'N',
                                'check2':'N',
                                'check3':'Y',
                                'check4':'N'
                            })
                        )
                    ]
                )
            ),
#  check4NNN
            'check4NNN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='データの利用に即時性は求められますか？',
                    actions=[
                        PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5NNNY',
                                'check1':'N',
                                'check2':'N',
                                'check3':'N',
                                'check4':'Y'
                            })
                        ),

                        PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'check5NNNN',
                                'check1':'N',
                                'check2':'N',
                                'check3':'N',
                                'check4':'N'
                            })
                        )
                    ]
                )
            ),
#---------#---------#---------#---------#---------
#  check5 
#---------#---------#---------#---------#---------
#            'check5': TemplateSendMessage(
#                alt_text='ConfirmTemplate',
#                template=ConfirmTemplate(
#                    text='分析機能は実装しますか？',
#                    actions=[
#                        PostbackAction(
#                            label='Yes',
#                            data=json.dumps({
#                                'model': 'ddp',
##                                'scene': 'result',
#                                'scene': 'answer',
#                                'process': {'handle': 'DDP_check_process',
#                                'check1':'check1',
#                                'check2':'check2',
#                                'check3':'check3',
#                                'check4':'check4',
#                                'check5':'Y'}
#                            })
#                        ),
#                        PostbackAction(
#                            label='No',
#                            data=json.dumps({
#                                'model': 'ddp',
##                                'scene': 'result',
#                                'scene': 'answer',
#                                'process': {'handle': 'DDP_check_process',
#                                'check1':'check1',
#                                'check2':'check2',
#                                'check3':'check3',
#                                'check4':'check4',
#                                'check5':'Y'}
#                            })
#                        )
#                    ]
#                )
#            ),
#  check5YYYY
            'check5YYYY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'Y',
                                'check4':'Y',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'Y',
                                'check4':'Y',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5YYYN
            'check5YYYN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'Y',
                                'check4':'N',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'Y',
                                'check4':'N',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5YYNY
            'check5YYNY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'N',
                                'check4':'Y',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'N',
                                'check4':'Y',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5YYNN
            'check5YYNN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'N',
                                'check4':'N',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'Y',
                                'check3':'N',
                                'check4':'N',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5YNYY
            'check5YNYY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'Y',
                                'check4':'Y',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'Y',
                                'check4':'Y',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5YNYN
            'check5YNYN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'Y',
                                'check4':'N',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'Y',
                                'check4':'N',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5YNNY
            'check5YNNY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'N',
                                'check4':'Y',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'N',
                                'check4':'Y',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5YNNN
            'check5YNNN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'N',
                                'check4':'N',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'Y',
                                'check2':'N',
                                'check3':'N',
                                'check4':'N',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5NYYY
            'check5NYYY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'Y',
                                'check4':'Y',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'Y',
                                'check4':'Y',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5NYYN
            'check5NYYN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'Y',
                                'check4':'N',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'Y',
                                'check4':'N',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5NYNY
            'check5NYNY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'N',
                                'check4':'Y',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'N',
                                'check4':'Y',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5NYNN
            'check5NYNN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'N',
                                'check4':'N',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'Y',
                                'check3':'N',
                                'check4':'N',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5NNYY
            'check5NNYY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'N',
                                'check3':'Y',
                                'check4':'Y',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'N',
                                'check3':'Y',
                                'check4':'Y',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5NNYN
            'check5NNYN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'N',
                                'check3':'Y',
                                'check4':'N',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'N',
                                'check3':'Y',
                                'check4':'N',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5NNNY
            'check5NNNY': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'N',
                                'check3':'N',
                                'check4':'Y',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'N',
                                'check3':'N',
                                'check4':'Y',
                                'check5':'N'}
                            })
                        )
                    ]
                )
            ),
#  check5NNNN
            'check5NNNN': TemplateSendMessage(
                alt_text='ConfirmTemplate',
                template=ConfirmTemplate(
                    text='分析機能は実装しますか？',
                    actions=[
                         PostbackAction(
                            label='Yes',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'N',
                                'check3':'N',
                                'check4':'N',
                                'check5':'Y'}
                            })
                        ),

                         PostbackAction(
                            label='No',
                            data=json.dumps({
                                'model': 'ddp',
                                'scene': 'answer',
                                'process': {'handle': 'DDP_check_process',
                                'check1':'N',
                                'check2':'N',
                                'check3':'N',
                                'check4':'N',
                                'check5':'N'}
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
