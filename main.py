import telegram
from command import cmd
from variables import AUTH_TOKEN, BOT_DATA_UPDATE

__author__ = 'warior'
__date__ = '27.10.2015'


def main(cmd):
    bot = telegram.Bot(AUTH_TOKEN)

    try:
        last_update = bot.getUpdates()[-1].update_id
    except IndexError:
        last_update = None

    while True:
        for update in bot.getUpdates(offset=last_update, timeout=BOT_DATA_UPDATE):
            print(update)
            message = update.message
            text = update.message.text

            if text in cmd:
                cmd[text](bot, message)
                last_update = update.update_id + 1
            else:
                last_update = update.update_id + 1



if __name__ == '__main__':
    main(cmd)