<h1 style="font-size: 30px; text-align: center; margin: 15px; padding: 10px;">MLwelding_seams</h1> 

# Main information
Dart Welders is a project providing a model capable of detecting and classifying weld defects.

Dart Welders - это проект предоставляющий модель, способную обнаруживать и классифицировать дефекты сварных швов.


Link to Jupyter Notebook: 

Link to Google Drive: https://drive.google.com/drive/folders/1NBqG0HD_YaXrMRcQ2iYGqrgA5HT9ZkQE?usp=drive_link
# Deploy  ![Python 3.8](https://img.shields.io/badge/python-3.8-blue.svg)

1. Clone git repository
```
git clone https://github.com/FoxjLis/MLwelding_seams.git
```

2. Load the model weights

3. Run API
```
docker-compose up website -d --build
```

4. Create config.py file with:
- ```TOKEN=<token key>```
- ```CONFIDENCE_THRESHOLD=<key>```

5. Run telegram bot
```
docker-compose up telegram-bot -d --build
```
