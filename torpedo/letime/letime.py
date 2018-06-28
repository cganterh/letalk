from datetime import datetime as _datetime

from telegram.ext import CommandHandler as _CommandHandler


def _send_time(bot, update):
    time = _datetime.now().time()
    time_str = str(time)
    update.message.reply_text(time_str)


_handler = _CommandHandler('time', _send_time)
