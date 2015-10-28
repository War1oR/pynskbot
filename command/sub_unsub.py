__author__ = 'warior'
__date__ = '28.10.2015'


def sub(bot, message, members):
    if message.chat_id in members:
        bot.sendMessage(chat_id=message.chat_id,
                        text="You are already subscribed.")
    else:
        members.append(message.chat_id)
        bot.sendMessage(chat_id=message.chat_id,
                        text="You are subscribed to the newsletter.")
    return members

def unsub(bot, message, members):
    global MEMBERS
    if message.chat_id in members:
        members.remove(message.chat_id)
        bot.sendMessage(chat_id=message.chat_id,
                        text="You are unsubscribe from the newsletter.")
    else:
        bot.sendMessage(chat_id=message.chat_id,
                        text="You are not subscribed yet")
    return members