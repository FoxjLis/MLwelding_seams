pip install albumentations opencv-python


import os
import cv2
import numpy as np
import albumentations as A
from tqdm import tqdm

def load_images_and_annotations(image_dir, annotation_dir):
    images = []
    annotations = []
    for filename in os.listdir(image_dir):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            image_path = os.path.join(image_dir, filename)
            annotation_path = os.path.join(annotation_dir, os.path.splitext(filename)[0] + '.txt')
            if os.path.exists(annotation_path):
                images.append(cv2.imread(image_path))
                with open(annotation_path, 'r') as f:
                    annotations.append(f.read())
    return images, annotations

def save_augmented_images_and_annotations(images, annotations, output_image_dir, output_annotation_dir, prefix):
    if not os.path.exists(output_image_dir):
        os.makedirs(output_image_dir)
    if not os.path.exists(output_annotation_dir):
        os.makedirs(output_annotation_dir)

    for idx, (image, annotation) in enumerate(zip(images, annotations)):
        output_image_path = os.path.join(output_image_dir, f"{prefix}_{idx}.jpg")
        output_annotation_path = os.path.join(output_annotation_dir, f"{prefix}_{idx}.txt")
        cv2.imwrite(output_image_path, image)
        with open(output_annotation_path, 'w') as f:
            f.write(annotation)

def augment_dataset(images, annotations, augmenter, num_augmentations):
    augmented_images = []
    augmented_annotations = []
    for _ in range(num_augmentations):
        for image, annotation in zip(images, annotations):
            augmented = augmenter(image=image)
            augmented_images.append(augmented['image'])
            augmented_annotations.append(annotation)
    return augmented_images, augmented_annotations

# Путь к исходникам
image_dir = 'path/to/images'
annotation_dir = 'path/to/annotations'

# Путь для сохранения
output_image_dir = 'path/to/output/images'
output_annotation_dir = 'path/to/output/annotations'

# Загрузка изображений и аннотаций
images, annotations = load_images_and_annotations(image_dir, annotation_dir)

# Определение аугментатора
augmenter = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.VerticalFlip(p=0.5),
    A.RandomRotate90(p=0.5),
    A.Transpose(p=0.5),
    A.ShiftScaleRotate(shift_limit=0.0625, scale_limit=0.2, rotate_limit=45, p=0.5),
    A.Blur(blur_limit=3, p=0.5),
    A.OpticalDistortion(p=0.5),
    A.GridDistortion(p=0.5),
    A.HueSaturationValue(p=0.5)
])

# Расширение датасета
num_augmentations = 5  # Количество аугментаций на каждое изображение
augmented_images, augmented_annotations = augment_dataset(images, annotations, augmenter, num_augmentations)

# Сохранение расширенного датасета
save_augmented_images_and_annotations(augmented_images, augmented_annotations, output_image_dir, output_annotation_dir, 'augmented')
