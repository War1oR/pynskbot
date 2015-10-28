__author__ = 'warior'
__date__ = '28.10.2015'


def start(bot, message):
    bot.sendMessage(chat_id=message.chat_id,
                    text="Hi {}.\nDial /sub to subscribe and /unsub  to unsubscribe".format(message.chat.first_name))