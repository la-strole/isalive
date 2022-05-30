""" Send notification to telegram chat.
Bot name is @isalivenotification_bot.

"""
import telebot


class telegram_bot:

    def __init__(self):
        self.bot = telebot.TeleBot("5346758240:AAFofsIDkIClcdRued7-AfqMflAUog2Yr-Q")
        self.notification_text = 'Помер!'

    def get_chat_ids(self):

        @self.bot.message_handler(commands=["start", ])
        def send_welcome(message):
            self.bot.reply_to(message, "Как только - так сразу!")

            with open('chat_ids.csv', 'a') as file:
                file.write(str(message.chat.id))

        self.bot.infinity_polling()

    def stop_bot(self):
        self.bot.stop_polling()

    def send_notification(self):
        # print(f'here is ids {self.chat_ids}')
        with open('./chat_ids.csv') as file:
            for chatid in file.readlines():
                self.bot.send_message(chat_id=int(chatid), text=self.notification_text)


if __name__ == "__main__":
    new_bot = telegram_bot()
    new_bot.get_chat_ids()

