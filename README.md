astra-django
============

Django app for pulling data from Astra Schedule API

Install by dropping this folder into your Django project.

Add the following to your settings.py file, filling in appropriately:

settings.ASTRA_USER = ''
settings.ASTRA_PASS = ''


For now, this application only grabs buildings and classrooms, because it's all I needed. When I need it to do more I will extend it.