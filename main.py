import telegram
from variables import AUTH_TOKEN

__author__ = 'warior'
__date__ = '27.10.2015'


def main(cmd):
    bot = telegram.Bot(AUTH_TOKEN)

    try:
        last_update = bot.getUpdates()[-1].update_id
    except IndexError:
        last_update = None

    while True:
        for update in bot.getUpdates(offset=last_update, timeout=10):
            print(update)
            message = update.message
            text = update.message.text

            if text in cmd:
                cmd[text](bot, message)
                last_update = update.update_id + 1
            else:
                last_update = update.update_id + 1

def start(bot, message):
    bot.sendMessage(chat_id=message.chat_id,
                    text="Hi {}.\nDial /sub to subscribe and /unsub  to unsubscribe".format(message.chat.first_name))

if __name__ == '__main__':
    cmd = {
        "/start": start,
        "/help": start
    }
    main(cmd)