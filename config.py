import os

DEBUG = True

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'zlbbs'
USERNAME = 'root'
PASSWORD = '123456'

DB_URL = "mysql+pymysql://{username}:{password}@{host}:{port}/{db}?charset=utf8".format(
    username=USERNAME,
    password=PASSWORD,
    host=HOSTNAME,
    port=PORT,
    db=DATABASE)

SQLALCHEMY_DATABASE_URI = DB_URL

SQLALCHEMY_TRACK_MODIFICATIONS = False

# SECRET_KEY = os.urandom(24)
SECRET_KEY = "dsdjsdhjhds121"

CMS_USER_ID = 'user_id'
FRONT_USER_ID = 'ddsds'

# flask分页配置
PER_PAGE = 10

MAIL_SERVER = "smtp.qq.com"
MAIL_PORT = '587'
MAIL_USE_TLS = True
# MAIL_USE_SSL = True
# MAIL_PORT = '465'
MAIL_USERNAME = "1162220392@qq.com"
# pfobbralyhfifhde
MAIL_PASSWORD = "wzgmxjpuvltlicef"
MAIL_DEFAULT_SENDER = "1162220392@qq.com"

UEDITOR_UPLOAD_TO_QINIU = False
UEDITOR_QINIU_ACCESS_KEY = "JJ-EN789DDyiZjd66VVT7K8BMT1p7DfWaOadBb4z"
UEDITOR_QINIU_SECRET_KEY = "F5UMffWvuEYAbr5p3eW_Nn5XaEAc5AQC97t-LSCz"
UEDITOR_QINIU_BUCKET_NAME = "pictureforric2"
UEDITOR_QINIU_DOMAIN = "http://q7y6ufg2l.bkt.clouddn.com/"


# celery配置
CELERY_RESULT_BACKEND = "redis://127.0.0.1:6379/0"
CELERY_BROKER_URL = "redis://127.0.0.1:6379/0"

