__author__ = 'warior'
__date__ = '28.10.2015'


def start(bot, message, members):
    bot.sendMessage(chat_id=message.chat_id,
                    text="Hello {}! In order to subscribe to the newsletter, you should "
                         "enter /sub. In order to unsubscribe from the newsletter, you "
                         "should enter /unsub.".format(message.chat.first_name))
    return members