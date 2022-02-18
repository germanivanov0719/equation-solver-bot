from telegram import KeyboardButton, ReplyKeyboardMarkup, ParseMode
from telegram.ext import (CommandHandler,
                          MessageHandler,
                          ConversationHandler,
                          Filters)
from res.states_numbers import *
from res.methods import *


def start(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Введите коэффициент a:",
                             reply_markup=generate_commands_buttons())
    return COEF_A


def coef_a(update, context):
    global a
    a = update.message.text
    context.bot.send_message(update.effective_chat.id,
                             "Введите коэффициент b:")
    return COEF_B


def coef_b(update, context):
    global b
    b = update.message.text
    context.bot.send_message(update.effective_chat.id,
                             "Введите коэффициент c:")
    return CALCULATION


def calculation(update, context):
    global c
    c = update.message.text
    print(a, b, c, end=' => ')
    context.bot.send_message(update.effective_chat.id, "Решаем...")
    try:
        D = float(b) ** 2 - (4 * float(a) * float(c))
        context.bot.send_message(update.effective_chat.id, f'√{D} = {D ** .5}')
        e = solve(float(a), float(b), float(c))
        context.bot.send_message(
            update.effective_chat.id, str(e), parse_mode=ParseMode.HTML)
    except ValueError:
        context.bot.send_message(update.effective_chat.id, "Вы не ввели числа")
        print('Вы не ввели числа')
    except Exception as e:
        context.bot.send_message(
            update.effective_chat.id, "Неизвестная ошибка: " + str(e))
        print("Неизвестная ошибка: " + str(e))
    return ConversationHandler.END


def cancel(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "Что-то пошло не так. Попробуйте позже. "
                             "Если ошибка повторится, свяжитесь с владельцом.")


def info(update, context):
    context.bot.send_message(
        update.effective_chat.id,
        "Привет. Данный бот был создан для решения "
        "квадратных уравнений любой сложности за считанные секунды.")


def easter_egg(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "https://www.karusel-tv.ru/")


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
