from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
import emoji
#start#
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print("someone started")
    await update.message.reply_text("سلام به ربات Atlantis Vpn خوش اومدی! :red_heart:")

app = Application.builder().token("8334306969:AAFJRgjgiRIp5TKdy72mcGcCcidnQMaDCA0").build()

app.add_handler(CommandHandler("start", start))

app.run_polling
