@echo off
cd "E:\python wed\site1"
.\env10\Scripts\activate.bat
pip install -r requirements.txt
python manage.py runserver 127.0.0.1
pause