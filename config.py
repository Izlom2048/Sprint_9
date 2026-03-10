import os
from pathlib import Path

BASE_URL = os.getenv("BASE_URL", "https://foodgram-frontend-1.prakticum-team.ru/")
SELENOID_URL = os.getenv("SELENOID_URL", "")
BROWSER_NAME = os.getenv("BROWSER_NAME", "chrome")
BROWSER_VERSION = os.getenv("BROWSER_VERSION", "128.0")

PROJECT_ROOT = Path(__file__).resolve().parent
ASSETS_DIR = PROJECT_ROOT / "assets"
RECIPE_IMAGE_PATH = ASSETS_DIR / "recipe_image.png"
