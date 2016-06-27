# django_student
This is a test task for django models showing integration with AngularJS.

# INSTALL
 
```
git clone git@github.com:rjuppa/django_student.git
cd django_student
```

use virtual environment if you want
```
python3  -m venv myenv
. myenv/bin/activate
```

Install python deps.
```
pip install -r requirements.txt
```

Install javascript deps.
```
cd static/app
npm install
```

Go back up to project folder and run django server
```
cd ..
cd ..
python manage.py runserver
```

Open page http://127.0.0.1:8000/ in web browser
