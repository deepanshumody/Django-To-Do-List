
## Installation

`clone` the repository and use `pipenv` to create the virtual environment and install the dependencies. The instructions below assume you are using sqlite as your database, `~/dev` as your development directory, and pipenv as your environment manager. Modify as needed.

```
pip3 install --user git+https://github.com/pypa/pipenv.git
cd ~/dev
git clone git@github.com:dmod99/Django_To_Do
cd Django_To_Do
cd gtd-master
pipenv --python 3.6   # Initializes the virtual environment
pipenv install --dev  # Installs all dependencies
pipenv shell  # Activates the environment
```

Copy `local.example.py` to `local.py` and modify to match your local db credentials. In `local.py`:

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

Then:

`./manage.py migrate`

## Sample Screenshots

![image](https://user-images.githubusercontent.com/39831386/141997003-4c79817f-9989-467f-bcb0-8a6f9360688e.png)
![image](https://user-images.githubusercontent.com/39831386/141997400-3b87027a-f953-4b86-8fd4-1b43c4fd6906.png)

