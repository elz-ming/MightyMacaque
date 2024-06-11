import os
import logging
from telegram.ext import MessageHandler, Updater, CommandHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

def start(update, context):
    update.message.reply_text('Hello! I am Mighty Macaque!')

def handle_message(update, context):
    text = update.message.text.lower()
    if 'hi' in text:
        update.message.reply_text('Hello there!')

def main():
    TOKEN = os.getenv('API_KEY')
    if not TOKEN:
        logger.error('No API_KEY found in environment variables')
        return
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
    updater.start_polling()   
    updater.idle()

if __name__ == '__main__':
    main()