import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Benvenuto su TrovaPrivati!\n"
        "Questo bot ti aiuta a trovare annunci immobiliari pubblicati solo da privati.\n\n"
        "Con 1€ ricevi tutti gli annunci per 1 città per 30 giorni.\n"
        "Con 5€ ricevi annunci da tutte le città che desideri, per 30 giorni.\n\n"
        "Puoi anche invitare un amico e ricevere 2 mesi gratis!"
    )

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
