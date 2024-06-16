# Folder Structure

- By default django uses `sqlite` database.
- `manage.py` - main file , used to run project, migration
- `Templates` - Created a `templates folder` to create html files and stored in it.
- `Static` - Created `Static Folder` to store static data. 
- `media` To store media related files (Image , Videos, e.t.c)

- Outer `settings.py` - Used to run the project.

- Inner `settings.py` - It manages all settings of application.
    - `BASE_DIR` - Current directory 
    - `SECRET_KEY` - During creation of project it creates a secret key.
    - `DEBUG` - Show Erros in project
    - `ALLOWED_HOSTS` - Stores the hosts
    - `INSTALLED_APPS` - Default table 
    - `Middlewares` - Restriction, security , session
    - `ROOT_URLCONF` - main urls 
    - `TEMPLATES` 
        - `DIRS` - Store the templates folder.
    - `DATABASES` - Info of database
    - `AUTH_PASSWORD_VALIDATIONS` - Validate the password
    - `STATIC_URL` - Keeps the static folder location.
    
- `urls.py` - Manages all urls of file.