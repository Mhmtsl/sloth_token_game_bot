
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = "7558411038:AAEEAj0E_SwK6FINbr5aPKv28-khFJJ2gtY"  # Telegram Bot API token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Sloth Coin Game! 🦥\nUse /play to start playing.")

async def play(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Sloth is collecting coins slowly but surely! 🌙")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("play", play))
    app.run_polling()

if __name__ == "__main__":
    main()
