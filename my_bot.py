import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7519317014:AAHnmXSWJ6OhK_us-d1lZMdifrNN7EkfU2A"

IMAGE_CERTIFICATE = "сертификат.jpg"
IMAGE_NEXT_LOCATION = "фудкорт.jpg"
IMAGE_FINAL_SPOT = "локация.jpg"
IMAGE_QR_CODE = "кино.jpg"
IMAGE_HOME = "дом.jpg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_button = [[KeyboardButton("Ура, начнём!")]]
    reply_markup = ReplyKeyboardMarkup(start_button, resize_keyboard=True)
    
    await update.message.reply_text(
        "Привет, мама! Готовься к увлекательному квесту!",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "Ура, начнём!":
        button = [[KeyboardButton("Приехала на место")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        await update.message.reply_text(
            "Адрес — Крылатая 2, этаж 2, справа от магазина Funday.",
            reply_markup=reply_markup
        )
    
    elif text == "Приехала на место":
        button = [[KeyboardButton("Готово")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        
        with open(IMAGE_CERTIFICATE, 'rb') as photo:
            await update.message.reply_photo(
                photo,
                caption="Это сертификат на книгу, выбирай скорее!",
                reply_markup=reply_markup
            )
    
    elif text == "Готово":
        button = [[KeyboardButton("На месте")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        
        with open(IMAGE_NEXT_LOCATION, 'rb') as photo:
            await update.message.reply_photo(
                photo,
                caption="Теперь сюда",
                reply_markup=reply_markup
            )
    
    elif text == "На месте":
        button = [[KeyboardButton("Сделала")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        await update.message.reply_text(
            "Подойди к MyBox и назови код 1234",
            reply_markup=reply_markup
        )
    
    elif text == "Сделала":
        button = [[KeyboardButton("Готово")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        await update.message.reply_text(
            "Подойди к КФС и назови код 4321",
            reply_markup=reply_markup
        )
    
    elif text == "Готово":
        button = [[KeyboardButton("Готово")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        await update.message.reply_text(
            "Подойди к Ташир пицце и назови код 1212",
            reply_markup=reply_markup
        )
    
    elif text == "Готово":
        button = [[KeyboardButton("На месте")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        
        with open(IMAGE_FINAL_SPOT, 'rb') as photo:
            await update.message.reply_photo(
                photo,
                caption="Молодец, теперь спрячь всё в рюкзак и направляйся вот сюда:",
                reply_markup=reply_markup
            )
    
    elif text == "На месте":
        button = [[KeyboardButton("Я всё")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        
        with open(IMAGE_QR_CODE, 'rb') as photo:
            await update.message.reply_photo(
                photo,
                caption="Покажи этот QR-код на входе. Возвращайся после просмотра!",
                reply_markup=reply_markup
            )
    
    elif text == "Я всё":
        with open(IMAGE_HOME, 'rb') as photo:
            await update.message.reply_photo(
                photo,
                caption="Твоё мучение закончено) Ждём тебя дома!",
                reply_markup=ReplyKeyboardMarkup.remove()
            )

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()