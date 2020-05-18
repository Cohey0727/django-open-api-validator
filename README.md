# DRF Open Api Validator
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
        'drf_open_api_validator.middleware.SchemaValidatorMiddleware',
        ...
    ]
    ```


## Settings.py

| Parameter | Type | Default |
| --------- | ---- | ------- |
| DRF_OAV_SERVER_URL | str | '' |
| DRF_OAV_LOG_LEVEL | 'ignore' or 'info' or 'waring' or 'error' or 'exception' | 'waring' |
| DRF_OAV_SCHEMA_FILE_PATH | str | '' |  |

### DRF_OAV_SERVER_URL
Prefix of url. The details are as follows.  
[Swagger API Server and Base URL](https://swagger.io/docs/specification/api-host-and-base-path/)
 
### DRF_OAV_LOG_LEVEL
When 'info' or 'waring' or 'error', logging each level.<br>
When 'ignore', no check schema.<br>
When 'exception', raise exception.<br> 

### DRF_OAV_SCHEMA_FILE_PATH
Path of schema file

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
