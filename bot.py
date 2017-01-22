from telegram.ext import Updater
from telegram.ext import CommandHandler

def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="Hey!... funziono!")


def main():
    updater = Updater(token='253084551:AAHOSlAHui8H-DkeJzj--MVeRo4PUFZZiC4')
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
