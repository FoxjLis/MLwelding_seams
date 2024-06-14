from flask import Flask, request, jsonify, send_from_directory
from ultralytics import YOLO 
import cv2 
from flask_cors import CORS 
import os 
import uuid 

app = Flask(__name__)
CORS(app)
model = YOLO('best_m.pt')

@app.route('/whatsdamage', methods=['POST'])
def whats_damage():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'})

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'})

    file_path = os.path.join('uploads', file.filename)
    file.save(file_path)

    results = model(file_path) 

    img = cv2.imread(file_path)
    for result in results:
        x1, y1, x2, y2, class_name = result
        cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv2.putText(img, class_name, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)

    result_file_path = os.path.join('results', f'{str(uuid.uuid4())}.jpg')
    cv2.imwrite(result_file_path, img)

    return jsonify({'result_file_path': result_file_path})

@app.route('/get_image/<image_name>', methods=['GET'])
def get_image(image_name):
    return send_from_directory('results', image_name)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)