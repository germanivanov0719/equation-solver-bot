from telegram import Bot
from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, ConversationHandler, Filters)


TOKEN = "5032070179:AAFlEyrofYEhStVpCPPgOginb-zyOYBalDc"
URL = "https://api.telegram.org/" + TOKEN + "/getUpdates"

bot = Bot(TOKEN)
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Бот временно не работает.")
    context.bot.send_message(update.effective_chat.id,
                             "Причина: переход на систему WebHook'ов.")
    return COOF_A


def cancel(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        "Что-то пошло не так. Попробуйте позже. "
        "Если ошибка повторится, свяжитесь с владельцом.")


start_handler = CommandHandler("start", start)
cancel_handler = CommandHandler("cancel", cancel)

conversation_handler = ConversationHandler(
    entry_points=[start_handler],
    states={},
    fallbacks=[cancel_handler]
)

dispatcher.add_handler(conversation_handler)
updater.start_polling()
updater.idle()
