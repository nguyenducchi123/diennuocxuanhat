from pathlib import Path
import os
from dotenv import load_dotenv
import dj_database_url

# Đọc biến môi trường từ .env
load_dotenv()

# Đường dẫn gốc của dự án
BASE_DIR = Path(__file__).resolve().parent.parent

# Key bí mật cho Django
SECRET_KEY = os.getenv('SECRET_KEY', 'your_default_secret_key')

# Chế độ debug: False khi deploy
DEBUG = os.getenv("DEBUG", "True") == "True"

# Danh sách host được phép truy cập
ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS', '127.0.0.1,localhost').split(',')

# Cài đặt ứng dụng
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
]

# Middleware
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',  # Thêm cho static files
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'site1.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "home/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'site1.wsgi.application'

# Cơ sở dữ liệu mặc định (SQLite)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Ghi đè cấu hình nếu có DATABASE_URL (Render cung cấp PostgreSQL)
db_from_env = dj_database_url.config()
if db_from_env:
    DATABASES['default'] = db_from_env

# Password validator
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Ngôn ngữ và múi giờ
LANGUAGE_CODE = 'vi'
TIME_ZONE = 'Asia/Ho_Chi_Minh'
USE_I18N = True
USE_TZ = True

# File static (CSS, JS...)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'home/static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Dùng WhiteNoise để quản lý static files khi deploy
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# File media (hình ảnh upload)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Cấu hình primary key mặc định
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Ghi log ra file và console
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'debug.log'),
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
    },
}
