import telegram
import tornado.ioloop
from command import cmd
from fix_tornado.ioloop import PeriodicCallback
from variables import AUTH_TOKEN, BOT_DATA_UPDATE

__author__ = 'warior'
__date__ = '27.10.2015'


def main(cmd):
    global LAST_UPDATE
    for update in bot.getUpdates(offset=LAST_UPDATE, timeout=BOT_DATA_UPDATE):
        print(update)
        message = update.message
        text = update.message.text

        if text in cmd:
            cmd[text](bot, message)
            LAST_UPDATE = update.update_id + 1
        else:
            LAST_UPDATE = update.update_id + 1



if __name__ == '__main__':
    print("start")
    bot = telegram.Bot(AUTH_TOKEN)
    try:
        LAST_UPDATE = bot.getUpdates()[-1].update_id
    except IndexError:
        LAST_UPDATE = None
    period = PeriodicCallback(main, cmd, 200)
    period.start()
    tornado.ioloop.IOLoop.current().start()