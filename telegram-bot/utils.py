from telegram import Update
import cv2

async def download_photo(update: Update) -> str:
    photo = update.message.photo[-1]
    photo_file = await photo.get_file()
    photo_path = 'photo.jpg'
    await photo_file.download_to_drive(photo_path)
    return photo_path

def process_image(results, image, model, defect_descriptions, confidence_threshold):
    response = "Классификация завершена. Результаты:\n"
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            confidence = float(box.conf)  # Преобразование Tensor к float
            label = model.names[class_id]
            defect_description = defect_descriptions.get(class_id, label)
            response += f'{defect_description}: {confidence:.2f}\n'

            # Рисование ректов на изображении
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, f'{label} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)

    return response, image
