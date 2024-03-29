"""
author          : nsuhara <na010210dv@gmail.com>
date created    : 2019/5/1
python version  : 3.7.3
"""
import logging

logger = logging.getLogger(__name__)

# メッセージの各挙動を共通化している
class Messenger(object):
# 初期化
    def __init__(self):
        self._SEND = {
            'reply': self._reply_message,
            'push': self._push_message
        }

# 送信
    def send(self, line_bot_api, reply_token, messages, method):
        self._SEND.get(method)(line_bot_api, reply_token, messages)

# 返信
    def _reply_message(self, line_bot_api, reply_token, messages):
        logger.info('_reply_message:{}'.format(messages))
#        print(messages)
        line_bot_api.reply_message(reply_token, messages, timeout=None)

# プッシュメッセージ
    def _push_message(self, line_bot_api, to, messages):
        logger.info('_push_message:{}'.format(messages))
        line_bot_api.push_message(to, messages, timeout=None)
