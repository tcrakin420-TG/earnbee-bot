import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Bot token and Web App URL
BOT_TOKEN = '7836059311:AAFPMFQndSTUEp3zRd01c8hRfyGQt7-shxY'
WEB_APP_URL = 'https://earn-bee.vercel.app/'

# Initialize bot
bot = telebot.TeleBot(BOT_TOKEN)

# /start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = (
        "Welcome to EarnBee! 🎉\n"
        "You can now earn money 💰 by watching ads 🎥.\n"
        "No sign-up required, just follow the steps below:\n"
        "1️⃣ Start watching ads to earn 🤑.\n"
        "2️⃣ Withdraw your earnings 💳 BY ADMIN.\n"
        "      To get started, simply click below to begin watching ads! 🚀"
    )

    keyboard = InlineKeyboardMarkup()
    watch_ads_button = InlineKeyboardButton("🎬 Start Watching Ads", web_app=WebAppInfo(url=WEB_APP_URL))
    keyboard.add(watch_ads_button)

    bot.send_message(message.chat.id, welcome_text, reply_markup=keyboard)

# /about command handler
@bot.message_handler(commands=['about'])
def about_info(message):
    about_text = (
        "👨‍💻 Developer & Admin: @tcrakin420\n"
        "📢 For any issues, contact the admin above."
    )
    bot.send_message(message.chat.id, about_text)

# Start polling
print("✅ EarnBee bot is running...")
bot.infinity_polling()
