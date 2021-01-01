import django
from django.core.handlers.wsgi import WSGIHandler


def get_wsgi_application():
    """
    The public interface to Django's WSGI support. Return a WSGI callable.

    Avoids making django.core.handlers.WSGIHandler a public API, in case the
    internal WSGI implementation changes or moves in the future.
    """
    django.setup(set_prefix=False)
    return WSGIHandler()

"""
note:
这里是框架中对内部WSGI处理对象的一层包装，避免将内部的实现直接暴漏，为以后的修改或扩展保留空间。
django.setup 是根据配置文件对日志、应用进行初始化。
在配置完毕后返回给wsgi server一个可调用对象。

从这里开始，进入框架内部处理流程。
"""