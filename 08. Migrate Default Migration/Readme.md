# How to Migrate Default Migration

- By default there are schema which are predefined.
- Whenever we create model
- Django by default uses sqlite database.
- when we run server by default sqlite database is created.
- It also gives admin pannel.
- To create super user we have to migrate first.
- `pyhton manage.py makemigrations` - when we create new tables
- `python manage.py migrate` - Default table is created inside `sqlite` DB.