from pathlib import Path
import subprocess
import shutil
import os

virtual_env = input("Please Inter Your Virtual Env Name: ")
project_name = input("Please Inter Your Django Project Name: ")
app_name = input("Please Inter Your Django App Name: ")

# virtual_env = 'env'
# project_name = 'project'
# app_name = 'celery'

if os.path.exists(f'{project_name}'):
    print('Found Existing Project, Removing... Folder')
    shutil.rmtree(project_name)
else:
    pass

if os.path.exists(f'{virtual_env}'):
    print('=====> Found Existing Virtual Environment <=====')
    subprocess.call(f"call {virtual_env}/scripts/activate.bat \
                    && pip install django==4.2 \
                    && django-admin startproject {project_name} \
                    && cd {project_name} \
                    && django-admin startapp {app_name}", shell=True)
else:
    print('=====> Please Wait, While Creating Virtual Environment <=====')
    subprocess.call(f"virtualenv {virtual_env} \
                && call {virtual_env}/scripts/activate.bat \
                && pip install django \
                && django-admin startproject {project_name} \
                && cd {project_name} \
                && django-admin startapp {app_name}", shell=True)

cwd = os.getcwd()
file_path = f"{cwd}\{project_name}\{project_name}"
settings_name = 'settings.py'
urls_name = 'urls.py'
urls = os.path.join(file_path, urls_name)
settings = os.path.join(file_path, settings_name)

with open(f'{settings}', 'r+') as f:
    lines = f.readlines()
    lines.insert(11, 'import os\n')
    lines.insert(40, f'    "{app_name}",\n')
    lines[58] = "        'DIRS': [os.path.join(BASE_DIR, 'templates')],\n" 
    lines.insert(119, "STATIC_ROOT = (os.path.join(BASE_DIR, 'static'),)\n")
    lines.insert(120, "MEDIA_URL = '/media/'\n")
    lines.insert(121, "MEDIA_ROOT = os.path.join(BASE_DIR, 'media')\n")

    f.seek(0)
    f.writelines(lines)
    f.truncate()
    print('settings.py file has been write successfully')

print("Opening urls.py - > ")
with open(f'{urls}', 'r+') as f:
    lines = f.readlines()
    lines[17] = 'from django.urls import path, include\n'
    lines.insert(18, "from django.conf import settings\n")
    lines.insert(19, "from django.conf.urls.static import static\n")
    lines.insert(23, f"    path('', include('{app_name}.urls', namespace = '{app_name}'))\n")
    lines[24] = "] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)"
    f.seek(0)
    f.writelines(lines)
    f.truncate()

    print("Write Finished for urls.py - >")

root_path = f"{cwd}\{project_name}"
app_path = f"{cwd}\{project_name}\{app_name}"
create_urls = os.path.join(app_path, 'urls.py')

templates_dir = "templates"
static_dir = 'static'

templates_abs_dir = os.path.join(root_path, templates_dir)
static_abs_dir = os.path.join(root_path, static_dir )

os.makedirs(templates_abs_dir, exist_ok=True)
os.makedirs(static_abs_dir, exist_ok=True)


forms = Path(app_path, 'forms.py')
forms.touch(exist_ok=True)  # will create file, if it exists will do nothing

views_path =  f"{app_path}\\views.py"

with open(f'{views_path}', 'w') as f:
    f.write("from django.http import HttpResponse \n"
            "from django.shortcuts import render \n"
            " \n"
            "# Create your views here. \n"
            "def home(request):\n"
            "    return HttpResponse(\"<h1 style='text-align: center; margin-top: 10rem;'>Everything Good!</h1>\") \n")
                

with open(f'{create_urls}', 'w') as f:
    f.write("from django.urls import path \n"
            "from .views import * \n"
            "  \n"
            f"app_name = '{app_name}'\n"
            " \n"
            "urlpatterns = [ \n"
            " path('', home, name='home'), \n"
            "]")
    
print('=====> Progress Finished 100% <=====')
print('=====> Please Wait, Running Django Server <=====')
subprocess.call(f"cd {project_name} && python manage.py makemigrations && python manage.py migrate && python manage.py runserver", shell=True)
