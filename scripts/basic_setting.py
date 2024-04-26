import os
import argparse

# ARGUMENT PARSING
try:
    ap = argparse.ArgumentParser()
    ap.add_argument("-prj", "--prj", type=str, required='True', 
					help="Define the name of the project")
    ap.add_argument("-db", "--db", type=str, required='True', 
					help="Define the type of database")
    args = vars(ap.parse_args())
    prj = args.get("prj")
    db = args.get("db")
except Exception as err:
    exc_type, exc_value, exc_traceback = sys.exc_info()
    print('\033[38;5;208mError during ARGUMENT PASSING:\nError Type: '+str(exc_type)+'\nLine number: '+str(exc_traceback.tb_lineno)+'\033[0;0m')
    print(err)
    sys.exit()

# MODIFY setting.py
setting_file = str(prj)+'/settings.py'
f = open(setting_file, 'w+')
mystr = 'import os\n'
mystr += 'from pathlib import Path\n\n'
mystr += "# Build paths inside the project like this: BASE_DIR / 'subdir'.\n"
mystr += 'BASE_DIR = Path(__file__).resolve().parent.parent\n\n'
mystr += '# Quick-start development settings - unsuitable for production\n'
mystr += '# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/\n\n'
mystr += '# SECURITY WARNING: keep the secret key used in production secret!\n'
mystr += "SECRET_KEY = 'django-insecure-)8$aqu&22)=zx&zbbaf-@5aqm7p-+iv6y5_y^r48dim_jz=g90'\n"
mystr += '\n'
mystr += "# SECURITY WARNING: don't run with debug turned on in production!\n"
mystr += 'DEBUG = True\n\n'
mystr += 'ALLOWED_HOSTS = []\n\n'
mystr += '# Application definition\n\n'
mystr += 'INSTALLED_APPS = [\n'
mystr += "    'django.contrib.admin',\n"
mystr += "    'django.contrib.auth',\n"
mystr += "    'django.contrib.contenttypes',\n"
mystr += "    'django.contrib.sessions',\n"
mystr += "    'django.contrib.messages',\n"
mystr += "    'django.contrib.staticfiles',\n"
mystr += "    '"+str(prj)+"'\n"
mystr += ']\n\n'
mystr += 'MIDDLEWARE = [\n'
mystr += "    'django.middleware.security.SecurityMiddleware',\n"
mystr += "    'django.contrib.sessions.middleware.SessionMiddleware',\n"
mystr += "    'django.middleware.common.CommonMiddleware',\n"
mystr += "    'django.middleware.csrf.CsrfViewMiddleware',\n"
mystr += "    'django.contrib.auth.middleware.AuthenticationMiddleware',\n"
mystr += "    'django.contrib.messages.middleware.MessageMiddleware',\n"
mystr += "    'django.middleware.clickjacking.XFrameOptionsMiddleware',\n"
mystr += ']\n\n'
mystr += "ROOT_URLCONF = 'crm.urls'\n\n"
mystr += 'TEMPLATES = [\n'
mystr += '    {\n'
mystr += "        'BACKEND': 'django.template.backends.django.DjangoTemplates',\n"
mystr += "        'DIRS': [os.path.join(BASE_DIR, '"+str(prj)+"_website', 'templates', '"+str(prj)+"')],\n"
mystr += "        'APP_DIRS': True,\n"
mystr += "        'OPTIONS': {\n"
mystr += "            'context_processors': [\n"
mystr += "                'django.template.context_processors.debug',\n"
mystr += "                'django.template.context_processors.request',\n"
mystr += "                'django.contrib.auth.context_processors.auth',\n"
mystr += "                'django.contrib.messages.context_processors.messages',\n"
mystr += '            ],\n'
mystr += '        },\n'
mystr += '    },\n'
mystr += ']\n\n'
mystr += "WSGI_APPLICATION = 'crm.wsgi.application'\n\n"
mystr += '# Database\n'
mystr += '# https://docs.djangoproject.com/en/5.0/ref/settings/#databases\n\n'
if db == 'mysql':
	mystr += 'DATABASES = {\n'
	mystr += "    'default': {\n"
	mystr += "        'ENGINE': 'django.db.backends.mysql',\n"
	mystr += "        'NAME': '"+str(prj)+"_db',\n"
	mystr += "        'USER': 'root',\n"
	mystr += "        'PASSWORD': 'password123',\n"
	mystr += "        'HOST': 'localhost',\n"
	mystr += "        'PORT': '3306'\n"
	mystr += '    }\n'
	mystr += '}\n\n'
elif db == 'sqlite3':
	raise Exception('\033[93m\nNeed to prepare DB sqlite3\033[0m\n')
else:
	raise Exception('\033[93m\nSelect a proper db between:\n\t-mysql\n\t-sqlite3\n\033[0m')
mystr += '# Password validation\n'
mystr += '# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators\n'
mystr += '\n'
mystr += 'AUTH_PASSWORD_VALIDATORS = [\n'
mystr += '    {\n'
mystr += "        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',\n"
mystr += '    },\n'
mystr += '    {\n'
mystr += "        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',\n"
mystr += '    },\n'
mystr += '    {\n'
mystr += "        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',\n"
mystr += '    },\n'
mystr += '    {\n'
mystr += "        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',\n"
mystr += '    },\n'
mystr += ']\n\n'
mystr += '# Internationalization\n'
mystr += '# https://docs.djangoproject.com/en/5.0/topics/i18n/\n\n'
mystr += "LANGUAGE_CODE = 'en-us'\n\n"
mystr += "TIME_ZONE = 'UTC'\n\n"
mystr += 'USE_I18N = True\n\n'
mystr += 'USE_TZ = True\n\n'
mystr += '# Static files (CSS, JavaScript, Images)\n'
mystr += '# https://docs.djangoproject.com/en/5.0/howto/static-files/\n\n'
mystr += "STATIC_URL = 'static/'\n\n"
mystr += '# Default primary key field type\n'
mystr += '# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field\n\n'
mystr += "DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'\n"
f.write(mystr)
