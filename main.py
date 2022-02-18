import os
from telegram import Bot
from telegram.ext import Updater, ConversationHandler
from res.number_classes import *
from res.handlers import handlers
from res.states_numbers import *
# Importing tokens
from tokens import token, token_debug

a, b, c = 1, 1, 1

DEBUG = 0
PORT = int(os.environ.get('PORT', 88))
if DEBUG:
    TOKEN = token_debug
else:
    TOKEN = token
WEBHOOK_URL = 'https://equation-solver-bot.herokuapp.com/' + TOKEN
URL = "https://api.telegram.org/bot" + TOKEN + "/getUpdates"

bot = Bot(TOKEN)
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

conversation_handler = ConversationHandler(
    entry_points=[handlers['start_handler']],
    states={COEF_A: [handlers['coof_a_handler']],
            COEF_B: [handlers['coof_b_handler']],
            CALCULATION: [handlers['calculation_handler']]},
    fallbacks=[handlers['cancel_handler']],
    allow_reentry=True
)

dispatcher.add_handler(handlers['info_handler'])
dispatcher.add_handler(conversation_handler)

if DEBUG:
    updater.start_polling()
else:
    updater.start_webhook(listen="0.0.0.0", port=int(PORT), url_path=TOKEN, webhook_url=WEBHOOK_URL)

updater.idle()

