# Django Development Project Auto Creation.
## Are you bored to create Django dev Project?

https://github.com/mohammadfayaj/Django_Auto_Project/assets/61315077/3a89c966-1aab-480c-b24f-e3d0ff2494e5

#### This is a repository of Python scripts that can be used for creating Auto Django project. Here are some features of this repository:
### The script will add some feature that ```Django default``` doesn't provide such as:-

```
import os
------

INSTALLED_APPS = [
    ----------
    "test_app",
]


TEMPLATES = [
    ----------
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    ----------
]

STATIC_ROOT = (os.path.join(BASE_DIR, 'static'),)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_URL = "static/"

```

- The script will create `templates` and `static` folder
- & also create `forms.py`, `urls.py`


```
# example modified urls.py

from django.urls import path 
from .views import * 
  
app_name = 'test_app'
 
urlpatterns = [ 
 path('', home, name='home'), 
]


# example modified views.py

from django.http import HttpResponse 
from django.shortcuts import render 
 
# Create your views here. 
def home(request):
    return HttpResponse("<h1 style='text-align: center; margin-top: 10rem;'>Everything Good!</h1>") 

```


- #### The scripts are written in Python 3+ and use standard libraries such as `subprocess`, `os`, `shutil`, and `pathlib`.
- #### The scripts can be executed from the command line or just double click on the `execute_django_dev_create.cmd` 


This repository is open source and licensed under the MIT License. You are free to use, modify, and distribute the scripts as long as you give credit to the original author and include the license file. If you find any bugs or have any suggestions for improvement, please open an issue or a pull request on GitHub. Thank you for using these Python scripts!
