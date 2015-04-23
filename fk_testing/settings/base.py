DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

INSTALLED_APPS = (
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "reversion",
    "cms.apps.pages",
    "cms.apps.media",
    "cms.apps.news",
    "fk_testing.apps.people",
)

SECRET_KEY = " "
