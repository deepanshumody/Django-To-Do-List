Tried running manage.py runserver in python3 
Following Error Showed up
Look into it: 

Watching for file changes with StatReloader
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "/usr/lib/python3.8/threading.py", line 932, in _bootstrap_inner
    self.run()
  File "/usr/lib/python3.8/threading.py", line 870, in run
    self._target(*self._args, **self._kwargs)
  File "/home/athul/.local/lib/python3.8/site-packages/django/utils/autoreload.py", line 53, in wrapper
    fn(*args, **kwargs)
  File "/home/athul/.local/lib/python3.8/site-packages/django/core/management/commands/runserver.py", line 110, in inner_run
    autoreload.raise_last_exception()
  File "/home/athul/.local/lib/python3.8/site-packages/django/utils/autoreload.py", line 76, in raise_last_exception
    raise _exception[1]
  File "/home/athul/.local/lib/python3.8/site-packages/django/core/management/__init__.py", line 357, in execute
    autoreload.check_errors(django.setup)()
  File "/home/athul/.local/lib/python3.8/site-packages/django/utils/autoreload.py", line 53, in wrapper
    fn(*args, **kwargs)
  File "/home/athul/.local/lib/python3.8/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/home/athul/.local/lib/python3.8/site-packages/django/apps/registry.py", line 91, in populate
    app_config = AppConfig.create(entry)
  File "/home/athul/.local/lib/python3.8/site-packages/django/apps/config.py", line 90, in create
    module = import_module(entry)
  File "/usr/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'todo'