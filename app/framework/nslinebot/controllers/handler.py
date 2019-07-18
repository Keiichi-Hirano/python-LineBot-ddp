"""
author          : nsuhara <na010210dv@gmail.com>
date created    : 2019/5/1
python version  : 3.7.3
"""
import json
import logging

from app.framework.nslinebot.views.messenger import Messenger
from app.models import MESSAGE_MODELS, MODELS   

#menu_text = {'メニュー', 'うん','そう','Yes','Y','ええ','だな','です','ええ','そだね'}

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# メッセージの制御部分
# メッセージ受信時の制御
class MessageHandler(object):
# 初期化
    def __init__(self, line_bot_api, event):
        self._GET_EVENT = {
            'message': self._get_message_event,
            'postback': self._get_postback_event
        }
        self.line_bot_api = line_bot_api
        self.event = event
        self.event_type = event.type

# パラメーター値を元に各機能の呼び出し先を起動していると思われ・・・
    def handle_event(self):
        logger.info('handle_event:{}'.format(self.event))
        event_data = self._GET_EVENT.get(self.event_type)()
        if event_data is None:
            return

        model = event_data.get('model')
        scene = event_data.get('scene')
        process = event_data.get('process', None)
        method = event_data.get('method', 'reply')
        model_instance = MODELS.get(model)()
        text = model_instance.process_handler(process) if process else None
        messages = model_instance.get_template(scene, text)
        Messenger().send(self.line_bot_api, self.event.reply_token, messages, method)

# models配下のpythonを起動してる？
    def _get_message_event(self):
        original = self.event.message.text
        r_text = ''
        if original in ('勤怠','きんたい'):
            r_text = '勤怠メニュー'
        elif  original in ('ごみ','ゴミ'):
            r_text = 'ごみ出しメニュー'
        elif  original in ('DDP','ddp','Ddp'):
            r_text = 'DDP利用メニュー'
        elif  original in ('メニュ','めにゅ'):
            r_text = 'メインメニュー'
        else:
            r_text = 'noanswer'
#        return MESSAGE_MODELS.get(self.event.message.text, None)
        return MESSAGE_MODELS.get(r_text, None)

# json load で過去のやり取りを取得している？ 
    def _get_postback_event(self):
        return json.loads(self.event.postback.data)

# メッセージ送信時の制御
class PostbackHandler(object):
    def __init__(self, event):
        self._EVENT = {
            'process': self.process
        }
        self.event = json.loads(event)
        self.event_type = self.event.get('type')
        self.event_data = self.event.get('data')

# どうやってここに制御が来るのかわからない
    def handle_event(self):
        logger.info('handle_event:{}'.format(self.event))
        return self._EVENT.get(self.event_type)(self.event_data)

# どうやってここに制御が来るのかわからない
    def process(self, data):
        model = data.get('model')
        process = data.get('process', None)
        model_instance = MODELS.get(model)()
#        print(process,data)
        return model_instance.process_handler(process)
