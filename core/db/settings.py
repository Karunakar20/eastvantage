
import os
from pathlib import Path

# Get the base directory of the project
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SQlite Database URL
DATABASE_URL = f"sqlite:///{BASE_DIR}/address_book.db"
