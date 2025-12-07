## Django CRUD

This is a simple Django project demonstrating basic CRUD (Create, Read, Update, Delete) operations. The project is structured to help you understand how to implement a CRUD application using Django's models, views, and templates.

#### Requirements
- Python  
- Django
- Other dependencies listed in requirements.txt

#### Setup Instructions
##### 1. Clone the repository:
```bash
git clone https://github.com/gmlincoln/django-crud.git
cd django-crud
```

##### 2. Set up the virtual environment:
```bash
python -m venv .venv
```

##### 3. Activate the virtual environment:

**On Windows:**
```bash

.venv\Scripts\activate

```
**On macOS/Linux:**
```bash
source .venv/bin/activate

```

##### 4. Install the required dependencies:
<!-- pip install -r requirements.txt -->
```bash
pip install django
```

##### 5. Set up the database:
```bash
python manage.py migrate

```

##### 6. Create a superuser (if needed):
```bash
python manage.py createsuperuser
```


###### When prompted, use the following credentials for the admin:

```bash
Username: admin

Password: P@ssw0rd
```

##### 7. Run the development server:
python manage.py runserver


Visit http://127.0.0.1:8000/ in your browser to view the app.

###### Core App

The core application in this project is named core, and it contains the necessary views, models, and templates for managing CRUD operations.