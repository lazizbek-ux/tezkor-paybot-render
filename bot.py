import os
from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = int(os.getenv("ADMIN_ID", "8060654578"))

# Start komandasi
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["Balans"], ["Admin bilan bog‘lanish"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Salom! Bu @Tezkor_paybot", reply_markup=reply_markup)

# Oddiy xabarlar
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()
    if "balans" in text:
        await update.message.reply_text("Balansingiz: 0 so‘m.\nTo‘ldirish uchun admin bilan bog‘laning.")
    elif "admin" in text:
        await update.message.reply_text(f"Admin: {ADMIN_ID}")
    else:
        await update.message.reply_text("Buyruqni tushunmadim. /start bosing.")

# Botni ishga tushirish
def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
