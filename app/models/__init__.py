from .clock_in import ClockIn
from .main_menu import MainMenu
from .trash import Trash
from .ddp import  Ddp

MODELS = {
    'main_menu': MainMenu,
    'clock_in': ClockIn,
# 2019/07/03 add start 
# DDP条件メニュー
    'trash': Trash,
    'ddp': Ddp
# 2019/07/03 add end 
}

MESSAGE_MODELS = {
    'メインメニュー': {
        'model': 'main_menu',
        'scene': 'menu'
    },
    '勤怠メニュー': {
        'model': 'clock_in',
        'scene': 'menu'
    },
    'ごみ出しメニュー': {
        'model': 'trash',
        'scene': 'menu'
# 2019/07/03 add start 
# DDP条件メニュー
    },
    'DDP利用メニュー': {
        'model': 'ddp',
        'scene': 'menu'
# 2019/07/03 add end 
    }
}
