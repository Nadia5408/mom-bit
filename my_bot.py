import os
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7519317014:AAHnmXSWJ6OhK_us-d1lZMdifrNN7EkfU2A"

IMAGE_CERTIFICATE = "����������.jpg"
IMAGE_NEXT_LOCATION = "�������.jpg"
IMAGE_FINAL_SPOT = "�������.jpg"
IMAGE_QR_CODE = "����.jpg"
IMAGE_HOME = "���.jpg"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    start_button = [[KeyboardButton("���, �����!")]]
    reply_markup = ReplyKeyboardMarkup(start_button, resize_keyboard=True)
    
    await update.message.reply_text(
        "������, ����! �������� � �������������� ������!",
        reply_markup=reply_markup
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    
    if text == "���, �����!":
        button = [[KeyboardButton("�������� �� �����")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        await update.message.reply_text(
            "����� � �������� 2, ���� 2, ������ �� �������� Funday.",
            reply_markup=reply_markup
        )
    
    elif text == "�������� �� �����":
        button = [[KeyboardButton("������")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        
        with open(IMAGE_CERTIFICATE, 'rb') as photo:
            await update.message.reply_photo(
                photo,
                caption="��� ���������� �� �����, ������� ������!",
                reply_markup=reply_markup
            )
    
    elif text == "������":
        button = [[KeyboardButton("�� �����")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        
        with open(IMAGE_NEXT_LOCATION, 'rb') as photo:
            await update.message.reply_photo(
                photo,
                caption="������ ����",
                reply_markup=reply_markup
            )
    
    elif text == "�� �����":
        button = [[KeyboardButton("�������")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        await update.message.reply_text(
            "������� � MyBox � ������ ��� 1234",
            reply_markup=reply_markup
        )
    
    elif text == "�������":
        button = [[KeyboardButton("������")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        await update.message.reply_text(
            "������� � ��� � ������ ��� 4321",
            reply_markup=reply_markup
        )
    
    elif text == "������":
        button = [[KeyboardButton("������")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        await update.message.reply_text(
            "������� � ����� ����� � ������ ��� 1212",
            reply_markup=reply_markup
        )
    
    elif text == "������":
        button = [[KeyboardButton("�� �����")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        
        with open(IMAGE_FINAL_SPOT, 'rb') as photo:
            await update.message.reply_photo(
                photo,
                caption="�������, ������ ������ �� � ������ � ����������� ��� ����:",
                reply_markup=reply_markup
            )
    
    elif text == "�� �����":
        button = [[KeyboardButton("� ��")]]
        reply_markup = ReplyKeyboardMarkup(button, resize_keyboard=True)
        
        with open(IMAGE_QR_CODE, 'rb') as photo:
            await update.message.reply_photo(
                photo,
                caption="������ ���� QR-��� �� �����. ����������� ����� ���������!",
                reply_markup=reply_markup
            )
    
    elif text == "� ��":
        with open(IMAGE_HOME, 'rb') as photo:
            await update.message.reply_photo(
                photo,
                caption="��� ������� ���������) ��� ���� ����!",
                reply_markup=ReplyKeyboardMarkup.remove()
            )

def main():
    app = Application.builder().token(TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("��� �������...")
    app.run_polling()

if __name__ == "__main__":
    main()