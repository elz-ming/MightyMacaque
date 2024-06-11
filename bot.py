import os
from telegram.ext import MessageHandler, Updater, CommandHandler, filters

def start(update, context):
    update.message.reply_text('Hello! I am Mighty Macaque!')

def handle_message(update, context):
    text = update.message.text.lower()
    if 'hi' in text:
        update.message.reply_text('Hello there!')

def main():
    TOKEN = os.getenv('API_KEY')
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(filters.text & ~filters.command, handle_message))
    updater.start_polling()   
    updater.idle()

if __name__ == '__main__':
    main()