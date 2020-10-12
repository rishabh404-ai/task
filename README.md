# task

PROJECT FOLDER : project
App : app
Database Used : db.sqlite3

1. Landing Page Endpoint :


http://127.0.0.1:8000/api/v1/


![](working-screenshots/1.png)


2. User Registeration Endpoint :


http://127.0.0.1:8000/api/v1/register/


![](working-screenshots/2.png)


3. Time Record Endpoint :


http://127.0.0.1:8000/api/v1/entry/


![](working-screenshots/3.png)


How to get the app running locally ?

For Linux : RUN > pip3 install -r requirements.txt & python3 manage.py runserver

For Windows : RUN > pip install -r requirements.txt & python manage.py runserver

How to check entries in database ?

Run > python3 manage.py createsuperuser

Please create a dummy superuser and check the details in the admin panel by going on the link :

 http://127.0.0.1:8000/admin/
