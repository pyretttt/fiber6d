"""
    Starting launcher.
"""

import typing as t
from enum import Enum
from os import environ

from flask import Flask

from helpers import Singleton


class Configuration(Enum):
    DEBUG = 'DEBUG'
    TEST = 'TEST'

    @classmethod
    def from_environment(cls):
        cfg = environ.get('CONFIG')
        return cls(cfg)
    
    def host_config(self) -> t.Tuple[str, str]:
        ip = environ.get('IP', '127.0.0.1')
        return ip, '5000'
    
    def db_url(self) -> str:
        return environ.get('DB_URL', 'sqlite:///app.db')

class AppLauncher(metaclass=Singleton):
    """
        Configurable launcher.
        Created at application start.

        It is okay to retrieve instance with empty init params, after initial creation.
        For instance -> AppLauncher().
    """

    def __init__(self, 
    configuration: Configuration, 
    launch_command: t.Callable[[], None] = None):
        self.config = configuration
        self.launch_command = launch_command

    def launch(self, app: Flask):
        self.prelaunch_hook()
        ip, port = self.config.host_config()
        print(ip, port)
        app.run(host=ip, port=port, debug=self.config == Configuration.TEST)
    
    def prelaunch_hook(self):
        if command := self.launch_command and self.config == Configuration.Test:
            command()
        if self.config == Configuration.DEBUG:
            pass