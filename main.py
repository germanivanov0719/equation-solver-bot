import os
from telegram import Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, ConversationHandler, Filters


PORT = int(os.environ.get('PORT', 88))
TOKEN = "5032070179:AAFlEyrofYEhStVpCPPgOginb-zyOYBalDc"
URL = "https://api.telegram.org/bot" + TOKEN + "/getUpdates"

bot = Bot(TOKEN)
updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher

a, b, c = 1, 1, 1
COOF_A = 1
COOF_B = 2
CALCULATION = 3

class AllRealNumbers():
    pass

class ImaginaryNumbers():
    pass


def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите коэффициент a:")
    return COOF_A

def coof_a(update, context):
    global a
    a = update.message.text
    context.bot.send_message(update.effective_chat.id, "Введите коэффициент b:")
    return COOF_B

def coof_b(update, context):
    global b
    b = update.message.text
    context.bot.send_message(update.effective_chat.id, "Введите коэффициент c:")
    return CALCULATION

def calculation(update, context):
    global c
    c = update.message.text
    print(a, b, c, end=' => ')
    context.bot.send_message(update.effective_chat.id, "Решаем...")
    try:
        e = solve_quadratic_eq(float(a), float(b), float(c))
        if isinstance(e, ImaginaryNumbers):
            context.bot.send_message(update.effective_chat.id, 'x ∉ ℝ')
            print('x ∉ ℝ')
        elif isinstance(e, AllRealNumbers):
            context.bot.send_message(update.effective_chat.id, 'x ∈ ℝ')
            print('x ∈ ℝ')
        elif isinstance(e, float):
            context.bot.send_message(update.effective_chat.id, 'x = ' + str(e))
            print('x = ' + str(e))
        elif isinstance(e, list) and len(e) == 2:
            e = [str(s) for s in e]
            context.bot.send_message(update.effective_chat.id, 'x ∈ {' + ', '.join(e) + '}')
            print('x ∈ {' + ', '.join(e) + '}')
    except ValueError:
        context.bot.send_message(update.effective_chat.id, "Вы не ввели числа")
        print('Вы не ввели числа')
    except Exception as e:
        context.bot.send_message(update.effective_chat.id, "Неизвестная ошибка:" + str(e))
        print("Неизвестная ошибка:" + str(e))
    return ConversationHandler.END

def cancel(update, context):
    context.bot.send_message(update.effective_chat.id, "Что-то пошло не так. Попробуйте позже. "
                                                       "Если ошибка повторится, свяжитесь с владельцом.")

def solve_quadratic_eq(a, b, c):
    D = b ** 2 - (4 * a * c)
    if a == 0 and b == 0 and c == 0:
        return AllRealNumbers()
    elif a == 0 and b == 0:
        return []
    elif a == 0:
        return -c/b
    elif D == 0:
        square1 = (-b + D ** 0.5) / (2 * a)
        return square1
    elif D > 0:
        square1 = (-b + D ** 0.5) / (2 * a)
        square2 = (-b - D ** 0.5) / (2 * a)
        return [square1, square2]
    else:
        return ImaginaryNumbers()
    
def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет, данный бот был создан для решения квадратных уравнений любой сложности")

start_handler = CommandHandler("start", start)
coof_a_handler = MessageHandler(Filters.text, coof_a)
coof_b_handler = MessageHandler(Filters.text, coof_b)
calculation_handler = MessageHandler(Filters.text, calculation)
cancel_handler = CommandHandler("cancel", cancel)
info_handler = CommandHandler("info", info)

conversation_handler = ConversationHandler(
    entry_points=[start_handler],
    states={
        COOF_A: [coof_a_handler],
        COOF_B: [coof_b_handler],
        CALCULATION: [calculation_handler]
    },
    fallbacks=[cancel_handler]
)

dispatcher.add_handler(info_handler)
dispatcher.add_handler(conversation_handler)
updater.start_webhook(listen="0.0.0.0",
                      port=int(PORT),
                      url_path=TOKEN,
                      webhook_url = 'https://equation-solver-bot.herokuapp.com/' + TOKEN)
# updater.start_polling()
updater.idle()

