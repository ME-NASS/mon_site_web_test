from telegram import Update, WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = '7759770883:AAFL8Vgl-vJXwRma48RVd25hpuGaFRdgFqc'
WEBAPP_URL = 'https://petitcasino.casino.fr/fr'  # Ton lien de WebApp

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [KeyboardButton(text="🎰 Lancer le Casino", web_app=WebAppInfo(url=WEBAPP_URL))]
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("Bienvenue au Casino ! Clique ci-dessous pour commencer :", reply_markup=reply_markup)

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
