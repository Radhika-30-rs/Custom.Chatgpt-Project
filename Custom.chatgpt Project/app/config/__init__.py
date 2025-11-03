import yaml
import os

class AppConfig:
    def __init__(self):
        config_path = os.path.join(os.path.dirname(__file__), "config.yaml")
        with open(config_path, "r") as file:
            self.config = yaml.safe_load(file)

        # Replace $(API_KEY) with actual environment variable
        api_key = os.getenv("API_KEY", "default-key")
        if "$(API_KEY)" in str(self.config):
            self.config["api"]["key"] = api_key

    def get(self, key, default=None):
        return self.config.get(key, default)

