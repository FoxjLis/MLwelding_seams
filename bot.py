import torch
from ultralytics import YOLO
import os

def train_model():
    model = YOLO('C:/Users/Karma/PycharmProjects/svarka/runs/detect/train3/weights/best.pt')

    data_path = 'C:/Users/Karma/Desktop/test/Dataset/Svarka/data.yaml'

    epochs = 50
    batch_size = 16
    img_size = 640

    # Проверка доступности GPU
    device = 'cuda' if torch.cuda.is_available() else 'cpu'
    print(f'Используется устройство: {device}')

    results = model.train(data=data_path, epochs=epochs, batch=batch_size, imgsz=img_size, device=device)

    model.save('C:/Users/Karma/Desktop/test/Dataset/Svarka/yolov8_trained_model.pt')

    print('Начинается проверка точности на тренировочном наборе данных...')
    metrics = model.val(data=data_path, split='test', device=device)

    print('Обучение завершено. Метрики:')
    print(metrics)

if __name__ == '__main__':
    train_model()
