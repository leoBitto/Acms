=====
Acms
=====

Acms is a Django app to organize content in a website
A content management system created with Bootstrap 5.0 
and Django 4.0 . Its scope is to allow people with no 
knowledge to create simple websites that contain images and text
Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "Acms" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'Acms',
    ]

2. Include the Acms URLconf in your project urls.py like this::

    path('', include(('Acms.urls', 'Acms'), namespace="Acms")),

3. Run ``python manage.py migrate`` to create the Acms models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create the models (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000 to see the website