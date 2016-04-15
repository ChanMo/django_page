Django-page
===========

基于django的简单页面模块

使用说明
--------

安装依赖:

.. code-block::

    pip install django-ckeditor

安装django-page:

.. code-block::

    pip install git+https://github.com/ChanMo/django_page.git

修改settings.py:

.. code-block::

    INSTALLED_APPS = (
        ...
        'page',
        ...
    )

修改urls.py:

.. code-block::

    url(r'^page/', include('page.urls')),

更新数据库:

.. code-block::

    python manage.py migrate

