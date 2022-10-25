Для активации venv:
python -m venv venv  
source venv/Scripts/activate  

Для установки необходимых библиотек:  
pip install -r requirements.txt

Для запуска проекта:  
python manage.py runserver  
Также требуется добавить в файл .env:  
SECRET_KEY=Ключ django
DEBUG=True/False  
