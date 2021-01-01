"""
WSGI config for dj_demo project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dj_demo.settings')

application = get_wsgi_application()

"""
note:
在部署时，需要将 application 暴漏给 wsgi server，
且 application 是一个可调用对象，接收 environ, start_response 这两个参数（标准的wsgi接口）。

对于生产部署（比如 uSWSGI 或者 gunicorn），是通过直接配置路径的方式，
对于runserver 本地调试的情况，Django的默认服务器会从配置项 WSGI_APPLICATION （项目的配置文件）中读取。
"""
