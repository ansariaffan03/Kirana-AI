
import os

APP_NAME = os.getenv("APP_NAME", "Kirana AI Backend")
APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
DEBUG = os.getenv("DEBUG", "false").lower() == "true"
