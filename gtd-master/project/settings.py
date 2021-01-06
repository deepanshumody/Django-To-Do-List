import os

from django.contrib.messages import constants as message_constants

DEBUG = False

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


TIME_ZONE = "America/Los_Angeles"


LANGUAGE_CODE = "en-us"

SITE_ID = 2


USE_I18N = True


MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "project.urls"
LOGIN_URL = "/"
LOGIN_REDIRECT_URL = "todo:lists"
LOGOUT_REDIRECT_URL = "/"

SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SECURITY_WARN_AFTER = 5
SESSION_SECURITY_EXPIRE_AFTER = 12

WSGI_APPLICATION = "project.wsgi.application"

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.admindocs",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.flatpages",
    "django.contrib.messages",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "todo",
    "project",
    "django_extensions",
    "emailer",
    
    "allauth",   # <--
    "allauth.account",   # <--
    "allauth.socialaccount",   # <--
    "allauth.socialaccount.providers.google",  # <--
)


STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "project", "static")]
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

MEDIA_ROOT = os.path.join(BASE_DIR, "media")
MEDIA_URL = "/media/"

FILE_UPLOAD_PERMISSIONS = 0o644



SECRET_KEY = ""

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "project", "templates",)],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
                "django.contrib.messages.context_processors.messages",
                
            ]
        },
    }
]




MESSAGE_TAGS = {message_constants.ERROR: "danger"}


DATABASES = {}

AUTHENTICATION_BACKENDS = (
 'django.contrib.auth.backends.ModelBackend',
 'allauth.account.auth_backends.AuthenticationBackend',
 )

TODO_ALLOW_FILE_ATTACHMENTS = True
TODO_LIMIT_FILE_ATTACHMENTS = [".jpg", ".gif", ".png", ".csv", ".pdf"]
ALLOWED_HOSTS = ["localhost", "192.168.1.6"]


SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

        

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIT_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = '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'