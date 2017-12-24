# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'bosdb',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': '',
        'PORT': 5432,
    }
}
