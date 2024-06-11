import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

def development_start():
    global API_KEY

    import dotenv

    dotenv.load_dotenv()

    API_KEY = os.getenv('API_KEY')

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = (
        "I'm a bot, please talk to me!\n\n"
        "Here are some commands you can use:\n"
        "/photo - Send a photo\n"
        "/audio - Send an audio\n"
        "/video - Send a video\n"
    )

    await context.bot.send_message(chat_id=update.effective_chat.id, text=message)

async def photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_photo(chat_id=update.effective_chat.id, photo=open('asset/bird_image.jpg', 'rb'))

async def audio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_audio(chat_id=update.effective_chat.id, audio=open('asset/bird_audio.mp3', 'rb'))

async def video(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_video(chat_id=update.effective_chat.id, video=open('asset/bird_video.mp4', 'rb'))

if __name__ == '__main__':
    API_KEY = os.getenv('API_KEY')

    # development_start()

    application = ApplicationBuilder().token(API_KEY).build()
    
    start_handler = CommandHandler('start', start)
    photo_handler = CommandHandler('photo', photo)
    audio_handler = CommandHandler('audio', audio)
    video_handler = CommandHandler('video', video)

    application.add_handler(start_handler)
    application.add_handler(photo_handler)
    application.add_handler(audio_handler)
    application.add_handler(video_handler)
    
    application.run_polling()