import tornado.ioloop
from bot import Bot
from command import cmd
from variables import AUTH_TOKEN

__author__ = 'warior'
__date__ = '27.10.2015'


print("start")
pynsk_bot = Bot(cmd, AUTH_TOKEN)
period = tornado.ioloop.PeriodicCallback(pynsk_bot.message_loop, 200)
period.start()
tornado.ioloop.IOLoop.current().start()