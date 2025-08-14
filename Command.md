<!-- For install from the requirements.txt file -->
pip install -r  requirements.txt

<!-- Initiate  the djano projects  -->
django-admin startproject core . 


<!-- run the django server  -->
python manage.py runserver

<!-- migrate for inintal  db creation -->

python manange.py  migrate
 
<!-- For creating super user for admin panel  -->
python manage.py createsuperuser