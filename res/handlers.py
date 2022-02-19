from telegram import KeyboardButton, ReplyKeyboardMarkup, ParseMode
from telegram.ext import (CommandHandler,
                          MessageHandler,
                          ConversationHandler,
                          Filters)
from res.states_numbers import *
BIQUADRARIC_MODE = False


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


def toggle_biq_mode(update, context):
    global BIQUADRARIC_MODE
    BIQUADRARIC_MODE = not BIQUADRARIC_MODE
    if BIQUADRARIC_MODE:
        context.bot.send_message(update.effective_chat.id, "Режим решения биквадратных уравнений включен.")
    else:
        context.bot.send_message(update.effective_chat.id, "Режим решения биквадратных уравнений выключен.")


def calculation(update, context):
    from res.methods import solve
    global c
    c = update.message.text
    print(a, b, c, end=' => ')
    context.bot.send_message(update.effective_chat.id, "Решаем...")
    try:
        e = solve(float(a), float(b), float(c))
        D = float(b) ** 2 - (4 * float(a) * float(c))
        context.bot.send_message(update.effective_chat.id, f'√{D} = {D ** .5}')
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
        "квадратных уравнений любой сложности за считанные секунды.\n"
        "Для решения биквадратных уравнений используйте команду /toggle_biq_mode.\n\n"
        "(Тут есть пасхалка, на английском через нижнее подчеркивание)")


def easter_egg(update, context):
    context.bot.send_message(update.effective_chat.id,
                             "https://www.karusel-tv.ru/")


def generate_commands_buttons():
    kb = [[KeyboardButton('/start')],
          [KeyboardButton('/toggle_biq_mode')],
          [KeyboardButton('/info')]]
    kb_markup = ReplyKeyboardMarkup(kb)
    return kb_markup


handlers = {
    'start_handler': CommandHandler("start", start),
    'coof_a_handler': MessageHandler(Filters.text, coef_a),
    'coof_b_handler': MessageHandler(Filters.text, coef_b),
    'calculation_handler': MessageHandler(Filters.text, calculation),
    'cancel_handler': CommandHandler("cancel", cancel),
    'info_handler': CommandHandler("info", info),
    'easter_egg_handler': CommandHandler("easter_egg", easter_egg),
    'toggle_biq_mode': CommandHandler("toggle_biq_mode", toggle_biq_mode)
}
