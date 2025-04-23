import os
import yaml

class Config:
    """加载与管理 YAML 配置"""
    def __init__(self, path: str = None):
        cfg_path = path or os.path.join(
            os.path.dirname(__file__), '..', 'configs', 'default.yaml'
        )
        with open(cfg_path, 'r', encoding='utf-8') as f:
            self._data = yaml.safe_load(f)

    @property
    def log_level(self) -> str:
        return self._data.get('log_level', 'all')

    @log_level.setter
    def log_level(self, value: str):
        self._data['log_level'] = value

    @property
    def annotation(self) -> dict:
        return self._data.get('annotation', {})
