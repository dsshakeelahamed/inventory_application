import os

from config import config as application_config


def get_environment_configs():
    env = os.getenv("FLASK_ENV", "dev").lower()
    cfg = application_config.DevConfig

    if env == "dev":
        cfg = application_config.DevConfig
    elif env == "test":
        cfg = application_config.TestConfig

    return cfg
