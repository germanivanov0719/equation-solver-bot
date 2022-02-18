from telegram import KeyboardButton, ReplyKeyboardMarkup
from telegram.ext import CommandHandler, MessageHandler, ConversationHandler, Filters
from res.states_numbers import *
from res.methods import *

def start(update, context):
    context.bot.send_message(update.effective_chat.id, "Введите коэффициент a:", reply_markup=generate_commands_buttons())
    return COEF_A

def coef_a(update, context):
    global a
    a = update.message.text
    context.bot.send_message(update.effective_chat.id, "Введите коэффициент b:")
    return COEF_B

def coef_b(update, context):
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

def info(update, context):
    context.bot.send_message(update.effective_chat.id, "Привет, данный бот был создан для решения квадратных уравнений любой сложности")
    
def generate_commands_buttons():
    kb = [[KeyboardButton('/start')],
          [KeyboardButton('/info')]]
    kb_markup = ReplyKeyboardMarkup(kb)
    return kb_markup

handlers = {
    'start_handler': CommandHandler("start", start),
    'coof_a_handler': MessageHandler(Filters.text, coef_a),
    'coof_b_handler': MessageHandler(Filters.text, coef_b),
    'calculation_handler': MessageHandler(Filters.text, calculation),
    'cancel_handler': CommandHandler("cancel", cancel),
    'info_handler': CommandHandler("info", info)
}