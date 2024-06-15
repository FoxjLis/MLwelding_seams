from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from handlers import start, help_command, handle_photo
from config import TOKEN


def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.PHOTO & ~filters.COMMAND, handle_photo))

    application.run_polling()


if __name__ == '__main__':
    main()
