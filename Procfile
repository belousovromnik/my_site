release: python manage.py migrate
python manage.py loaddata reader.json
python manage.py loaddata p_library.json
web: python manage.py runserver 0.0.0.0:$PORT
