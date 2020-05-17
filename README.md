# Drf Open Api Validator
## Usage

- Install django-open-api-validator with pip\
    ```shell script
    $ pip install drf-open-api-validator
    ```

<br>

- Add django application drf_open_api_validator to INSTALLED_APPS in settings.py
    ```python
    INSTALLED_APPS = [
        ...
        'drf_open_api_validator',
        ...
    ]
    ```

<br>

- Add RequestValidatorMiddleware and ResponseValidatorMiddleware to MIDDLEWARE in settings.py
    ```python
    MIDDLEWARE = [
        ...
        'drf_open_api_validator.middleware.RequestValidatorMiddleware',
        'drf_open_api_validator.middleware.ResponseValidatorMiddleware',
        ...
    ]
    ```

----------------------------------------------------------------

## Develop
- Install packages
    ```shell script
    $ pipenv shell
    $ pipenv install
    ```

<br>

- Test
    ```shell script
    $ pipenv run test
    ```

<br>

- Release
    ```shell script
    $ pipenv run clean
    $ pipenv run package
    $ pipenv run publish
    ```
