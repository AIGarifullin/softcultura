"""Модуль запуска проекта."""

from flask import Flask

from .config import Config
from .logger_config import init_globals_logging

app = Flask(__name__)
app.config.from_object(Config)
init_globals_logging()

from . import api_views  # noqa
