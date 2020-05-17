# Django Open Api Validator
## For Users
### Usage

- Install django-open-api-validator with pip\
    ```shell script
    $ pip install django-open-api-validator
    ```

- Add django application django_open_api_validator to INSTALLED_APPS in settings.py
    ```python
    INSTALLED_APPS = [
        ...
        'django_open_api_validator',
        ...
    ]
    ```

- Add RequestValidatorMiddleware and ResponseValidatorMiddleware to MIDDLEWARE in settings.py
    ```python
    MIDDLEWARE = [
        ...
        'django_open_api_validator.middleware.RequestValidatorMiddleware',
        'django_open_api_validator.middleware.ResponseValidatorMiddleware',
        ...
    ]
    ```


## For Developers
### Get started
```shell script
$ pipenv shell
```

### Test
```shell script
$ pipenv run test
```

### Release
```shell script
$ pipenv run clean
$ pipenv run package
$ pipenv run publish
```
