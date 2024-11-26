# softcultura

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/kmvit/softcultura
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

* Если у вас Linux/macOS

    ```
    source env/bin/activate
    ```

* Если у вас Windows (Git Bash)

    ```
    source env/scripts/activate
    ```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Запустить проект (переходим в директорию flask_amocrm_project):

```
flask run
```

В случае возникновения ошибки:

```
export FLASK_APP=main.py
flask run
```

## Pre-commit
Для минимизации трудностей во время разработки и поддержании высокого качества кода в разработке мы используем `pre-commit`. Данный фреймворк позволяет проверить код на соответствие `PEP8`, защитить ветки master и develop от непреднамеренного коммита, проверить корректность импортов и наличие trailing spaces.
`Pre-commit` конфигурируется с помощью специального файл `.pre-commit-config.yaml`. Для использования фреймворка его необходимо установить, выполнив команду из активированного виртуального окружения:

```bash
pip install pre-commit==3.6.0
```
или 

```bash
pip install -r requirements-dev.txt
```
Для принудительной проверки всех файлов можно выполнить команду:
```bash
pre-commit run --all-files
```
При первом запуске будут скачаны и установлены все необходимые хуки, указанные в конфигурационном файле.

Для автоматической проверки всех файлов необходимо инициализировать фреймворк командой:
```bash
pre-commit install
```
