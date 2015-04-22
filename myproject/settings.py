"""
Django settings for myproject project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ho4o$k(2=0uwtc^i0n)fq%bl6(=w%5c_*eoqa=$uw9_rx@(kh#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'haystack',
    'ckeditor'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'myproject.urls'

WSGI_APPLICATION = 'myproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'blog',
	'USER':'tmyyss',
	'PASSWORD':'password',
	'HOST':'localhost',
	'PORT':'3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh-cn'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT=os.path.join(BASE_DIR,'static')

LOGIN_REDIRECT_URL='/'

CACHES={
	'default':{
		'BACKEND':'django.core.cache.backends.memcached.MemcachedCache',
		'LOCATION':'127.0.0.1:11211',
		'TIMEOUT':60,
	}
}

MIDDLEWARE_CLASSED = (
	'django.middleware.cache.UpdateCacheMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.cache.FetchFromCacheMiddleware',
)

HAYSTACK_CONNECTIONS = {
	'default':{
		'ENGINE':'blog.whoosh_cn_backend.WhooshEngine',
		'PATH':os.path.join(BASE_DIR,'whoosh_index'),
		},
}

HAYSTACK_SIGAL_PROCESSOR='haystack.signals.RealtimeSignalProcessor'

MEDIA_URL="/meida/"
MEDIA_ROOT=os.path.join(BASE_DIR,"meida")
CKEDITOR_UPLOAD_PATH='ck_images'


CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': (
			['div','Source','-','Save','NewPage','Preview','-','Templates'], 
			['Cut','Copy','Paste','PasteText','PasteFromWord','-','Print','SpellChecker','Scayt'], 
			['Undo','Redo','-','Find','Replace','-','SelectAll','RemoveFormat'], 
			['Form','Checkbox','Radio','TextField','Textarea','Select','Button', 'ImageButton','HiddenField'], 
			['Bold','Italic','Underline','Strike','-','Subscript','Superscript'], 
			['NumberedList','BulletedList','-','Outdent','Indent','Blockquote'], 
			['JustifyLeft','JustifyCenter','JustifyRight','JustifyBlock'], 
			['Link','Unlink','Anchor'], 
			['Image','Flash','Table','HorizontalRule','Smiley','SpecialChar','PageBreak'], 
			['Styles','Format','Font','FontSize'], 
			['TextColor','BGColor'], 
			['Maximize','ShowBlocks','-','About', 'pbckcode'],
		),
	}
}
