import telegram
from variables import BOT_DATA_UPDATE, AUTH_TOKEN

__author__ = 'warior'
__date__ = '28.10.2015'


class Bot():

    def __init__(self, cmd, auth, members=None):
        self.cmd = cmd
        self.members = members or []
        self.bot = telegram.Bot(AUTH_TOKEN)
        try:
            self.last_upd = self.bot.getUpdates()[-1].update_id
        except IndexError:
            self.last_upd = None

    def message_loop(self):
        for update in self.bot.getUpdates(offset=self.last_upd, timeout=BOT_DATA_UPDATE):
            print(update)
            message = update.message
            text = update.message.text
            if text in self.cmd:
                self.members = self.cmd[text](self.bot, message, self.members)
                self.last_upd = update.update_id + 1
            else:
                self.last_upd = update.update_id + 1