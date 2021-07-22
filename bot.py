import requests
import json
import configparser as cfg
from telegram import ParseMode

class telegram_chatbot():
        def __init__(self):
            self.token = self.read_token_from_config_file()
            self.base = "https://api.telegram.org/bot{}/".format(self.token)

        def get_updates(self, offset=None):
            url = self.base + "getUpdates?timeout=100"
            if offset:
                url = url + "&offset={}".format(offset + 1)
                print("url: " + url)
            r = requests.get(url)
            return json.loads(r.content)

        def send_message(self, msg, chat_id):
            url = self.base + "sendMessage?chat_id={}&text={}&parse_mode={}".format(chat_id, msg,ParseMode.MARKDOWN)
            print(url)
            if msg is not None:
                requests.get(url)

        def read_token_from_config_file(self):
            parser = cfg.ConfigParser()
            config = r"config.cfg"
            parser.read(config)
            return parser.get("creds", "TRACKER_TELEBOT_API_KEY")
