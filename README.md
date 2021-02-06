# DRC System Test
---

* Clone project

* Copy environment file and fill required field.

    `$ cp .env.template .env`
  
* Now install all required packages.

    `$ pip install -r requirements.txt`
  
* Now create a database in your MySQL DBMS.

* Migrate models in the database.

    `$ python manage.py migrate`
  
* Run server

    `$ python manage.py runserver`