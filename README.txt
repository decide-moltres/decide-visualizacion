Una vez clonado, es recomendable hacer "sudo python3 manage.py migrate".
Para poder desplegar en local, solo hay que irse a decide/localsettings.py y cambiar lo siguiente:

BASEURL = 'http://localhost:8000'
APIS = {
    'authentication': BASEURL,
    'base': BASEURL,
    'booth': BASEURL,
    'census': BASEURL,
    'mixnet': BASEURL,
    'postproc': BASEURL,
    'store': BASEURL,
    'visualizer': BASEURL,
    'voting': BASEURL,
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres',
        'USER': 'decide',
	'PASSWORD': 'decide',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
