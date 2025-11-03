import logging
import os
from datetime import datetime
from app.config import AppConfig

class CustomLogger:
    def __init__(self, name="app_logger"):
        config = AppConfig().config  # Load global config

        log_dir = config['logging']['log_directory']
        os.makedirs(log_dir, exist_ok=True)

        current_time_stamp = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
        log_file_path = os.path.join(log_dir, f"log_{current_time_stamp}.log")

        logging.basicConfig(
            filename=log_file_path,
            filemode="a",
            level=getattr(logging, config['logging']['level']),
            format=config['logging']['log_file_format']
        )

        self.logger = logging.getLogger(name)

    def get_logger(self):
        return self.logger
