import os, yaml


class Vars:
    def __init__(self):
        self.BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        self.RUNTIME_DIR = os.path.join(self.BASE_DIR, "runtime")
        self.HISTORY_DIR = os.path.join(self.RUNTIME_DIR, "history.json")
        self.CONFIG_DIR = os.path.join(self.RUNTIME_DIR, "Config.yaml")


class Config:
    # TODO Config
    pass


VARS = vars()
CONFIG = config()
