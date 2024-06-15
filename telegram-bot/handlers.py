from telegram import Update
from telegram.ext import ContextTypes
import cv2
from ultralytics import YOLO
from utils import download_photo, process_image
from config import CONFIDENCE_THRESHOLD

# Инициализация модели
model = YOLO('best_x.pt')

defect_descriptions = {
    'adj': 'Брызги, прожоги от дуги',
    'int': 'Кратер, шлак, свищ, пора, прожог, включения',
    'geo': 'Подрез, непровар, наплыв, чешуйчатость, западание, неравномерность',
    'pro': 'Заусенец, торец, задир, забоина',
    'non': 'Незаполнение раковины, несплавление'
}

# Цвета для каждого класса
class_colors = {
    'adj': (255, 0, 0),
    'int': (0, 255, 0),
    'geo': (0, 0, 255),
    'pro': (255, 255, 0),
    'non': (255, 0, 255)
}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привет! Отправь мне фотографию сварного шва, и я классифицирую её.')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Отправь мне фотографию сварного шва, и я скажу тебе, есть ли на ней дефекты.')

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    photo_path = await download_photo(update)

    # Загрузка и предобработка изображения
    image = cv2.imread(photo_path)
    results = model(image)

    # Обработка результатов и рисование ректов
    response, output_image = process_image(results, image, model, defect_descriptions, class_colors, CONFIDENCE_THRESHOLD)

    # Сохранение изображения с ректами
    output_path = 'output.jpg'
    cv2.imwrite(output_path, output_image)

    # Отправка результата пользователю
    await update.message.reply_text(response)
    await context.bot.send_photo(chat_id=update.message.chat_id, photo=open(output_path, 'rb'))
