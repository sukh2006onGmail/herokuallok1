SECRET_KEY = 'ff^#-e94e=57_pd1!z2+y8lvhcrs=3*79nbcmgn-tonm-1^7=m'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']

ROOT_URLCONF = 'djangoman.urls'


INSTALLED_APPS = [
    'djangoman',
    'django.contrib.staticfiles',
]
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'APP_DIRS': True,
        # 'OPTIONS': {
        #     'context_processors': [
        #     ],
        # },
    },
]

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


STATIC_URL = "/static/"














