from typing import Any, Optional
from pydantic import BaseModel

import yaml


class APIRemote(BaseModel):
    name: str
    service: Optional[str]
    key: Optional[str]
    url: Optional[str]

class IMRemote(BaseModel):
    name: str
    adapter: str
    appid: str
    token: str
    ws_port: Optional[int]
    http_port: Optional[int]
    host: Optional[int]


class LLMConfig:
    def __init__(self, remotes: list[APIRemote] = []):
        self.remotes: list[APIRemote] = remotes

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        return cls(**data)


class TTSConfig:
    def __init__(self, remotes: list[APIRemote] = [], enable: bool = False):
        self.remotes: list[APIRemote] = remotes
        self.enable: bool = enable

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        return cls(**data)


class IMConfig:
    def __init__(self, remotes: list[IMRemote] = []):
        self.remotes: list[IMRemote] = remotes

    @classmethod
    def from_dict(cls, data: dict[str, Any]):
        return cls(**data)


class Config:
    def __init__(self):
        with open('config.yml', 'r', encoding='utf-8') as file:
            config: dict[str, Any] = yaml.safe_load(file.read())
            self.llm = LLMConfig.from_dict(config['llm'])
            self.tts = TTSConfig.from_dict(config['tts'])
            self.im = IMConfig.from_dict(config['im'])


config = Config()
