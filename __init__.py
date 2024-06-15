from flask import Flask, request, jsonify, send_from_directory
from ultralytics import YOLO
import cv2
from flask_cors import CORS
import os
import uuid

app = Flask(__name__)
CORS(app)
model = YOLO('best.pt')

@app.route('/whatsdamage', methods=['POST'])
def whats_damage():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    image = cv2.imread(file_path)
    results = model(file_path)

    img = cv2.imread(file_path)
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
            confidence = float(box.conf)  # Преобразование Tensor к float
            label = model.names[class_id]

            # Рисование ректов на изображении
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(image, f'{label} {confidence:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12),
                        2)
    unical_name = f'{str(uuid.uuid4())}.jpg' 
    result_file_path = os.path.join('results', unical_name)
    cv2.imwrite(result_file_path, image)
    result_file_path = unical_name
    return jsonify({'result_file_path': (result_file_path, results[0][0].tojson())})

@app.route('/get_image/<image_name>', methods=['GET'])
def get_image(image_name):
    return send_from_directory('results', image_name)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)

