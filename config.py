from typing import Any, Optional
from pydantic import BaseModel

import yaml


class APIRemote(BaseModel):
    name: str
    service: Optional[str]
    key: Optional[str]
    url: Optional[str]


class LLMConfig:
    def __init__(self, remotes: list[APIRemote] = []):
        self.remotes: list[APIRemote] = remotes

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        return cls(**data)


class TTSConfig:
    def __init__(self, remotes: list[APIRemote] = [],enable: bool = False):
        self.remotes: list[APIRemote] = remotes
        self.enable: bool = enable

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        return cls(**data)

class IMConfig:
    def __init__(self, adapter:str,**kwargs):
        pass

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        pass

class Config:
    def __init__(self):
        with open('config.yml', 'r', encoding='utf-8') as file:
            config: dict[str, Any] = yaml.safe_load(file.read())
            self.llm = LLMConfig.from_dict(config['llm'])
            self.tts = TTSConfig.from_dict(config['tts'])

config = Config()